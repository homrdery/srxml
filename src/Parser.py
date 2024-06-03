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


    def prepare(self):
        stag = "User_ID"
        sval = self.args[0]

        if self.options.search:
            if self.options.user_id_search:
                files = self.args[1:]
            else:
                stag = self.args[0]
                sval = self.args[1]
                files = self.args[2:]

            return stag, sval, files
        else:
            if self.options.user_id_search:
                rtag = self.args[1]
                rval = self.args[2]
                files = self.args[3:]
            else:
                stag = self.args[0]
                sval = self.args[1]
                rtag = self.args[2]
                rval = self.args[3]
                files = self.args[4:]
            return stag, sval, rtag, rval, files
