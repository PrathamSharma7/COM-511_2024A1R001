'''
Write a Python program to show that tuple values cannot be changed directly. Convert tuple into list, update it
then change into tuple again
'''
t = (1,2,3,4,5,6)
# t[0] = "Changed"          # [gives error]
l = list(t)
l[0] = 'Changed'
t = tuple(l)
print(t)