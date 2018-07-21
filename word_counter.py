active = True
print

while active == True:
    print('Starting up...')

    try:
        file_name = input('Which file do you want to scan?')
        print("type 'q' to quit. ")
        if file_name == 'q':
            active = False
            break
            print('Cleaning up...\nExiting program...\nThank you!')
        print('Scanning...')
    except NameError:
        msg = "The file finder has a bug. We can't find your file"
     
        print(msg)

    try:
        with open(file_name, encoding='utf-8') as f_obj:
            contents = f_obj.read()

    except FileNotFoundError:
        msg = "We can't find " + file_name
        print(msg)

    else:
        num_words = str(len(contents.split())) + " words"
        num_characters = str(len(contents)) + " characters"
        period = len(contents.split('.'))
        question = len(contents.split('?'))
        exclamation = len(contents.split('!'))
        num_sentences =  str(period + question + exclamation)+ ' sentences'
     
                                                                                                
        print('After scanning ' + file_name + ', we have gathered the following results:')
        print('The file ' + file_name + " has:")
        print(num_words)
        print(num_characters)
        print(num_sentences)

        try:
            repeat = input('Do you want to scan another file(yes/no)?')
            if repeat == 'no':
                active = False
                print('Cleaning up...\nThank you!')
            else:
                print('Cleaning up...\nReloading...')
        except NameError:
            print('Sorry, we couldn\'t load up the full program')

