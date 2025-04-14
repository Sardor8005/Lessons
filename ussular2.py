a='sardor'#str()-sozga aylantirish
b=5#int()
c=True#bool()

#bool() ichiga str tashalinsa va uni ichida soz bolsa True qaytaradi qolgan payti False

bool('sardor')#True
bool(' ')#Ture
bool('')#False

#bool()ICHIGA0 tashlanilsa bu False boladi qolgan holatda True

bool(5)#True
bool(-5)#True
bool(0)#False

#str() ichiga boolian tashalinsa usoz holatida chiqadi "True"va "False"

str(True)#"True"
str(False)#"False"

bool(str(False))#True

# str()ichiga int berlisa ula soz sifatida qaytadi 
 
str(5)#"5"
str(-5)#"-5"
str(0)#"0"

#Operatorlari

#str uchun+ va *, f'{}
'sardor'+'salom' #sardor salom
a='salom'
'Javohir'+a##sardor salom
f'sardor{a}'#sardor salom
'sardor'* 3#sardor sardor sardor

#int operatorlari+ -* % ** //

5+4#9
5-4#1
5*4#20
5%4#1 qoldigin chiqarib beradi
16%5#1
5**4#5*5*5*5 625
5//4#1 butunini chqarib beradi yani qoldiq siz
16//5#3


bool(int(str(0)))#False

#kop malumotlar saqlash uchun list va dict ishlatilinadi

d=[1,True,"sardor"]#list yaratish
d[0]#javob:1 listni birinchi elementini olish uchun 0,ikinchi elementini olish uchun1 qoyiladi
[1,2]#list
e={'number':1,'Boolean':True,'nemeis':'sardor'}#dict yaratish yaratilinvotganda{key:value}
e['number']

