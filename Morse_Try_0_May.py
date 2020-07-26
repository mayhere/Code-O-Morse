def morse(txt):
    encrypt = {
        #Alphabets
        'A' : '.-',
        'B' : '-...',
        'C' : '-.-.',
        'D' : '-..',
        'E' : '.',
        'F' : '..-.',
        'G' : '--.',
        'H' : '....',
        'I' : '..',
        'J' : '.---',
        'K' : '-.-',
        'L' : '.-..',
        'M' : '--',
        'N' : '-.',
        'O' : '---',
        'P' : '.--.',
        'Q' : '--.-',
        'R' : '.-.',
        'S' : '...',
        'T' : '-',
        'U' : '..-',
        'V' : '...-',
        'W' : '.--',
        'X' : '-..-',
        'Y' : '-.--',
        'Z' : '--..',

        #Numbers
        '0' : '-----',
        '1' : '.----',
        '2' : '..---',
        '3' : '...--',
        '4' : '....-',
        '5' : '.....',
        '6' : '-....',
        '7' : '--...',
        '8' : '---..',
        '9' : '----.',

        #Symblos
        ' ' : '  ',
        '.' : '.-.-.-',
        ',' : '--..--',
        '?' : '..--..',
        '\'': '.----.',
        '!' : '-.-.--',
        ':' : '---...',
        '$' : '...-..-',
        '@' : '.--.-.'
        
                }

    decrypt = {v: k for k, v in encrypt.items()}
    if '-' in txt:
        return ''.join(decrypt[i] for i in txt.split())
    return ' '.join(encrypt[i] for i in txt.upper())

exit='y'
while exit=='y':
    c=int(input("""Choose your convertor
    1.Morse to Text
    2.Text to Morse
    3.Exit\n"""))

    if c==1: 
        mor=str(input("Enter your input in morse:"))
        print("Morse to text:")
        print(mor,": ",morse(mor))

    elif c==2:
        txt=str(input("Enter your input in text:"))
        print("Text to Morse:")
        print(txt,": ",morse(txt))

    elif c==3:
        print("Thanks for using...")
        break

    else:
        print("Plase enter valid input !!!")

    if exit=='y':
        exit=str(input("You want to use it again: y/n: "))
        if exit=='n':
            print("Thanks for using...")
            break        


    
    
