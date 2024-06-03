#!/usr/bin/python
# Утилита для работы с xml файлами
import sys
try:
    # Импорт нужных методов и библиотек, также описание всех опций для OptionParser'a
    from logger import Logger
    from Parser import Parser
    from XML import Xml
    parser = Parser()
    parser.parse_args()

    logger = Logger(parser.options.verbose)
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(5)

try:
    # """Основное тело утилиты"""
    logger.msg_debug(f"Аргументы {parser.args}")
    # if len(parser.args) < 3:
    #     raise Exception(f"Не хватает аргументов, передано {len(parser.args)}, а должно быть не меньше 3")




    if parser.options.search:

        tag, value, filenames = parser.params
        logger.msg_info("Режим поиска")
        logger.msg_debug(f"Ищем {value} в теге {tag} в файлах {filenames}")
    else:

        tag, value, set_tag, set_value, filenames = parser.params

        logger.msg_info("Режим замены")
        logger.msg_debug(f"Ищем значения: {value} в теге {tag} и устанавливаем тег {set_tag} в значение {set_value} в файлах {filenames}")


    # Цикл который парсит файлы и передаёт их в опции поиска или замены
    for filename in filenames:
        logger.msg_info(filename)
        tree = Xml.parse(filename)
        if tree.search(tag, value):
            if parser.options.search:
                print(tree.filename)
            else:
                tree.replace(set_tag, set_value)
    logger.msg_info("утилита отработала")

except Exception as e:
    logger.msg_error(e)
