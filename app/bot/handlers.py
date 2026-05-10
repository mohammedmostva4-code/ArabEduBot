from telegram import Update
from telegram.ext import ContextTypes
from app.database.session import SessionLocal
from app.models import models
from app.keyboards import inline

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    db = SessionLocal()
    # Save user if not exists
    db_user = db.query(models.User).filter(models.User.telegram_id == str(user.id)).first()
    if not db_user:
        db_user = models.User(telegram_id=str(user.id), username=user.username, full_name=user.full_name)
        db.add(db_user)
        db.commit()
    db.close()

    welcome_text = (
        f"مرحباً بك {user.first_name} في **ArabEduBot** 🎓\n\n"
        "منصتك الذكية للبحث عن الجامعات والتخصصات في العالم العربي.\n"
        "نحن هنا لمساعدتك في اختيار مستقبلك الأكاديمي."
    )
    await update.message.reply_text(welcome_text, reply_markup=inline.get_start_keyboard(), parse_mode="Markdown")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    db = SessionLocal()

    if data == "main_menu":
        await query.edit_message_text(
            "القائمة الرئيسية:",
            reply_markup=inline.get_start_keyboard()
        )

    elif data == "start_search":
        countries = db.query(models.Country).all()
        await query.edit_message_text(
            "الرجاء اختيار الدولة:",
            reply_markup=inline.get_countries_keyboard(countries)
        )

    elif data.startswith("country_"):
        country_id = data.split("_")[1]
        unis = db.query(models.University).join(models.City).filter(models.City.country_id == country_id).all()
        await query.edit_message_text(
            "الجامعات المتوفرة:",
            reply_markup=inline.get_universities_keyboard(unis, country_id)
        )

    elif data.startswith("uni_"):
        uni_id = data.split("_")[1]
        uni = db.query(models.University).filter(models.University.id == uni_id).first()
        facs = db.query(models.Faculty).filter(models.Faculty.university_id == uni_id).all()
        
        text = f"🎓 **{uni.name}**\n\n{uni.description or 'لا يوجد وصف'}\n\n📍 الموقع: {uni.location_url or 'غير متوفر'}\n🌐 الموقع الإلكتروني: {uni.website or 'غير متوفر'}"
        await query.edit_message_text(
            text,
            reply_markup=inline.get_faculties_keyboard(facs, uni_id),
            parse_mode="Markdown"
        )

    elif data.startswith("fac_"):
        fac_id = data.split("_")[1]
        fac = db.query(models.Faculty).filter(models.Faculty.id == fac_id).first()
        depts = db.query(models.Department).filter(models.Department.faculty_id == fac_id).all()
        
        await query.edit_message_text(
            f"أقسام كلية {fac.name}:",
            reply_markup=inline.get_departments_keyboard(depts, fac_id)
        )

    elif data.startswith("dept_"):
        dept_id = data.split("_")[1]
        dept = db.query(models.Department).filter(models.Department.id == dept_id).first()
        
        details = (
            f"📚 **التخصص: {dept.name}**\n"
            f"⏱ مدة الدراسة: {dept.duration_years} سنوات\n"
            f"🗣 لغة الدراسة: {dept.study_language}\n"
            f"💰 الرسوم السنوية: {dept.annual_fees}$\n"
            f"📈 المعدل المطلوب: {dept.required_grade}%\n"
            f"⚙️ نظام الدراسة: {dept.study_system}\n"
        )
        await query.edit_message_text(
            details,
            reply_markup=inline.get_back_button(f"fac_{dept.faculty_id}"),
            parse_mode="Markdown"
        )

    db.close()
