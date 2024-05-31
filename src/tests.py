import unittest
from io import StringIO
from XML import Xml
src = StringIO("<User_ID>123</User_ID>")
xml = Xml (src)


class Test_srxml(unittest.TestCase):
    def test_tag_search(self):
        self.assertTrue(xml.search("User_ID","123"))
        self.assertFalse(xml.search("User_ID2", "123"))
    def test_value_search(self):
        self.assertTrue(xml.search("User_ID", "123"))
        self.assertFalse(xml.search("User_ID", "1523"))

    def test_parse(self):
        testxml =  "<User_ID>123</User_ID>"
        srcfile = StringIO(testxml)
        xml = Xml(srcfile)
        xml.replace("User_ID","23",write=False)
        result = xml.tostring()
        self.assertNotEqual (srcfile.readline(),testxml)
        self.assertEqual(result,"<User_ID>23</User_ID>")
if __name__ == '__main__':
    unittest.main()
