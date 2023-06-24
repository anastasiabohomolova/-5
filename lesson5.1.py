k = ['age', 'salary', 'day']
b = [str(x) for x in  input('Введіть значення через пробіл: ').split()] 


def func(a):
    for i in a:
        n = list(b)
        dicti = dict(zip(k, n))
        print(dicti)
    

 
    return dicti

f = func(b)
print(f)


