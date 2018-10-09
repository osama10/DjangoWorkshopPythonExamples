import random

# **********              Looping             ***************
# Key words : 'for', 'while'
# Examples below

for x in range(0, 10):
    print(x)

print('\n')

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
for item in grocery_list:
    print(item)


random_num = random.randrange(0,100)
while random_num is not 15:
    print(random_num)
    random_num = random.randrange(0,100)

i = 0
while i <= 20:
    if i % 2 == 0:
        print(i)
    elif i == 9:
        break
    else:
        i += 1
        continue
    i += 1