from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class CountryBase(BaseModel):
    name: str
    code: Optional[str] = None

class CountryCreate(CountryBase):
    pass

class Country(CountryBase):
    id: str
    class Config:
        from_attributes = True

class CityBase(BaseModel):
    name: str
    country_id: str

class City(CityBase):
    id: str
    class Config:
        from_attributes = True

class UniversityBase(BaseModel):
    name: str
    description: Optional[str] = None
    city_id: str
    website: Optional[str] = None

class University(UniversityBase):
    id: str
    class Config:
        from_attributes = True

class FacultyBase(BaseModel):
    name: str
    university_id: str

class Faculty(FacultyBase):
    id: str
    class Config:
        from_attributes = True

class DepartmentBase(BaseModel):
    name: str
    faculty_id: str
    annual_fees: Optional[float] = None
    study_language: Optional[str] = None

class Department(DepartmentBase):
    id: str
    class Config:
        from_attributes = True
