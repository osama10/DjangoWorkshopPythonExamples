# **********              Functions             **************
# Key words : 'def'
# Examples below


def add_number(num1, num2):
    cal = num1 + num2
    return cal


result = add_number(10, 15)
print(result)


def sub_number(num1, num2):
    return num1 - num2


result = sub_number(10, 15)
print(result)


def sum(num1, num2, num3):
    return num1 + num2 + num3

args = (1, 2, 3)  # usually a tuple, always an iterable[1]
# The *args argument is called the "variable positional parameter"
print(sum(*args))   # -> sum(1, 2, 3)

# **kwargs is the "variable keyword parameter"

kwargs = {"num1": 1, "num2": 2, "num3": 3}  # usually a dict, always a mapping*

print(sum(**kwargs)) # -> sum(1, 2, 3)