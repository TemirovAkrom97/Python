import unittest
from class2 import Shaxs,Talaba

class ShaxsTest(unittest.TestCase):
    '''shaxs klassini tekshirish uchun test'''
    def setUp(self):
        ism = 'akrom'
        familiya = 'temirov'
        passport = 'FA112299'
        tyil = 2000
        self.shaxs1=Shaxs(ism,familiya,passport,tyil)
        
    def test_create(self):
        # Qiymatlar mavjudligini tekishiramiz
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)
    
    def test_get_age(self):
        self.assertAlmostEqual(self.shaxs1.get_age(2021), 21)
    
unittest.main()