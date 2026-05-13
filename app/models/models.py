import uuid # تصحيح الخطأ الإملائي هنا
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean, Text, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.session import Base

def generate_uuid():
    return str(uuid.uuid4())

class TimestampMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    is_deleted = Column(Boolean, default=False)

# Many-to-Many table for Favorites
favorites = Table(
    'favorites',
    Base.metadata,
    Column('user_id', String, ForeignKey('users.telegram_id', ondelete="CASCADE")),
    Column('university_id', String, ForeignKey('universities.id', ondelete="CASCADE"))
)

class Country(Base, TimestampMixin):
    __tablename__ = "countries"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, unique=True, nullable=False)
    code = Column(String, unique=True)
    # إضافة علاقة لجعل الحذف أسهل (إذا حذفت دولة تحذف مدنها)
    cities = relationship("City", back_populates="country", cascade="all, delete-orphan")

class City(Base, TimestampMixin):
    __tablename__ = "cities"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    country_id = Column(String, ForeignKey("countries.id", ondelete="CASCADE"))
    
    country = relationship("Country", back_populates="cities")
    universities = relationship("University", back_populates="city", cascade="all, delete-orphan")

class University(Base, TimestampMixin):
    __tablename__ = "universities"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    description = Column(Text)
    location_url = Column(String)
    website = Column(String)
    registration_link = Column(String)
    international_recognition = Column(Text)
    city_id = Column(String, ForeignKey("cities.id", ondelete="CASCADE"))
    
    city = relationship("City", back_populates="universities")
    faculties = relationship("Faculty", back_populates="university", cascade="all, delete-orphan")
    living_costs = relationship("LivingCost", back_populates="university", cascade="all, delete-orphan")
    scholarships = relationship("Scholarship", back_populates="university", cascade="all, delete-orphan")
    reviews = relationship("StudentReview", back_populates="university", cascade="all, delete-orphan")
    dormitories = relationship("Dormitory", back_populates="university", cascade="all, delete-orphan")

class Faculty(Base, TimestampMixin):
    __tablename__ = "faculties"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    university_id = Column(String, ForeignKey("universities.id", ondelete="CASCADE"))
    
    university = relationship("University", back_populates="faculties")
    departments = relationship("Department", back_populates="faculty", cascade="all, delete-orphan")

class Department(Base, TimestampMixin):
    __tablename__ = "departments"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    duration_years = Column(Integer)
    study_language = Column(String)
    annual_fees = Column(Float)
    semester_fees = Column(Float)
    required_grade = Column(Float)
    study_system = Column(String)
    faculty_id = Column(String, ForeignKey("faculties.id", ondelete="CASCADE"))
    
    faculty = relationship("Faculty", back_populates="departments")
    admission_requirements = relationship("AdmissionRequirement", back_populates="department", cascade="all, delete-orphan")

class Dormitory(Base, TimestampMixin):
    __tablename__ = "dormitories"
    id = Column(String, primary_key=True, default=generate_uuid)
    university_id = Column(String, ForeignKey("universities.id", ondelete="CASCADE"))
    cost = Column(Float)
    room_type = Column(String)
    includes_internet = Column(Boolean, default=False)
    includes_food = Column(Boolean, default=False)
    gender = Column(String)
    
    university = relationship("University", back_populates="dormitories") # أضفت هذه العلاقة لتكتمل الحلقة

class LivingCost(Base, TimestampMixin):
    __tablename__ = "living_costs"
    id = Column(String, primary_key=True, default=generate_uuid)
    university_id = Column(String, ForeignKey("universities.id", ondelete="CASCADE"))
    food_cost = Column(Float)
    transport_cost = Column(Float)
    electricity_cost = Column(Float)
    internet_cost = Column(Float)
    water_cost = Column(Float)
    total_monthly_avg = Column(Float)
    
    university = relationship("University", back_populates="living_costs")

class Scholarship(Base, TimestampMixin):
    __tablename__ = "scholarships"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String)
    discount_percentage = Column(Float)
    conditions = Column(Text)
    university_id = Column(String, ForeignKey("universities.id", ondelete="CASCADE"))
    
    university = relationship("University", back_populates="scholarships")

class AdmissionRequirement(Base, TimestampMixin):
    __tablename__ = "admission_requirements"
    id = Column(String, primary_key=True, default=generate_uuid)
    requirement_text = Column(Text)
    department_id = Column(String, ForeignKey("departments.id", ondelete="CASCADE"))
    
    department = relationship("Department", back_populates="admission_requirements")

class StudentReview(Base, TimestampMixin):
    __tablename__ = "student_reviews"
    id = Column(String, primary_key=True, default=generate_uuid)
    rating = Column(Integer)
    comment = Column(Text)
    user_id = Column(String, ForeignKey("users.telegram_id", ondelete="CASCADE"))
    university_id = Column(String, ForeignKey("universities.id", ondelete="CASCADE"))
    
    university = relationship("University", back_populates="reviews")

class User(Base, TimestampMixin):
    __tablename__ = "users"
    telegram_id = Column(String, primary_key=True)
    username = Column(String)
    full_name = Column(String)
    favorite_universities = relationship("University", secondary=favorites)
