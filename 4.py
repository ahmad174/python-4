"""1"""
o=lambda x=1,y=2,z=3:x+y+z
print(o())
print(o(10))
print(o(10,20))

print("\n\n")





"""2"""
import functools
def myfunction(num):
    return(reduce(lambda a,b:a*b,num ))
numbers = [1, 2, 3, 4, 5]
print(myfunction(numbers))






"""3"""
x=(lambda x,y:x*y)(5,3)
print(x)








"""4"""
g=list(filter(lambda x:x<0 , range(-5,5) ))
print(g)





"""5"""
x = lambda a,b,c :a+b+c
print(x(5,6,2))



"""6"""
x=("Joey","Monica","Ross")
y=("Chandler","Pheobe")
z=("David","Rachel","Courteny")
result = list(zip(x,y,z))
print(result)


"""7"""
coin=('Bitcoin','Ether','Ripple','Litecoin')
code=('BTC','ETH','XRP','LTC')
d= dict(zip(coin,code))
print(d)




"""8"""
#function that filters vowels
def fun(variable):
    letters = ['a','e','i','o','u']
    if(variable in letters):
        return True
    else:
        return False
sequence = ['g','j','e','j','k','o','p','r']
filtered = list(filter(fun,sequence))
print(filtered)

"""9"""
x=list(map(int,input("Enter a multiple value:").split()))
print("List of students:",x)







"""10"""
def newfunc(a):
    return (a*a)
x=list(map(newfunc,(1,2,3,4)))
print(x)







"""11"""
def func(a,b):
    return(a+b)
a= list(map(func,[2,4,5],[1,2,3,4]))
print(x)






"""12"""
c = map(lambda x:x+x ,filter(lambda x:(x>=3),(1,2,3,4)))
print(list(c))







"""13"""
c = filter(lambda x:(x>3),map(lambda x:x+x,(1,2,3,4) ))
print(list(c))








"""14"""
import functools
lis = [ 8,5,-9,-2,1,3, 5, 6, 2, ]
print (functools.reduce(lambda a,b : a if a < b else b,lis)) 





"""15"""
numbers=[1,2,3]
letters=['a','b','c']
results = list(zip( numbers , letters ))
print(results)
