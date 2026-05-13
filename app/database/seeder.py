import uuid
from app.database.session import SessionLocal, engine
from app.models.models import Base, Country, City, University, Faculty, Department, Dormitory, LivingCost, Scholarship, AdmissionRequirement

# هذا هو الملف الذي سننشئه في الخطوة القادمة
try:
    from app.data_structure import ARAB_COUNTRIES_DATA
except ImportError:
    ARAB_COUNTRIES_DATA = [] # قائمة فارغة مؤقتاً لتجنب انهيار الكود

def generate_uuid():
    return str(uuid.uuid4())

def seed_data():
    # تنبيه: drop_all ستمسح كل بياناتك القديمة، استخدمها فقط عند التصفير
    # Base.metadata.drop_all(bind=engine) 
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if not ARAB_COUNTRIES_DATA:
        print("❌ خطأ: لم يتم العثور على بيانات في ARAB_COUNTRIES_DATA")
        return

    try:
        for country_data in ARAB_COUNTRIES_DATA:
            # إضافة الدولة مع توليد ID يدوي لضمان الربط
            country = Country(
                id=generate_uuid(),
                name=country_data["name"], 
                code=country_data["code"]
            )
            db.add(country)
            db.flush() 

            for city_data in country_data.get("cities", []):
                city = City(
                    id=generate_uuid(),
                    name=city_name := city_data["name"], 
                    country_id=country.id
                )
                db.add(city)
                db.flush() 

                for uni_data in city_data.get("universities", []):
                    university = University(
                        id=generate_uuid(),
                        name=uni_data["name"],
                        description=uni_data.get("description", ""),
                        website=uni_data.get("website", ""),
                        city_id=city.id
                    )
                    db.add(university)
                    db.flush()

                    # إضافة الكليات
                    for faculty_name in uni_data.get("faculties", []):
                        faculty = Faculty(id=generate_uuid(), name=faculty_name, university_id=university.id)
                        db.add(faculty)
                        db.flush()

                        # إضافة الأقسام
                        for dept_data in uni_data.get("departments", []):
                            department = Department(
                                id=generate_uuid(),
                                name=dept_data["name"],
                                faculty_id=faculty.id,
                                duration_years=dept_data.get("duration", 4),
                                annual_fees=float(dept_data.get("fees", 0)),
                                study_language=dept_data.get("language", "العربية/الإنجليزية"),
                                study_system="فصلي"
                            )
                            db.add(department)
                            db.flush()

        db.commit()
        print("✅ تمت تغذية قاعدة البيانات بنجاح!")
    except Exception as e:
        db.rollback()
        print(f"❌ خطأ أثناء التغذية: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
