# sum = lambda a,b:a+b
# print(sum(2,5))

# map Function
# r = map(func, seq)

def fahrenheit(T):
    return ((float(9)/5)*T +32)
def celsius (T):
    return ((float(5)/9)*(T-32))
temperatures = (36.5, 37, 37.5, 38, 39)

returnFah = list(map(fahrenheit,temperatures))
returnCels = list(map(celsius,temperatures))

print(returnFah)
print(returnCels)

