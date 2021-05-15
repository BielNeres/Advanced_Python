from string import Template
import itertools

def concat_str_bytes():
    # STRINGS AND BYTES 
    __bytes = bytes([0x41, 0x42, 0x43, 0x44])
    __string = " This is a String"

    # CONCAT STRING & BYTES - ENCODE OR DECODE
    print(
        "String: " + __bytes.decode('utf-8') + __string + "\nBytes: ",
        __bytes + __string.encode('utf-32')
    )

def templates():
    response = "anything"

    #USING FORMAT 
    __string = "This is {0}".format(
        response
    )

    # USING TEMPLATE IMPORT
    __template = Template("This is ${thing}").substitute(
        thing = response
    )

    print(__string,"\n" + __template)

def utilities():
    __list = [0,1,2,3,4]

    #USING ANY AND ALL IN A LIST - ANY IS TRUE IF ANY ELEMENT IS TRUE / ALL IS TRUE IF ALL ELEMENTS ARE TRUE
    print(any(__list),"/",all(__list))
    #MIN && MAX && SUM IN A LIST
    print("Min:", min(__list), "\nMax:", max(__list), "\nSum:", sum(__list))

def iterators(method):
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    days_br = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]

    if method == "iterator":
        # ITER - CREATE A ITERATOR IN A LIST
        for day in iter(days):
            print(day)
    elif method == "range":
        # RANGE - YOU CAN USE MORE ARGS IN RANGE METHOD LIKE -1
        for day in range(len(days)):
            print(day, days[day])
    elif method == "enumerate":
        #ENUMARATE - LESS QNT OF CODE && GIVE A COUNT
        for i, day in enumerate(days):
            print(i, day)
    elif method == "zip":
        #ZIP - CONCAT LISTS
        for day in zip(days, days_br):
            print(day)
    elif method == "match":
        # MATCHING ITERATORS
        for i, day in enumerate(zip(days, days_br)):
            print(i, day[0], "=", day[1])

def transforms():
    def odd(x):
        if x % 2 == 0:
            return False
        else:
            return True
    
    def lower(x):
        if x.isupper():
            return False
        else:
            return True
    
    def quadratic(x):
        return x**2
    
    def verify(x):
        if x >= 90:
            return "A"
        elif (x >= 80 and x < 90):
            return "B"
        elif (x >= 70 and x < 80):
            return "C"
        elif (x >= 60 and x < 70):
            return "D"
        else:
            return "F"

    numbers = (1, 5, 8, 6, 255, 33, 98, 475)
    grades = (60, 20, 80, 40, 10, 100, 96)
    letters = "abcDEfgHIjKLMnrsp"

    # FILTER - FILTER IN A LIST
    # CAT UNIQUE NUMBERS IN A LIST
    unique = list(filter(odd, numbers))
    print(unique)

    # LOWERCASE STRINGS
    lowercase = list(filter(lower, letters))
    print(lowercase)

    # MAP - CREATE A NEW SEQUENCE
    quadrate = list(map(quadratic, numbers))
    print(quadrate)

    #USING SORTED E MAP
    grade = sorted(grades)
    print(list(map(verify, grade)))

def iterators():
    def condition(x):
        return x < 40

    # CYCLE 
    __list = ["Gabriel", "Lucas", "John", "Hosé"]
    cycle = itertools.cycle(__list)
    print(next(cycle), next(cycle), next(cycle), next(cycle), next(cycle))

    # COUNT
    __count = itertools.count(100, 10)
    print(next(__count), next(__count), next(__count))

    # ACUMULATE - IT'S POSSIBLE USE PARAMETERS TO CHANGE THE LIST LIKE MAX
    numbers = [10, 20, 30, 60, 50, 40]
    __accumulate = itertools.accumulate(numbers)
    print(list(__accumulate))

    # CHAIN - CONNECT LISTS
    __chain = itertools.chain("ABCD", "1234")
    print(list(__chain))

    # DROPWHILE & TAKEWHILE - RETURN VALUES UNTIL A CONDITION
    print(list(itertools.dropwhile(condition, numbers)))
    print(list(itertools.takewhile(condition, numbers)))
