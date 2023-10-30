'''
Create a program that:
A) Asks the user how many pizzas they ordered
B) Asks the user how many slices are there in each pizza
C) Asks the user how many attendees are coming to this event
D) Returns a full english sentence that includes:
    > all the information the user inputted
    > the number of slices per attendee as a float
'''

print('how many pizzas do you order?')
pizza_num = int(input())
print('how many slices are there in each pizza?')
slice_num = int(input())
print('how many attendees are coming to this event?')
attendee = int(input())

print('You are ordering %d pizzas, and each pizza has %d slices. '
    'If you have %d attendees, that is approximately %.2f slices per person' 
    %(pizza_num, slice_num, attendee, (pizza_num * slice_num)/attendee))

