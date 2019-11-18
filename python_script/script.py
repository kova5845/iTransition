import sys
import random
import time
from mimesis import Address
from mimesis import Person

def func(line):
    if error_list:
            if i == error_list[0]:
                while(error_list[0] == i):
                    num = random.randint(0, 100)
                    if (num > 10 and num < 90 and len(line) > 2):
                        n = random.randint(0, len(line) - 1)
                        m = random.randint(0, len(line) - 1)
                        k = line[n]
                        line = line[:n] + line[m] + line[n+1:]
                        line = line[:m] + k + line[m+1:]
                    elif (num >= 900):
                        n = random.randint(0, len(line) - 1)
                        line = line[:n] + " " + line[n+1:]
                    elif (num < 0 and len(line) > 2):
                        n = random.randint(0, len(line) - 1)
                        line = line[:n] + line[n+1:]

                    del error_list[0]
                    if(not error_list):
                        break
    return line

if (len(sys.argv)) != 4:
    print("ERROR!")
    raise SystemExit(1)

s_time = time.time()

err = int(float(sys.argv[3]) * int(sys.argv[1]))

error_list = list()
for i in range(0, err):
    error_list.append(random.randint(0, int(sys.argv[1]) - 1))

error_list.sort()
# print(error_list)

if sys.argv[2] == 'ru':
    address = Address('ru')
    person = Person('ru')
    kol = int(sys.argv[1])
    for i in range(0, kol):
        listok = list()
        listok.append(person.last_name() + " ")
        listok.append(person.name() + " ")
        listok.append(person.name() + "ович ")
        listok.append(person.telephone('+7 ### ### ## ##') + " ")
        listok.append(address.address())
        line = "".join(listok)
        line = func(line)
        print(line)
elif sys.argv[2] == 'en':
    address = Address('en')
    person = Person('en')
    for i in range(0, int(sys.argv[1])):
        listok = list()
        listok.append(person.last_name() + " ")
        listok.append(person.name() + " ")
        listok.append(person.name() + " ")
        listok.append(person.telephone('+1 ### ### ## ##') + " ")
        listok.append(address.address())
        line = "".join(listok)
        line = func(line)
        print(line)
elif sys.argv[2] == 'by':
    address = Address('uk')
    person = Person('uk')
    for i in range(0, int(sys.argv[1])):
        listok = list()
        listok.append(person.last_name().replace('и', 'i').replace('ї', 'й').replace('є','э').replace('Ї','I').replace('И','I') + " ")
        listok.append(person.name().replace('и', 'i').replace('ї', 'й').replace('є','э').replace('Ї','I').replace('И','I') + " ")
        listok.append(person.name().replace('и', 'i').replace('ї', 'й').replace('є','э').replace('Ї','I').replace('И','I') + "авiч ")
        listok.append(person.telephone('+375 ## ### ## ##') + " ")
        listok.append(address.address().replace('и', 'i').replace('ї', 'й').replace('є','э').replace('Ї','I').replace('И','I') + " ")
        line = "".join(listok)
        line = func(line)
        print(line)
else:
    print("ERROR!")
    raise SystemExit(1)

# print (err)
# print(time.time() - s_time)



# cd /d d:iTransition\python_script