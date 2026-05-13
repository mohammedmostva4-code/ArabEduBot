import uuid
from app.database.session import SessionLocal, engine
from app.models import models

def generate_uuid():
    return str(uuid.uuid4())

def seed_data():
    # إنشاء الجداول في قاعدة البيانات إذا لم تكن موجودة
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # قائمة الدول العربية
        countries_data = [
            {"name": "اليمن", "code": "YE"}, {"name": "مصر", "code": "EG"},
            {"name": "السعودية", "code": "SA"}, {"name": "الإمارات", "code": "AE"},
            {"name": "الأردن", "code": "JO"}, {"name": "المغرب", "code": "MA"},
            {"name": "العراق", "code": "IQ"}, {"name": "قطر", "code": "QA"}
            # يمكنك إضافة البقية هنا بنفس النمط
        ]

        print("جاري إضافة الدول والمدن...")
        for c_data in countries_data:
            # التأكد من عدم تكرار الدولة
            existing_country = db.query(models.Country).filter_by(name=c_data["name"]).first()
            if not existing_country:
                country = models.Country(id=generate_uuid(), name=c_data["name"], code=c_data["code"])
                db.add(country)
                db.flush() # للحصول على ID الدولة لربط المدينة بها

                # إضافة العاصمة كمدينة افتراضية
                city_name = "العاصمة" # يمكنك تخصيصها لاحقاً
                city = models.City(id=generate_uuid(), name=city_name, country_id=country.id)
                db.add(city)
        
        db.commit()
        print("✅ تمت العملية بنجاح! قاعدة البيانات الآن تحتوي على هيكل الوطن العربي.")

    except Exception as e:
        print(f"❌ حدث خطأ: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
