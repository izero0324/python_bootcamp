'''
You're at a restaurant with some friends and you want to split the bill
Task1:
ask the user how many people he/she wants to split the bill between
save that number into a variable:noOfPeople
Task2:
ask the user what's the bill's cost
save that number into a variable: bill
Task3:
Write a function that returns how much each person should pay
call this function splitBill and give it two parameters, noOfPeople and bill
Task4:
Print the function's return value
'''
def splitBill(noOfPeople, bill):
    return round(float(bill)/int(noOfPeople),3)

noOfPeople = input('Input the number of people to split the bills: ')
bill = input('Input the bill: (£)')
print('£', splitBill(noOfPeople, bill), 'each')