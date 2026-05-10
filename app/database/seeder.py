from app.database.session import SessionLocal
from app.models import models

from app.models.models import Base
from app.database.session import engine

def seed_data():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    # Add Countries
    yemen = models.Country(name="اليمن", code="YE")
    egypt = models.Country(name="مصر", code="EG")
    saudi = models.Country(name="السعودية", code="SA")
    
    db.add_all([yemen, egypt, saudi])
    db.commit()
    
    # Add Cities
    sanaa = models.City(name="صنعاء", country_id=yemen.id)
    cairo = models.City(name="القاهرة", country_id=egypt.id)
    riyadh = models.City(name="الرياض", country_id=saudi.id)
    
    db.add_all([sanaa, cairo, riyadh])
    db.commit()
    
    # Add University
    su = models.University(
        name="جامعة صنعاء", 
        description="أقدم وأكبر جامعة في اليمن", 
        city_id=sanaa.id,
        website="https://su.edu.ye"
    )
    cu = models.University(
        name="جامعة القاهرة", 
        description="من أعرق الجامعات العربية", 
        city_id=cairo.id,
        website="https://cu.edu.eg"
    )
    
    db.add_all([su, cu])
    db.commit()
    
    # Add Faculty
    eng_su = models.Faculty(name="كلية الهندسة", university_id=su.id)
    med_cu = models.Faculty(name="كلية الطب", university_id=cu.id)
    
    db.add_all([eng_su, med_cu])
    db.commit()
    
    # Add Department
    it_su = models.Department(
        name="تكنولوجيا المعلومات", 
        faculty_id=eng_su.id,
        duration_years=5,
        study_language="العربية/الإنجليزية",
        annual_fees=500,
        required_grade=85,
        study_system="فصلي"
    )
    
    db.add(it_su)
    db.commit()
    db.close()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
