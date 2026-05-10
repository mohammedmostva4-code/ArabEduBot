from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from sqladmin import Admin, ModelView
from app.database.session import engine, get_db, Base
from app.models import models
from app.api import schemas
from app.utils.config import settings

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="ArabEduBot API", description="API for ArabEduBot Educational Platform")

# Admin Panel Setup
admin = Admin(app, engine)

class CountryAdmin(ModelView, model=models.Country):
    column_list = [models.Country.id, models.Country.name, models.Country.code]

class CityAdmin(ModelView, model=models.City):
    column_list = [models.City.id, models.City.name, models.City.country]

class UniversityAdmin(ModelView, model=models.University):
    column_list = [models.University.id, models.University.name, models.University.city]

class FacultyAdmin(ModelView, model=models.Faculty):
    column_list = [models.Faculty.id, models.Faculty.name, models.Faculty.university]

class DepartmentAdmin(ModelView, model=models.Department):
    column_list = [models.Department.id, models.Department.name, models.Department.faculty, models.Department.annual_fees]

admin.add_view(CountryAdmin)
admin.add_view(CityAdmin)
admin.add_view(UniversityAdmin)
admin.add_view(FacultyAdmin)
admin.add_view(DepartmentAdmin)

@app.get("/")
def read_root():
    return {"message": "Welcome to ArabEduBot API", "status": "running", "admin_panel": "/admin"}

@app.get("/countries", response_model=List[schemas.Country])
def get_countries(db: Session = Depends(get_db)):
    return db.query(models.Country).all()

@app.get("/universities", response_model=List[schemas.University])
def get_universities(country_id: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(models.University)
    if country_id:
        query = query.join(models.City).filter(models.City.country_id == country_id)
    return query.all()

@app.get("/universities/{uni_id}", response_model=schemas.University)
def get_university(uni_id: str, db: Session = Depends(get_db)):
    uni = db.query(models.University).filter(models.University.id == uni_id).first()
    if not uni:
        raise HTTPException(status_code=404, detail="University not found")
    return uni
