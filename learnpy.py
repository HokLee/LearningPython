#python3
import urllib.request
import random
import easygui
file = urllib.request.urlopen('http://helloworldbook2.com/data/message.txt')
message = file.read()
print(message)
secret = random.randint(1,99)
guess = 0
tries = 0
easygui.msgbox('please enter a number:')
while guess != secret and tries<6:
    guess = easygui.integerbox('what\'s your guess?')
    if guess<secret:
        easygui.msgbox('too low, you haved used '+str(tries+1)+' chances')
    elif guess>secret:
        easygui.msgbox('too high, you haved used '+str(tries+1)+' chances')
    tries = tries+1
if guess == secret:
    easygui.msgbox('good')
else:
    easygui.msgbox('no more guesses!the number was '+str(secret))



