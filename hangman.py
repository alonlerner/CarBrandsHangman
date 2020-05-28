import random
print("CAR BRANDS GAME")
for x in range(80):
    print('*',end='')
print()
f=open('car brands list.txt','r')
brands=f.readlines()
word=random.choice(brands)
word=word[:len(word)-1].upper()
tries=input('PLEASE ENTER THE NUMBER OF GUESSES ('+str(len(word))+'-26): ')
while not tries.isnumeric() or int(tries)<len(word) or int(tries)>26:
    print('NUMBER OF GUESSES IS ILLEGAL')
    tries=input('PLEASE ENTER THE NUMBER OF GUESSES: ')
tries=int(tries)
tl=[' ']
w=False
attempts=0
while tries!=0 and w==False:
    print()
    for letter in word:
        if letter in tl:
            print(letter,end='')
        else:
            print('*',end='')
    print()
    print('NUMBERS OF GUESSES LEFT: '+str(tries))
    print('GUESSES: ', end='')
    for letter in tl:
        print(letter,end=' ')
    print()
    guess=input('PLEASE ENTER THE NEXT GUESS: ')
    guess=guess.upper()
    while guess in tl or len(guess)==0 or not guess.isalpha():
        if guess in tl:
            print('YOU HAVE ALREADY GUESSED ' + guess)
        if not guess.isalpha():
            print('ILLEGAL CHARACTER')
        guess=input('PLEASE ENTER THE NEXT GUESS: ').upper()
    tl.append(guess)
    w=True
    if len(guess)==1:
        for letter in word:
            if letter not in tl:
                w=False
                break
    else:
        if guess!=word:
            w=False
    tries-=1
    attempts+=1
if w==True:
    print('YOU WON!!! THE CAR BRAND IS '+word+'. IT TOOK YOU '+str(attempts)+' ATTEMPTS.')
else:
    print('YOU LOSE!!! THE CAR BRAND IS '+word)
