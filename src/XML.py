from xml.etree import ElementTree
from io import StringIO


class Xml:
    """
    Класс для работы с XML файлами
    гмккт искать и устанавливать узлы в файле
    """
    @staticmethod
    def parse(filename: str):
        obj = Xml()
        obj.filename = filename
        obj.xml = ElementTree.parse(filename)
        obj.root = obj.xml.getroot()

        return obj

    @staticmethod
    def fromstring(text: str):
        obj = Xml()

        obj.xml = ElementTree.parse(StringIO(text))
        obj.root = obj.xml.getroot()
        return obj
    # def __init__(self, filename=None):
    #     """
    #
    #     :param filename: имя файла или объкт файл с xml
    #     """
    #     self.filename = filename
    #
    #     if filename:
    #         self.xml = ElementTree.parse(filename)
    #         self.root = self.xml.getroot()

    def search(self, tag: str, value: str) -> bool:
        """
        Ищет значение в дереве XML
        :param tag: тег в котором надо найти заднное значение-(value)
        :param value: значеное значение которое надо найти в теге-(tag)
        :return: True если нашел и False если нет
        """
        nodes = self.root.iter(tag)
        for node in nodes:
            if node.text == value:
                return True
        return False

    def replace(self, tag: str, value: str, write: bool = True):
        """
        заменяет значения в теле выбранного теге
        :param write:
        :param tag: тег в котором надо заменить значение-(value)
        :param value: значение тега которое надо вписать в тег-(tag)
        :return:
        """
        nodes = self.root.iter(tag)
        count = 0
        for node in nodes:
            count += 1
            node.text = value
        if count == 0:
            raise Exception(f""" Тега  "{tag}" не существует""")

        if write:
            self.xml.write(self.filename)

    def tostring(self):
        return ElementTree.tostring(self.xml.getroot(), "UTF-8").decode("UTF-8")

