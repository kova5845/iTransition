import sys
import random
from mimesis import Address
from mimesis import Person

if (len(sys.argv)) != 4:
    print("ERROR!")
    raise SystemExit(1)

err = float(sys.argv[3])
err1 = float(sys.argv[3]) * int(sys.argv[1])
err2 = 0;

if sys.argv[2] == 'ru':
    address = Address('ru')
    person = Person('ru')
    count = 0
    porog = random.randint(1, int(1 + 3*err))
    for i in range(0, int(sys.argv[1])):
        count += err
        if count >= porog:
            while (count > 1):
                count -= 1
                err2 += 1;
                print("---------------------")
                porog = random.randint(1,int(1 + 3*err))
        print(i, " ", person.name(), " ", person.telephone('+7 ### ### ## ##'), " ",  address.address())
elif sys.argv[2] == 'en':
    address = Address('en')
    person = Person('en')
    for i in range(0, int(sys.argv[1])):
        print(i, " ", person.name(), " ", person.telephone('+1 ### ### ## ##'), " ", address.address())
elif sys.argv[2] == 'by':
    address = Address('uk')
    person = Person('uk')
    for i in range(0, int(sys.argv[1])):
        print(i, " ", person.name().replace('и', 'i').replace('ї', 'й'),
        " ", person.telephone('+375 ## ### ## ##'), " ",
        address.address().replace('и', 'i').replace('ї', 'й'))
else:
    print("ERROR!")
    raise SystemExit(1)

print (err2, " ", err1)


