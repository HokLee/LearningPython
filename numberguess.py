import random
secret = random.randint(1,99)
print(secret)
n=6
guess=0
print('please enter a number,you hava '+str(n)+' chances')
#注意要给guess做类型转换，否则每次判断都为false，即使猜对也不会停止循环
while(int(guess)!=secret and n>0):
    guess = input("what's your guess?")
    if int(guess) <secret:
        print('too low!')
    elif(int(guess)>secret):
        print('too high')
    n = n - 1
    if(n<=0):
        print('out of chances')

if(int(guess)==secret):
    print('you are right!')
