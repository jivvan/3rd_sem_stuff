# a = int(input("Enter a = "))
# b = int(input("Enter b = "))

# while True:
#     op = input("Enter operation: (+, -, *, /). q to quit")
#     if op == 'q':
#         break

#     if op == '+':
#         print(f"{a}+{b}={a+b}")
#     elif op == '-':
#         print(f"{a}-{b}={a-b}")
#     elif op == '*':
#         print(f"{a}*{b}={a*b}")
#     elif op == '/':
#         print(f"{a}/{b}={a/b}")

import random

diff = int(input("Enter difficulty: \n1. Easy\n2. Normal\n3. Hard"))
if diff == 1:
    ans = random.randint(0, 100)
elif diff == 2:
    ans = random.randint(0, 1000)
else:
    ans = random.randint(0, 10000)
counter = 0
while True:
    print("Guesses left: "+str(10-counter))
    user_ans = int(input())
    if counter > 8:
        print("Game Over! Answer was - "+str(ans))
        break
    counter += 1
    if user_ans < ans:
        print("too low!")
    elif user_ans > ans:
        print("high!")
    elif user_ans == ans:
        print("You guessed it!")
        break
