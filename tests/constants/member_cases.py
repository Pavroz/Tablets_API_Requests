MEMBER_CREATE_CASES = [
            (None, None, None),
            ("middlename", None, None),
            (None, "subject", None),
            (None, None, "position"),
            ("middlename", "subject", None),
            ("middlename", None, "position"),
            (None, "subject", "position"),
            ("middlename", "subject", "position"),
        ]

MEMBER_PUT_CASES = [
    # 1. Одиночные изменения (5 тестов)
    ("firstname", None, None, None, None),  # только firstname
#     (None, "lastname", None, None, None),  # только lastname
#     (None, None, "middlename", None, None),  # только middlename
#     (None, None, None, "position", None),  # только position
#     (None, None, None, None, "subject"),  # только subject
#
#     # 2. Парные изменения (все комбинации с firstname/lastname)
#     ("firstname", "lastname", None, None, None),  # firstname + lastname
#     ("firstname", None, "middlename", None, None),  # firstname + middlename
#     ("firstname", None, None, "position", None),  # firstname + position
#     ("firstname", None, None, None, "subject"),  # firstname + subject
#     (None, "lastname", "middlename", None, None),  # lastname + middlename
#     (None, "lastname", None, "position", None),  # lastname + position
#     (None, "lastname", None, None, "subject"),  # lastname + subject
#     (None, None, "middlename", "position", None),  # middlename + position
#     (None, None, "middlename", None, "subject"),  # middlename + subject
#     (None, None, None, "position", "subject"),  # position + subject
#
#     # 3. Тройные изменения (ключевые комбинации)
#     ("firstname", "lastname", "middlename", None, None),  # firstname + lastname + middlename
#     ("firstname", "lastname", None, "position", None),  # firstname + lastname + position
#     ("firstname", "lastname", None, None, "subject"),  # firstname + lastname + subject
#     ("firstname", None, "middlename", "position", None),  # firstname + middlename + position
#     ("firstname", None, "middlename", None, "subject"),  # firstname + middlename + subject
#     ("firstname", None, None, "position", "subject"),  # firstname + position + subject
#     (None, "lastname", "middlename", "position", None),  # lastname + middlename + position
#     (None, "lastname", "middlename", None, "subject"),  # lastname + middlename + subject
#     (None, "lastname", None, "position", "subject"),  # lastname + position + subject
#     (None, None, "middlename", "position", "subject"),  # middlename + position + subject
#
#     # 4. Четверные изменения
#     ("firstname", "lastname", "middlename", "position", None),  # все кроме subject
#     ("firstname", "lastname", "middlename", None, "subject"),  # все кроме position
#     ("firstname", "lastname", None, "position", "subject"),  # все кроме middlename
#     ("firstname", None, "middlename", "position", "subject"),  # все кроме lastname
#     (None, "lastname", "middlename", "position", "subject"),  # все кроме firstname
#
#     # 5. Пять полей
#     ("firstname", "lastname", "middlename", "position", "subject"),  # все поля
#
#     # 6. Граничные случаи
#     ("", "", "", "", ""),  # пустые строки
]