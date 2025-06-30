from random import choice
"""This project demonstrates how to make random lottery"""
lottery_list = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 0, 'a', 'b', 'c','d']

print("The winning lottery number is:")
winner = [choice(list) for _ in range(4)]
print(winner)