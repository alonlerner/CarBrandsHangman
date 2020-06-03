
import random
print("CAR BRANDS GAME")
for x in range(15):
    print('-',end='')
print()
f=open('carBrandsList.txt','r')
brands=f.readlines()
word=random.choice(brands)
word=word[:len(word)-1].upper()
#tries=input('PLEASE ENTER THE NUMBER OF GUESSES ('+str(len(word))+'-26): ')
#while not tries.isnumeric() or int(tries)<len(word) or int(tries)>26:
#    print('NUMBER OF GUESSES IS ILLEGAL')
#    tries=input('PLEASE ENTER THE NUMBER OF GUESSES: ')
#tries=int(tries)
tries=6
tl=[' ']
w=False
while tries!=0 and w==False:
    print()
    print('THE CAR BRAND: ',end='')
    for letter in word:
        if letter in tl:
            print(letter,end='')
        else:
            print('*',end='')
    print()
    print('NUMBERS OF MISSED GUESSES LEFT: '+str(tries))
    print('MISSED GUESSES: ', end='')
    for letter in tl:
        if letter not in word:
            print(letter,end=' ')
    print()
    guess=input('PLEASE ENTER THE NEXT GUESS: ')
    guess=guess.upper()
    while guess in tl or not len(guess)==1 or not guess.isalpha():
        if guess in tl:
            print('YOU HAVE ALREADY GUESSED ' + guess)
        if not guess.isalpha():
            print('ILLEGAL CHARACTER')
        if not len(guess)==1:
            print('ILLEGAL NUMBER OF CHARACTERS')
        guess=input('PLEASE ENTER THE NEXT GUESS: ').upper()
    tl.append(guess)
    w=True
    if len(guess)==1:
        for letter in word:
            if letter not in tl:
                w=False
                break
    if not guess in word:
        tries-=1
print()
if w==True:
    print('YOU WON!!! THE CAR BRAND IS '+word)
else:
    print('YOU LOST!!! THE CAR BRAND IS '+word)
