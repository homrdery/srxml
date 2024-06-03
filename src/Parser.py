from optparse import OptionParser


class Parser(OptionParser):
    def __int__(self):
        super().__init__(usage="usage: %prog [options] tag value filename(s)")
        # OptionParser.__init__(self,usage="usage: %prog [options] tag value filename(s)")

    def parse_args(self):

        self.add_option("-v", action="count", dest="verbose", help="verbose", default=False)
        self.add_option("-s", action="store_true", dest="search", help="search for tag minimum 3 args", default=True)
        self.add_option("-r", action="store_false", dest="search", help="replace text in tag body minimum")
        self.add_option("--user", action="store_true", dest="user_id_search", help="search by User_ID_158",
                        default=False)
        self.options, self.args = super().parse_args()

        self.params = self.prepare()

    #функционал опций
    def prepare(self):
        stag = "User_ID" #СПЕЦИАЛЬНОЕ ИМЯ ТЕГа ДЛЯ ОПЦИИ ПОИСКА ПО ID
        sval = self.args[0] #значение тега которое ищем/

        if self.options.search:
            if self.options.user_id_search:
                # опция поиска по ID
                files = self.args[1:]#файлы в которых производится поиск
            else:
                # обычный поиск
                stag = self.args[0]#имя тега в котором ищем значение
                sval = self.args[1]#значение тега которое ищем
                files = self.args[2:]#файлы в которых производится поиск

            return stag, sval, files
        else:
            if self.options.user_id_search:
                #опция замены + опция --user
                rtag = self.args[1]#иимя тега на которое мы заменяем в случае поиска по id
                rval = self.args[2]#значение тега на которое мы заменяем в случае поиска по id
                files = self.args[3:]#файлы в которых производится поиск
            else:
                # опция замены
                stag = self.args[0]#имя тега в котором производится замена
                sval = self.args[1]#первичное значение тега которое в последствии поменяется
                rtag = self.args[2]#иимя тега на которое мы заменяем
                rval = self.args[3]#значение тега на которое мы заменяем
                files = self.args[4:]#файлы в которых производится поиск
            return stag, sval, rtag, rval, files
