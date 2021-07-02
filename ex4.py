import random


print('What is your name?')
print('>', end='')
name = input()
print('Hello, {}!'.format(name))

print('Rolling the dice...')
count = 0
for i in range(2):
    num_1 = random.randrange(6)+1
    count += num_1
    print('Die {}:{}'.format(i+1, num_1))

print('Total value: {}'.format(count))

if count >= 7:
    print('{} won!'.format(name))
else:
    print('{} lost!'.format(name))
