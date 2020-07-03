# Write a program that prints the integers from 1 to 100. But for multiples of three print "Bruh" instead of the number, and for the multiples of five print "moment". For numbers which are multiples of both three and five print "Bruh moment".

for i in range(1,101):
    if i%3==0 and i%5==0:
        print('Bruh moment')
    elif i%3==0:
        print('Bruh')
    elif i%5==0:
        print('moment')
    else:
        print(i)