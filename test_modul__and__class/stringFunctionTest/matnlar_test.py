import unittest
from matnlar import titleTekst

class MatnText:
    
    def test_titleText(self):
        self.assertEqual(titleTekst(['akrom','temirov'],['Akrom','Temirov']))
unittest.main()