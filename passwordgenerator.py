import random
nums = '0 1 2 3 4 5 6 7 8 9 '
lower = 'q w e r t y u i o p a s d f g h j k l z x c v b n m'
upper = lower.upper()
spechar = '! @ # $ % ^ & * ( ) _ + - = { } | [ ] \ : " ; \' \, . / < > ?'

numsplit = nums.split()
lowersplit = lower.split()
uppersplit = upper.split()
specharsplit = spechar.split()

ask = ''

while True:
    try:
        while not ask == 'n':
            numput = int(input('How many numbers do you want? '))
            lowput = int(input('How many lowercase letters do you want? '))
            upput = int(input('How many uppercase letters do you want? '))
            specput = int(input('How many special characters do you want? '))

            a = random.choices(numsplit, k = numput)
            b = random.choices(lowersplit, k = lowput)
            c = random.choices(uppersplit, k = upput)
            d = random.choices(specharsplit, k = specput)
            e = a + b + c + d
            random.shuffle(e)
            print('Here\'s your randomly generated password:')
            print(''.join(str(i) for i in e).replace(',', ''))
            ask = input('Would you like to create another password? y/n ')
            if ask == 'y':
                continue
            elif ask == 'n':
                print('Thank you for using our services. Have a nice day!')
            else:
                print('That is not a valid response. Goodbye')
    except ValueError:
        print('Enter a numerical value')
        continue