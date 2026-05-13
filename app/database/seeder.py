
from app.database.session import SessionLocal, engine, Base
from app.models.models import Country, City, University, Faculty, Department, Dormitory, LivingCost, Scholarship, AdmissionRequirement, StudentReview, User

# Import the data structure
from app.data_structure import ARAB_COUNTRIES_DATA

def seed_data():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # Seed Countries, Cities, Universities, Faculties, Departments, LivingCosts, Dormitories
        for country_data in ARAB_COUNTRIES_DATA:
            country = Country(name=country_data["name"], code=country_data["code"])
            db.add(country)
            db.flush() # Flush to get the country.id

            for city_data in country_data["cities"]:
                city = City(name=city_data["name"], country_id=country.id)
                db.add(city)
                db.flush() # Flush to get the city.id

                for university_data in city_data["universities"]:
                    university = University(
                        name=university_data["name"],
                        description=university_data["description"],
                        website=university_data["website"],
                        city_id=city.id
                    )
                    db.add(university)
                    db.flush() # Flush to get the university.id

                    # Add Faculties
                    for faculty_name in university_data["faculties"]:
                        faculty = Faculty(name=faculty_name, university_id=university.id)
                        db.add(faculty)
                        db.flush() # Flush to get the faculty.id

                        # Add Departments (simplified for now, can be expanded)
                        for dept_data in university_data["departments"]:
                            department = Department(
                                name=dept_data["name"],
                                faculty_id=faculty.id,
                                duration_years=dept_data.get("duration"),
                                annual_fees=dept_data.get("fees"),
                                study_language="العربية/الإنجليزية", # Default language
                                study_system="فصلي" # Default system
                            )
                            db.add(department)
                            db.flush()

                            # Add Admission Requirements (simplified)
                            admission_req = AdmissionRequirement(
                                requirement_text="شهادة الثانوية العامة بمعدل جيد جداً",
                                department_id=department.id
                            )
                            db.add(admission_req)

                    # Add Living Costs
                    if "living_costs" in university_data:
                        living_cost = LivingCost(
                            university_id=university.id,
                            food_cost=university_data["living_costs"].get("food"),
                            transport_cost=university_data["living_costs"].get("transport"),
                            total_monthly_avg=university_data["living_costs"].get("total")
                        )
                        db.add(living_cost)

                    # Add Dormitory Info
                    if "dormitory" in university_data:
                        dormitory = Dormitory(
                            university_id=university.id,
                            cost=university_data["dormitory"].get("cost"),
                            room_type=university_data["dormitory"].get("room_type"),
                            includes_internet=True, # Default
                            includes_food=False, # Default
                            gender="Mixed" # Default
                        )
                        db.add(dormitory)

        db.commit()
        print("✅ Database seeded successfully with all 22 Arab countries!")
    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
