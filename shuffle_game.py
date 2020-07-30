name = 'Nathan'
print(f'My Name is {name} !!')

#importing shuffle method from random library.
from random import shuffle
mylist = [' ','O',' ']

# This fuction will just use the shuffle method to shuffle the items in mylist.

def shuffle_list(mylist):
    shuffle(mylist)
    return(mylist)
result = shuffle_list(mylist)
#print(result)

#this function is to take the user input as an index number which will be later compared with the position of 'O' in the list.

def player_guess():

    guess = ' '
    while guess not in ['0','1','2']:
        guess = input('Please enter the number 0, 1 or 2 \n')
    return int(guess)

#this function will just check if the entered number is a place where 'O' is in the list currently.

def check(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
        print(mylist)
    else:
        print('Wrong Guess')
        print(mylist)

#functions called in sequence, so called how functions interacting with each other.
shuffeling = shuffle_list(mylist)
guess = player_guess()
check_guess = check(mylist,guess)
