import uuid
from app.database.session import SessionLocal, engine, Base
from app.models.models import Country, City, University, Faculty, Department, Dormitory, LivingCost, Scholarship, AdmissionRequirement
from app.data_structure import ARAB_COUNTRIES_DATA

def generate_uuid():
    return str(uuid.uuid4())

def seed_data():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if not ARAB_COUNTRIES_DATA:
        print("❌ لم يتم العثور على بيانات")
        return

    try:
        for country_data in ARAB_COUNTRIES_DATA:
            country = Country(id=generate_uuid(), name=country_data["name"], code=country_data["code"])
            db.add(country)
            db.flush()

            for city_data in country_data.get("cities", []):
                city = City(id=generate_uuid(), name=city_data["name"], country_id=country.id)
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

                    for faculty_name in uni_data.get("faculties", []):
                        faculty = Faculty(id=generate_uuid(), name=faculty_name, university_id=university.id)
                        db.add(faculty)
                        db.flush()

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

                    if "living_costs" in uni_data:
                        living_cost = LivingCost(
                            id=generate_uuid(),
                            university_id=university.id,
                            food_cost=uni_data["living_costs"].get("food"),
                            transport_cost=uni_data["living_costs"].get("transport"),
                            total_monthly_avg=uni_data["living_costs"].get("total")
                        )
                        db.add(living_cost)

                    if "dormitory" in uni_data:
                        dormitory = Dormitory(
                            id=generate_uuid(),
                            university_id=university.id,
                            cost=uni_data["dormitory"].get("cost"),
                            room_type=uni_data["dormitory"].get("room_type"),
                            includes_internet=True,
                            includes_food=False,
                            gender="Mixed"
                        )
                        db.add(dormitory)

        db.commit()
        print("✅ تمت تغذية قاعدة البيانات بنجاح - 22 دولة عربية!")
    except Exception as e:
        db.rollback()
        print(f"❌ خطأ: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
