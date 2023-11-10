LOCATION_VIEW = """
Название: {name}
Тип: {type}
Создан: {created}
{description}
"""

MAP_LOCATION_YANDEX = "https://yandex.ru/maps/?ll={longitude}%2C{latitude}&l=map&z=18"
MAP_LOCATION_GOOGLE = "https://www.google.com/maps/place/{latitude},{longitude}"

LOCATION_TYPE_CREATE_END = """
Вы успешно завершили создание типа локаций: {name}
"""

LOCATION_TYPE_ALREADY_EXISTS_END = """
Такой тип локаций уже существует: {name}
"""