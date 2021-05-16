import collections
import string

## SIMPLE COLLECTIONS
# LIST IS MUTABLE
__list = ['a', 'b']
# TUPLE IS IMMUTABLE
_tuple = ('a', 'b')
# A SEQUENCE DISTINCT VALUES
__set = {'a', 'b'}
# KEYS && VALUES 
__dictionary = {'a': 'b', 'c': 'd'}


## ADVANCED COLLECTIONS
# NAMEDTUPLE - USE TO DETERMINE A "KEY"(NAME) TO A TUPLE - LIKE COORDENATES
### coordinates = collections.namedtuple("point", "x y")   

# DEFAULTDIC
def defaultdic_func():
    fruits = ['apple', 'pear', 'banana', 'strawberry',
              'apple', 'grape', 'banana', 'pineapple']

    # DEFAULT TO CREATE A COUNT EACH ELEMENT - CAN USE LAMBDA TO RETURN A DIFFERENT VALUE
    count_fruits = collections.defaultdict(lambda: 100)

    for fruit in fruits:
        count_fruits[fruit] += 1

    for (c, v) in count_fruits.items():
        print(c + ": " + str(v))

# COUNTER
def counter_func():
    a_class = ["Barbara", "João", "Carlos", "Gustavo"]
    b_class = ["Hélio", "Claudio", "Junior", "Gabriel", "Samuel", "Leticia"]

    # COUNTER IN A LIST
    a = Counter(a_class)
    b = Counter(b_class)

    # CAT SOME VALUES 
    print(a["João"], sum(a.values()))
    print(b["Gabriel"], sum(b.values()))

    # UPDATE - UPDATE A VALUES IN A LIST
    a.update(b_class)
    print(sum(a.values()))

    # MOST COMMOM - USERS MOST COMMOM IN A LIST
    print(a.most_commom())

    #SUBTRACT - SUBSTRACT VALUES IN A LIST
    a.subtract(b_class)
    print(a.most_commom())

    # INTERSECTION LISTS
    print(a & b)

#ORDER DICT
def order_dict_func():
    soccer_teams = [("PSG", (18,20)), ("Barcelona", (30, 60)), ("Liverpool", (15, 40))
                    ("Corinthians", (100, 0)), ("Santos", (0, 50)), ("Manchester City", (45, 60))]

    # ORDER BY WIN QNT
    order_teams = sorted(soccer_teams, key=lambda t: t[1][0], reverse=True)

    # CREATE A ORDER DICT IN A LIST
    teams = OrderedDict(order_teams)
    print(teams)

    #POPITEM - REMOVE OR CAT (TRUE, FALSE) TOP ELEMENT DICT
    times.popitem(False)

#DEQUE 
def deque_func():
    lower_letters = collections.deque(string.ascii_lowercase)

    #USING LEN
    print(len(lower_letters))

    # ITERATE LIST
    for letter in lower_letters:
        print(letter.upper(), end='')
    
    # HANDLE ITENS 
    # POP LAST ELEMENT
    lower_letters.pop()
    # POP FIRST ELEMENT
    lower_letters.popleft()
    # ADD LAST ELEMENT
    lower_letters.append(2)
    # ADD FIRST ELEMENT
    lower_letters.appendleft(5)

    print(lower_letters)

    # ROTATION DEQUE
    lower_letters.rotate(10)
    print(lower_letters)




