from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from app.services.media_services import MediaService
from app.domain.models.media import MediaFile
from datetime import datetime
from app.domain.schemas.media_schema import MediaResponse, MediaCreate
import io
from app.core.db.database import get_media_service
from app.services.auth import get_current_user
from typing import Annotated
from fastapi.security import HTTPBearer
from app.domain.schemas.token_schema import TokenData

router = APIRouter(prefix="/media", tags=["media"])
security = HTTPBearer()

@router.post("/upload", response_model=MediaResponse, status_code=status.HTTP_201_CREATED)
async def upload_file(
    file: UploadFile = File(...),
    # owner: TokenData = Depends(get_current_user),  # You'll need to implement this
    media_service: MediaService = Depends(get_media_service)
):
    try:
        contents = await file.read()
        media = MediaFile(
            filename=file.filename,
            content_type=file.content_type,
            size=len(contents),
            upload_date=datetime.utcnow(),
            # owner_id=owner.id
        )
        
        uploaded_media = await media_service.upload_media(media, contents)
        return MediaResponse(
            id=uploaded_media.id,
            filename=uploaded_media.filename,
            content_type=uploaded_media.content_type,
            size=uploaded_media.size
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/{file_id}")
async def download_file(
    file_id: str,
    media_service: MediaService = Depends(get_media_service)
):
    try:
        media, file_data = await media_service.download_media(file_id)
        return StreamingResponse(
            io.BytesIO(file_data),
            media_type=media.content_type,
            headers={"Content-Disposition": f"filename={media.filename}"}
        )
    except FileNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="File not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.delete("/{file_id}")
async def delete_file(
    file_id: str,
    # owner: TokenData = Depends(get_current_user),  # You'll need to implement this
    media_service: MediaService = Depends(get_media_service)
):
    try:
        # First verify the user owns the file
        media, _ = await media_service.download_media(file_id)
        # if media.owner_id != owner.id:
        #     raise HTTPException(
        #         status_code=status.HTTP_403_FORBIDDEN,
        #         detail="Not authorized to delete this file"
        #     )
            
        success = await media_service.delete_media(file_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="File not found"
            )
        return {"message": "File deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )