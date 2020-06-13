

def find_sum(input1, input2):
    if type(input1) == type(input2):
        return input1 + input2
    else:
        return "Loop is completed!"


result = find_sum(5, 10)
print(result)


def shop(item, price):
    print(item)
    print(price)


shop("Sugar", 50)
shop(price=55, item="Rice")


def default_shop(item, price=55):
    print(item)
    print(price)


default_shop(item="Coconut")
default_shop(item="Coconut", price=101)


def std(name, stand, *marks):
    print(name)
    print(stand)
    print(marks)       # marks is of tuple type

    for x in marks:
        print("Mark is: ", x)


std("Vivek", 11, 55, 66, 88, 99)


def std_enhanced(name, stand, **marks):
    print("Name: ", name)
    print("Class: ", stand)
    print("Marks: ", marks)            # marks will of type dict

    for x, y in marks.items():
        print(x, " Marks: ", y)


std_enhanced("Vivek", 11, English=55, Hindi=66, Maths=77, IT=88)



