def args_function():
    # '*' allow that function receive variables parameters
    def add(*args):
        return sum(args)

    __list = [15, 60, 80 ,11]
    print(add(*__list))

def lambda_function():
    def celsius_to_fahrenheit(temp):
        return (temp * 9/5) + 32
    
    def fahrenheit_to_celsius(temp):
        return (temp - 32) * 5/9

    celsius_temp = [0, 12, 34, 100]
    farenheit_temp = [32, 65, 100, 212]

    # USING CONVENTIONAL FUNCS
    print(list(map(fahrenheit_to_celsius, farenheit_temp)))
    print(list(map(celsius_to_fahrenheit, celsius_temp)))

    # USING LAMBDA
    print(list(map(lambda t: (t - 32) * 5/9, farenheit_temp)))
    print(list(map(lambda t: (t * 9/5) + 32, celsius_temp)))

def exception_function():
    def critic_function(arg1, arg2, *, __exception=False):
        print(arg1, arg2, __exception)

    #iF NOT PARSE A NAME VARIABLE OCCURS A ERROR SO
    critic_function(1, 2, __exception=True)
