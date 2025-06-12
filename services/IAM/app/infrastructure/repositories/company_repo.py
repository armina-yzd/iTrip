from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.db.database import get_db
from app.domain.models.company import Company

class CompanyRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def create_company(self, company: Company) -> Company:
        self.db.add(company)
        self.db.commit()
        self.db.refresh(company)
        return company

    def get_company_by_email(self, email: str) -> Company:
        return self.db.query(Company).filter(Company.email == email).first()
    
    def get_company_by_name(self, name: str) -> Company:
        return self.db.query(Company).filter(Company.name == name).first()
    
    def get_banned_company(self, email: str) -> Company:
        return self.db.query(Company).filter(Company.email == email, Company.is_banned).first()
    
    def get_verified_company(self, email: str) -> Company:
        return self.db.query(Company).filter(Company.email == email, Company.is_verified).first()
    
    def get_company_name(self, id: int) -> str:
        company = self.db.query(Company).filter(Company.id == id).first()
        if not company:
            raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, 
                    detail="company does not exist"
                )
        return company.name