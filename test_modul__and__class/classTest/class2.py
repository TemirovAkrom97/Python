
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
      
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar=[]
        
    '''dunder metodlar'''
    
    def __repr__(self):
        '''talaba ism familiyasini tugridan tugri print orqali chiqaruvchi yoki str'''
        return f'{self.ism} {self.familiya}'
    
    def __lt__(self,ikkinchi):
        return self.bosqich<ikkinchi.bosqich
    
    def __eq__(self, ikkinchi):
        return self.bosqich==ikkinchi.bosqich
    '''/dunder metodlar'''
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
      """Talaba haqida ma'lumot"""
      info = f"{self.ism} {self.familiya}. "
      info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
      return info
  
    def fanga_yozil(self,fan):
      '''fan klasidan kelgan obektni fanlar ruyhatiga qushuvchi funksiya'''
      self.fanlar.append(fan)

    def remove_fan(self,fan):
      '''talabaning fanlar ruyhatidan berilgan fanni uchirib tashlovchi funksiya'''
      for fan1 in self.fanlar:
          if fan == fan1.get_fanNomi():
              self.fanlar.remove(fan1)
              return f'Sizning fanlar ruyhatingizdan {fan} uchirildi!'
          else:
              return f'Siz bu fanga yozilmagansiz'
    def get_fanlar(self):
        return [fan.get_fanNomi() for fan in self.fanlar]
      
class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil
class Fan:
    """Fanlarni saqlash uchun class"""
    def __init__(self,nomi):
        self.nomi=nomi
    def get_fanNomi(self):
        
        return f'{self.nomi}'
    
# talaba_manzil = Manzil(12,'Olmazor',"Bog'bon","Samarqand")
# talaba1 = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil)
# talaba2 = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil)
# fan1= Fan('matematika')
# fan2= Fan('Ona tili')
# talaba1.fanga_yozil(fan1)
# talaba2.fanga_yozil(fan2)

