spusok_1 = ['name', 354, 'hobby', 'name', 'name']
spusok_2 = ['rikky', 'days', 'cycle']


def func(a):
    for i in a:
        for i in spusok_1:
            i = i
            print(spusok_1.remove(i))
            dictionary = dict(zip(spusok_1, spusok_2))
            print(dictionary)


            return dictionary

f = func(spusok_1)
print(f)
