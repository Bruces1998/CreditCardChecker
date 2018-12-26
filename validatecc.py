'''
This Program Works On Luhn's Algorithm
to identify if the entered card number 
is valid or not.
'''

print("Welcome to The card Validator App!!!!")
num=input('Enter The Card Number:')
oddsum=0
evensum=0

li=list(num)
size=len(li)
lastterm=int(li.pop())
Reversed=li[::-1]
li=li[::-1]
while li!=[]:
    y=int(li.pop())
    y=y*2
    if(y>9):
        y=y-9
    oddsum=oddsum+y
    if(li==[]):
        break
    x=int(li.pop())
    evensum=evensum+x
    
totalsum=evensum+oddsum
print(totalsum)
rem=totalsum%10
if(rem==lastterm):
    print('VALID CREDIT/DEBIT CARD!!!!')
else:
    print('Invalid Card!!!!')
