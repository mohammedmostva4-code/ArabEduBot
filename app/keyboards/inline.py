from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_start_keyboard():
    keyboard = [
        [InlineKeyboardButton("🔍 ابدأ البحث", callback_data="start_search")],
        [InlineKeyboardButton("⭐ المفضلة", callback_data="favorites"), 
         InlineKeyboardButton("📊 مقارنة", callback_data="compare")],
        [InlineKeyboardButton("ℹ️ حول البوت", callback_data="about")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_countries_keyboard(countries):
    keyboard = []
    for i in range(0, len(countries), 2):
        row = [InlineKeyboardButton(countries[i].name, callback_data=f"country_{countries[i].id}")]
        if i + 1 < len(countries):
            row.append(InlineKeyboardButton(countries[i+1].name, callback_data=f"country_{countries[i+1].id}"))
        keyboard.append(row)
    keyboard.append([InlineKeyboardButton("🔙 رجوع", callback_data="main_menu")])
    return InlineKeyboardMarkup(keyboard)

def get_universities_keyboard(universities, country_id):
    keyboard = []
    for uni in universities:
        keyboard.append([InlineKeyboardButton(uni.name, callback_data=f"uni_{uni.id}")])
    keyboard.append([InlineKeyboardButton("🔙 رجوع", callback_data="start_search")])
    return InlineKeyboardMarkup(keyboard)

def get_faculties_keyboard(faculties, uni_id):
    keyboard = []
    for fac in faculties:
        keyboard.append([InlineKeyboardButton(fac.name, callback_data=f"fac_{fac.id}")])
    keyboard.append([InlineKeyboardButton("🔙 رجوع", callback_data=f"uni_{uni_id}")])
    return InlineKeyboardMarkup(keyboard)

def get_departments_keyboard(departments, fac_id):
    keyboard = []
    for dept in departments:
        keyboard.append([InlineKeyboardButton(dept.name, callback_data=f"dept_{dept.id}")])
    keyboard.append([InlineKeyboardButton("🔙 رجوع", callback_data=f"fac_{fac_id}")])
    return InlineKeyboardMarkup(keyboard)

def get_back_button(callback_data):
    return InlineKeyboardMarkup([[InlineKeyboardButton("🔙 رجوع", callback_data=callback_data)]])
