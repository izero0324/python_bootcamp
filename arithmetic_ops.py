'''
write a program in which it:
1. ask for the number of students
2. knows there should be four students per team
3. responds to you with the number of resulting teams
'''
print('Please input number of students :')
std_num = input()
teams = int(int(std_num) / 4)
print('There will be %d teams.' %teams)