def attack(char_name: str, char_class: str) -> str:
    """
    Функция для атаки противника.
    :param char_name: имя персонажа
    :param char_class: класс персонажа
    :return: строку с описанием атаки
    """
    ...


def defence(char_name: str, char_class: str) -> str:
    """
    Функция для блокирования атаки противника.
    :param char_name: имя персонажа
    :param char_class: класс персонажа
    :return: строку с описанием блокирования атаки
    """
    ...


def special(char_name: str, char_class: str) -> str:
    """
    Функция для применения специального умения.
    :param char_name: имя персонажа
    :param char_class: класс персонажа
    :return: строку с описанием применения специального умения
    """
    ...


def start_training(char_name: str, char_class: str) -> str:
    """
    Функция для начала тренировки персонажа.
    :param char_name: имя персонажа
    :param char_class: класс персонажа
    :return: строку с сообщением об окончании тренировки
    """
    ...


def choice_char_class() -> str:
    """
    Функция для выбора класса персонажа.
    :return: строку с названием класса персонажа
    """
    ...


def main() -> None:
    """Основная функция игры."""