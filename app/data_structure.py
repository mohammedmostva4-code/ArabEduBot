
# هيكل البيانات لـ 22 دولة عربية
ARAB_COUNTRIES_DATA = [
{
        "name": "اليمن",
        "code": "YE",
        "cities": [
            {
                "name": "حجة",
                "universities": [
                    {
                        "name": "جامعة حجة",
                        "description": "جامعة حكومية تخدم إقليم حجة، تعتبر رائدة في إعداد الكوادر المؤهلة في العلوم التطبيقية والإنسانية.",
                        "website": "https://hujja-univ.edu.ye",
                        "faculties": [
                            "كلية الطب والعلوم الصحية", 
                            "كلية علوم الحاسوب وتقنية المعلومات",
                            "كلية العلوم التطبيقية", 
                            "كلية العلوم المالية والمصرفية", 
                            "كلية التربية والعلوم الإنسانية",
                            "كلية الزراعة والطب البيطري",
                            "كلية التربية - عبس"
                        ],
                        "departments": [
                            {"name": "الطب البشري", "duration": 7, "fees": 1500, "language": "الإنجليزية"},
                            {"name": "الأمن السيبراني", "duration": 4, "fees": 450, "language": "الإنجليزية"},
                            {"name": "تقنية المعلومات (IT)", "duration": 4, "fees": 400, "language": "الإنجليزية/العربية"},
                            {"name": "علوم الحاسوب", "duration": 4, "fees": 400, "language": "الإنجليزية"},
                            {"name": "المختبرات الطبية", "duration": 4, "fees": 600, "language": "الإنجليزية"},
                            {"name": "المحاسبة", "duration": 4, "fees": 300, "language": "العربية"},
                            {"name": "العلوم المالية والمصرفية", "duration": 4, "fees": 300, "language": "العربية"},
                            {"name": "الطب البيطري", "duration": 5, "fees": 400, "language": "العربية/الإنجليزية"}
                        ]
                    }
                ]
            },
            {
                "name": "عمران",
                "universities": [
                    {
                        "name": "جامعة عمران",
                        "description": "جامعة حكومية متميزة، تشهد نهضة تعليمية كبيرة في مجالات الطب والأعمال الدولية.",
                        "website": "https://amu.edu.ye",
                        "faculties": [
                            "كلية الطب والعلوم الصحية", 
                            "كلية الهندسة وتقنية المعلومات", 
                            "كلية الأعمال - خمر",
                            "كلية الشريعة والقانون"
                        ],
                        "departments": [
                            {"name": "الطب البشري", "duration": 7, "fees": 1500, "language": "الإنجليزية"},
                            {"name": "الهندسة المدنية", "duration": 5, "fees": 600, "language": "الإنجليزية"},
                            {"name": "المحاسبة الدولية (بالإنجليزي)", "duration": 4, "fees": 500, "language": "الإنجليزية"},
                            {"name": "إدارة الأعمال الدولية", "duration": 4, "fees": 500, "language": "الإنجليزية"}
                        ]
                    }
                ]
            },
            {
                "name": "صعدة",
                "universities": [
                    {
                        "name": "جامعة صعدة",
                        "description": "صرح أكاديمي حكومي يقدم برامج متميزة في العلوم التطبيقية والإنسانية.",
                        "website": "https://saada-univ.net",
                        "faculties": ["كلية الطب", "كلية العلوم التطبيقية", "كلية العلوم الإنسانية والإدارية"],
                        "departments": [
                            {"name": "الطب البشري", "duration": 7, "fees": 1500, "language": "الإنجليزية"},
                            {"name": "نظم المعلومات", "duration": 4, "fees": 400, "language": "الإنجليزية/العربية"},
                            {"name": "المحاسبة", "duration": 4, "fees": 300, "language": "العربية"}
                        ]
                    }
                ]
            }
        ]
    }
    {
        "name": "مصر", "code": "EG",
        "cities": [
            {
                "name": "الجيزة",
                "universities": [
                    {
                        "name": "جامعة القاهرة",
                        "description": "من أعرق الجامعات في الوطن العربي.",
                        "website": "https://cu.edu.eg",
                        "faculties": ["كلية الطب", "كلية الهندسة", "كلية الاقتصاد والعلوم السياسية"],
                        "departments": [
                            {"name": "الطب والجراحة", "fees": 6000, "duration": 6},
                            {"name": "الهندسة المدنية", "fees": 5000, "duration": 5}
                        ],
                        "living_costs": {"food": 200, "transport": 100, "total": 500},
                        "dormitory": {"cost": 100, "room_type": "Shared"}
                    }
                ]
            }
        ]
    },
    {
        "name": "السعودية", "code": "SA",
        "cities": [
            {
                "name": "الرياض",
                "universities": [
                    {
                        "name": "جامعة الملك سعود",
                        "description": "رائدة التعليم العالي في المملكة.",
                        "website": "https://ksu.edu.sa",
                        "faculties": ["كلية الطب", "كلية الهندسة", "كلية العلوم"],
                        "departments": [
                            {"name": "الطب البشري", "fees": 0, "duration": 7},
                            {"name": "هندسة البرمجيات", "fees": 0, "duration": 5}
                        ],
                        "living_costs": {"food": 400, "transport": 200, "total": 1000},
                        "dormitory": {"cost": 0, "room_type": "Single"}
                    }
                ]
            }
        ]
    },
    {
        "name": "الإمارات", "code": "AE",
        "cities": [
            {
                "name": "أبوظبي",
                "universities": [
                    {
                        "name": "جامعة خليفة",
                        "description": "جامعة بحثية عالمية المستوى.",
                        "website": "https://ku.ac.ae",
                        "faculties": ["كلية الهندسة", "كلية الطب والعلوم الصحية"],
                        "departments": [
                            {"name": "الهندسة الميكانيكية", "fees": 20000, "duration": 4},
                            {"name": "الطب", "fees": 25000, "duration": 6}
                        ],
                        "living_costs": {"food": 600, "transport": 300, "total": 1500},
                        "dormitory": {"cost": 800, "room_type": "Single"}
                    }
                ]
            }
        ]
    },
    {
        "name": "الأردن", "code": "JO",
        "cities": [
            {
                "name": "عمان",
                "universities": [
                    {
                        "name": "الجامعة الأردنية",
                        "description": "أم الجامعات الأردنية.",
                        "website": "https://ju.edu.jo",
                        "faculties": ["كلية الطب", "كلية الهندسة"],
                        "departments": [
                            {"name": "الطب", "fees": 8000, "duration": 6},
                            {"name": "الهندسة الكهربائية", "fees": 4000, "duration": 5}
                        ],
                        "living_costs": {"food": 300, "transport": 100, "total": 600},
                        "dormitory": {"cost": 250, "room_type": "Shared"}
                    }
                ]
            }
        ]
    },
    {
        "name": "قطر", "code": "QA",
        "cities": [
            {
                "name": "الدوحة",
                "universities": [
                    {
                        "name": "جامعة قطر",
                        "description": "الجامعة الوطنية الرئيسية في قطر.",
                        "website": "https://qu.edu.qa",
                        "faculties": ["كلية الهندسة", "كلية الإدارة والاقتصاد"],
                        "departments": [
                            {"name": "هندسة الحاسب", "fees": 12000, "duration": 4},
                            {"name": "المحاسبة", "fees": 10000, "duration": 4}
                        ],
                        "living_costs": {"food": 500, "transport": 200, "total": 1200},
                        "dormitory": {"cost": 500, "room_type": "Single"}
                    }
                ]
            }
        ]
    },
    {
        "name": "الكويت", "code": "KW",
        "cities": [
            {
                "name": "الكويت",
                "universities": [
                    {
                        "name": "جامعة الكويت",
                        "description": "الجامعة الحكومية الرائدة.",
                        "website": "https://ku.edu.kw",
                        "faculties": ["كلية الهندسة والبترول", "كلية العلوم الإدارية"],
                        "departments": [
                            {"name": "هندسة البترول", "fees": 0, "duration": 5},
                            {"name": "إدارة الأعمال", "fees": 0, "duration": 4}
                        ],
                        "living_costs": {"food": 400, "transport": 150, "total": 900},
                        "dormitory": {"cost": 0, "room_type": "Single"}
                    }
                ]
            }
        ]
    },
    {
        "name": "البحرين", "code": "BH",
        "cities": [
            {
                "name": "الصخير",
                "universities": [
                    {
                        "name": "جامعة البحرين",
                        "description": "أكبر جامعة حكومية في البحرين.",
                        "website": "https://uob.edu.bh",
                        "faculties": ["كلية تقنية المعلومات", "كلية الهندسة"],
                        "departments": [
                            {"name": "علوم الحاسوب", "fees": 2000, "duration": 4},
                            {"name": "الهندسة الكيميائية", "fees": 2500, "duration": 4}
                        ],
                        "living_costs": {"food": 350, "transport": 100, "total": 800},
                        "dormitory": {"cost": 200, "room_type": "Shared"}
                    }
                ]
            }
        ]
    },
    {
        "name": "عمان", "code": "OM",
        "cities": [
            {
                "name": "مسقط",
                "universities": [
                    {
                        "name": "جامعة السلطان قابوس",
                        "description": "الجامعة الحكومية المرموقة في عمان.",
                        "website": "https://squ.edu.om",
                        "faculties": ["كلية الهندسة", "كلية الطب والعلوم الصحية"],
                        "departments": [
                            {"name": "الهندسة الميكانيكية", "fees": 0, "duration": 5},
                            {"name": "الطب البشري", "fees": 0, "duration": 7}
                        ],
                        "living_costs": {"food": 300, "transport": 100, "total": 700},
                        "dormitory": {"cost": 0, "room_type": "Single"}
                    }
                ]
            }
        ]
    },
    {
        "name": "العراق", "code": "IQ",
        "cities": [
            {
                "name": "بغداد",
                "universities": [
                    {
                        "name": "جامعة بغداد",
                        "description": "أكبر وأقدم جامعة في العراق.",
                        "website": "https://uobaghdad.edu.iq",
                        "faculties": ["كلية الطب", "كلية الهندسة"],
                        "departments": [
                            {"name": "الطب العام", "fees": 1500, "duration": 6},
                            {"name": "الهندسة المدنية", "fees": 1000, "duration": 5}
                        ],
                        "living_costs": {"food": 250, "transport": 100, "total": 500},
                        "dormitory": {"cost": 100, "room_type": "Shared"}
                    }
                ]
            }
        ]
    },
    {
        "name": "لبنان", "code": "LB",
        "cities": [
            {
                "name": "بيروت",
                "universities": [
                    {
                        "name": "الجامعة الأمريكية في بيروت",
                        "description": "من أرقى الجامعات الخاصة في المنطقة.",
                        "website": "https://aub.edu.lb",
                        "faculties": ["كلية الفنون والعلوم", "كلية الهندسة والعمارة"],
                        "departments": [
                            {"name": "علوم الحاسب", "fees": 18000, "duration": 4},
                            {"name": "الهندسة الكهربائية", "fees": 22000, "duration": 4}
                        ],
                        "living_costs": {"food": 400, "transport": 150, "total": 900},
                        "dormitory": {"cost": 600, "room_type": "Single/Shared"}
                    }
                ]
            }
        ]
    },
    {
        "name": "سوريا", "code": "SY",
        "cities": [
            {
                "name": "دمشق",
                "universities": [
                    {
                        "name": "جامعة دمشق",
                        "description": "أعرق جامعة في سوريا.",
                        "website": "https://damascusuniversity.edu.sy",
                        "faculties": ["كلية الطب", "كلية الآداب"],
                        "departments": [
                            {"name": "الطب البشري", "fees": 500, "duration": 6},
                            {"name": "اللغة العربية", "fees": 200, "duration": 4}
                        ],
                        "living_costs": {"food": 150, "transport": 50, "total": 300},
                        "dormitory": {"cost": 30, "room_type": "Shared"}
                    }
                ]
            }
        ]
    },
    {
        "name": "فلسطين", "code": "PS",
        "cities": [
            {
                "name": "بيرزيت",
                "universities": [
                    {
                        "name": "جامعة بيرزيت",
                        "description": "جامعة وطنية فلسطينية متميزة.",
                        "website": "https://birzeit.edu",
                        "faculties": ["كلية الهندسة والتكنولوجيا", "كلية الأعمال والاقتصاد"],
                        "departments": [
                            {"name": "هندسة الأنظمة الحاسوبية", "fees": 3000, "duration": 5},
                            {"name": "إدارة الأعمال", "fees": 2500, "duration": 4}
                        ],
                        "living_costs": {"food": 300, "transport": 100, "total": 600},
                        "dormitory": {"cost": 200, "room_type": "Shared"}
                    }
                ]
            }
        ]
    },
    {
        "name": "تونس", "code": "TN",
        "cities": [
            {
                "name": "تونس",
                "universities": [
                    {
                        "name": "جامعة تونس المنار",
                        "description": "أكبر قطب جامعي في تونس.",
                        "website": "https://utm.rnu.tn",
                        "faculties": ["كلية الطب", "كلية الحقوق والعلوم السياسية"],
                        "departments": [
                            {"name": "الطب", "fees": 1000, "duration": 6},
                            {"name": "الحقوق", "fees": 500, "duration": 4}
                        ],
                        "living_costs": {"food": 200, "transport": 50, "total": 400},
                        "dormitory": {"cost": 50, "room_type": "Shared"}
                    }
                ]
            }
        ]
    },
    {
        "name": "الجزائر", "code": "DZ",
        "cities": [
            {
                "name": "الجزائر العاصمة",
                "universities": [
                    {
                        "name": "جامعة هواري بومدين للعلوم والتكنولوجيا",
                        "description": "رائدة العلوم والتكنولوجيا في الجزائر.",
                        "website": "https://usthb.dz",
                        "faculties": ["كلية الإلكترونيك والمعلوماتية", "كلية الهندسة الميكانيكية"],
                        "departments": [
                            {"name": "هندسة الحاسوب", "fees": 100, "duration": 5},
                            {"name": "الهندسة الميكانيكية", "fees": 100, "duration": 5}
                        ],
                        "living_costs": {"food": 150, "transport": 30, "total": 300},
                        "dormitory": {"cost": 20, "room_type": "Shared"}
                    }
                ]
            }
        ]
    },
    {
        "name": "المغرب", "code": "MA",
        "cities": [
            {
                "name": "الرباط",
                "universities": [
                    {
                        "name": "جامعة محمد الخامس",
                        "description": "أول جامعة حديثة في المغرب.",
                        "website": "https://um5.ac.ma",
                        "faculties": ["كلية الطب والصيدلة", "كلية العلوم"],
                        "departments": [
                            {"name": "الطب", "fees": 500, "duration": 6},
                            {"name": "الفيزياء", "fees": 100, "duration": 4}
                        ],
                        "living_costs": {"food": 250, "transport": 50, "total": 500},
                        "dormitory": {"cost": 100, "room_type": "Shared"}
                    }
                ]
            }
        ]
    },
    {
        "name": "ليبيا", "code": "LY",
        "cities": [
            {
                "name": "طرابلس",
                "universities": [
                    {
                        "name": "جامعة طرابلس",
                        "description": "أكبر جامعة في ليبيا.",
                        "website": "https://uot.edu.ly",
                        "faculties": ["كلية الطب البشري", "كلية الهندسة"],
                        "departments": [
                            {"name": "الطب البشري", "fees": 300, "duration": 6},
                            {"name": "الهندسة المدنية", "fees": 200, "duration": 5}
                        ],
                        "living_costs": {"food": 200, "transport": 50, "total": 400},
                        "dormitory": {"cost": 50, "room_type": "Shared"}
                    }
                ]
            }
        ]
    },
    {
        "name": "السودان", "code": "SD",
        "cities": [
            {
                "name": "الخرطوم",
                "universities": [
                    {
                        "name": "جامعة الخرطوم",
                        "description": "من أعرق الجامعات في أفريقيا والوطن العربي.",
                        "website": "https://uofk.edu",
                        "faculties": ["كلية الطب", "كلية الهندسة"],
                        "departments": [
                            {"name": "الطب", "fees": 1000, "duration": 6},
                            {"name": "الهندسة المعمارية", "fees": 800, "duration": 5}
                        ],
                        "living_costs": {"food": 150, "transport": 50, "total": 350},
                        "dormitory": {"cost": 50, "room_type": "Shared"}
                    }
                ]
            }
        ]
    },
    {
        "name": "موريتانيا", "code": "MR",
        "cities": [
            {
                "name": "نواكشوط",
                "universities": [
                    {
                        "name": "جامعة نواكشوط العصرية",
                        "description": "الجامعة الرئيسية في موريتانيا.",
                        "website": "https://una.mr",
                        "faculties": ["كلية العلوم والتقنيات", "كلية الطب"],
                        "departments": [
                            {"name": "الرياضيات والمعلوماتية", "fees": 200, "duration": 4},
                            {"name": "الطب", "fees": 500, "duration": 6}
                        ],
                        "living_costs": {"food": 150, "transport": 40, "total": 300},
                        "dormitory": {"cost": 40, "room_type": "Shared"}
                    }
                ]
            }
        ]
    },
    {
        "name": "جيبوتي", "code": "DJ",
        "cities": [
            {
                "name": "جيبوتي",
                "universities": [
                    {
                        "name": "جامعة جيبوتي",
                        "description": "الجامعة الوطنية الوحيدة في جيبوتي.",
                        "website": "https://univ.edu.dj",
                        "faculties": ["كلية الهندسة", "كلية الطب"],
                        "departments": [
                            {"name": "تقنية المعلومات", "fees": 1000, "duration": 4},
                            {"name": "الطب", "fees": 1500, "duration": 6}
                        ],
                        "living_costs": {"food": 250, "transport": 60, "total": 500},
                        "dormitory": {"cost": 150, "room_type": "Shared"}
                    }
                ]
            }
        ]
    },
    {
        "name": "الصومال", "code": "SO",
        "cities": [
            {
                "name": "مقديشو",
                "universities": [
                    {
                        "name": "جامعة مقديشو",
                        "description": "جامعة رائدة غير حكومية.",
                        "website": "https://mogadishuuniversity.com",
                        "faculties": ["كلية الهندسة", "كلية الطب"],
                        "departments": [
                            {"name": "هندسة الحاسوب", "fees": 800, "duration": 4},
                            {"name": "الطب العام", "fees": 1200, "duration": 6}
                        ],
                        "living_costs": {"food": 150, "transport": 40, "total": 350},
                        "dormitory": {"cost": 80, "room_type": "Shared"}
                    }
                ]
            }
        ]
    },
    {
        "name": "جزر القمر", "code": "KM",
        "cities": [
            {
                "name": "موروني",
                "universities": [
                    {
                        "name": "جامعة جزر القمر",
                        "description": "الجامعة الوطنية لجزر القمر.",
                        "website": "https://univ-comores.km",
                        "faculties": ["كلية العلوم والتقنيات", "كلية الآداب"],
                        "departments": [
                            {"name": "العلوم الطبيعية", "fees": 300, "duration": 4},
                            {"name": "الدراسات العربية", "fees": 200, "duration": 4}
                        ],
                        "living_costs": {"food": 200, "transport": 50, "total": 400},
                        "dormitory": {"cost": 50, "room_type": "Shared"}
                    }
                ]
            }
        ]
    }
]
