from random import choice
"""This project demonstrates how to make random lottery"""
lottery_list = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 0, 'a', 'b', 'c','d']

print("The winning lottery number is:")
winner = []
my_ticket = [1, 2, 3, 4]
num = 0
while (winner != my_ticket):
    winner = [choice(lottery_list) for _ in range(4)]
    num += 1


print(winner)
print("You need this to win:")
print(num)