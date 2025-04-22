#def times(x,y):
#    return x * y
#print(times("Sardor",3))
#print(times(3.14,4))
#def kesishmalar(soz1,soz2):
#    res=[]
#    for x in soz1:
#        if x in soz2:
#            res.append(x)
#    return res

#print(kesishmalar("Sardor","Javoxir"))
#def hello():
#    x=5
#    print(x)#5
#print(x)#error
#x=5
#def hello():
#    print(x)#5
#print(x)#5
#def hello():
#    x=5
#    def inner():
#        x=4
#        print(x)#4
#    print(x)#5
#print(x)#error
#x=5
# def hello():
#    global x 
#    x=4#4
#    print(x)
#hello()
#print(x)#4
#x=5
#def hello():
#    x=3
#    def inner():
#        nonlocal x
#        x=2
#    inner()
#    print(x)
#hello()
#print(x)
#def Sayhi(name):
#    print('salom'+name)

#Sayhi("sardor")

#x=input('boyi')
#y=input('eni')
#def kvadrat(x,y):
#    return x+x+y+y

#print(kvadrat(2,5))
#print(kvadrat(4,8))


#def son(x):
#    x = int(x)
#    if x%2:
#        print("Bu son toq son")
#    else:
#        print("Bu son jub son")

#son(input("Soni kiriting"))
x=(input('x:'))
y=(input('y:'))
h=(input('h:'))
def son(x,y,h):

    if x>=y and x>=h:
        print('x 5kata')
    elif y>=x and y>=h:
        print(' y kata') 
    elif h>=x and h>y:  
        print('h kata')
    else:
        print('teng')

son(5,6,7)
