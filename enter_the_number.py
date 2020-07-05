import random

number = random.randint(0,101)
while True:
    answer = input('Enter the number: ')
    if not answer or answer == "exit":
        break
    if not answer.isdigit():
        print('Enter the right number!')
        continue

    user_answer = int(answer)
    if user_answer > number:
        print('Make a number less')
    elif user_answer < number:
        print('Make a bigger number')
    else:
        print("You're right!")
        break
    continue
