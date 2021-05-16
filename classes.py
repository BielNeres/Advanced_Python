from enum import Enum, auto

# ENUM
def enums_func():
    # CANNOT ADD SAME NAMES
    class Fruit(Enum):
        PINEAPPLE = 1
        BANANA = 2
        PEAR = 3
        APPLE = 4
        TOMATO = 5
        ORANGE = auto()
    
    # TYPE AND REPRESENTATION
    print(type(Fruit.APPLE), repr(Fruit.APPLE))

    # NAME AND VALE
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # CAT ORANGE AUTO VALUE
    print(Fruit.ORANGE.value)

    # CAN USE ENUM WITH DICTS ({})
    fruits = dict()
    fruits[Fruit.BANANA] = "Yellow"
    print(fruits[Fruit.BANANA])


