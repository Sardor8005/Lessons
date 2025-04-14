#a=5
#b=3
#result=a**b
#print(result)
#name="sardor"
#age="14"
#print("Salom "+name+" siz "+age+" yoshdasiz ")
#print(f"salom {name}.siz {age} yoshdasiz")
string='salom'
len(string)#5
string[0]#S
string[-1]#m
string[len(string)-1]#m
string='salom'
string[1:3]#al
string[0:3]#sal
string[1:]#alom
string+'akbar'
string[3:6]#om
name=input('siznig ismingiz')
age=input('yoshingiz;')
print('hush kelibsiz:'+name)
print('yoshim:'+age)

#print(string[0]='Z')#eRROR
string='z'+string[1:]
print(string)
