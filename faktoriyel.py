def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n-1)
#sayı=4
#print(faktoriyel(sayı))

x="global değişken"

def function():
    x="local değişken"
    print(x)

#function()
#print(x)
    
#Hatalar
    
#print(a)
    
#int('a19') = value error

#print(10/0) syntax error

#print('hello'world)
    
try:
    x=int(input("x giriniz"))
    y=int(input("y giriniz"))
    print(x/y)
except ZeroDivisionError:
    print("sıfıra bölünme hatası")
except ValueError:
    print("x ve y için sayısal değer giriniz")

except Exception as ex:
    print()