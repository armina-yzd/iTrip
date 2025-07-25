from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from app.services.media_services import MediaService
from app.domain.models.media import MediaFile
from datetime import datetime
from app.domain.schemas.media_schema import MediaDetails, MediaResponse
import io
from app.core.db.database import get_media_service
from app.services.auth import get_current_user
from typing import Annotated, List
from fastapi.security import HTTPBearer
from app.domain.schemas.token_schema import TokenData

router = APIRouter(prefix="/media", tags=["media"])
security = HTTPBearer()

@router.post("/upload", response_model=MediaResponse, status_code=status.HTTP_201_CREATED)
async def upload_file(
    ticket_id: int,
    file: UploadFile = File(...),
    current_user: TokenData = Depends(get_current_user),
    media_service: MediaService = Depends(get_media_service),
):
    try:
        contents = await file.read()
        media = MediaFile(
            filename=file.filename,
            content_type=file.content_type,
            size=len(contents),
            upload_date=datetime.utcnow(),
            ticket_id=ticket_id
        )
        uploaded_media = await media_service.upload_media(media, contents,ticket_id,current_user.id)
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
    current_user: TokenData = Depends(get_current_user),
    media_service: MediaService = Depends(get_media_service)
):
    try:
        media, _ = await media_service.download_media(file_id)   
        success = await media_service.delete_media(file_id,media.ticket_id,current_user.id)
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
    
@router.get("/ticket/{ticket_id}")
async def get_media_by_ticket_id(
    ticket_id: int,
    media_service: MediaService = Depends(get_media_service)
):
    try:
        media_files = await media_service.get_media_by_ticket(ticket_id)
        return media_files
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error in get_media_by_ticket_id: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving media files"
        )