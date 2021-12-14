'''
author = Dušan Goll
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# separators
separator = '-' * 38
sep_long = '=' * 70

# registered users and passwords
registered = {'Denis': "01", 'Daniel': "02", 'Dusan': "03", 'Darek': "04"}

# user login
switch_1 = True
switch_2 = True
print(f"{sep_long}\nLog in by entering username and password, or leave by commmand 'exit'.\n{sep_long}")
while switch_1:
    user = input('username: ')
    if user in registered.keys():
        switch_1 = False
        while switch_2:
            password = input('password: ')
            if password == registered.get(user):
                print(f'User logged in. Welcome in text analysator.\n{sep_long}')
                switch_2 = False
            elif password == 'exit':
                quit()
            else:
                print('Wrong password.')
    elif user == 'exit':
        quit()
    else:
        print('Entered username is\'nt in database of registered users.')

# text selecting
print('Select text to analyze, or turn off using command "exit".')
print(sep_long)
switch_3 = True
while switch_3:
    print(separator)
    print('Texts offer:     | 1 | 2 | 3 |')
    select = input('Select one of offered numbers: ')
    if select == 'exit':
        quit()
    elif not select.isdigit():
        if select.startswith('-') and select[1:].isdigit():
            print('Input is negative number.')
        else:
            print('Input contains non-digit characters.')
    else:
        if select.isdecimal() and int(select) in range(1, 4):
            switch_3 = False
        else:
            print('Number is\'nt in offer.')
selected_text = TEXTS[int(select)-1]
print(separator, '\nSELECTED TEXT:')
print(selected_text)

# slicing the text
splited_text_brutto = selected_text.split()
splited_text = []
for word in splited_text_brutto:
    if not word.endswith('.') and not word.endswith(','):
        splited_text.append(word)
    elif word.endswith('.'):
        splited_text.append(word.rstrip('.'))
    elif word.endswith(','):
        splited_text.append(word.rstrip(','))

# word count
word_count = len(splited_text)

# titlecase word count
titlecases = [word for word in splited_text if word.isalpha() and word.istitle() and not word.isupper()]
titlecases_count = len(titlecases)

# uppercase word count
upppercases = [word for word in splited_text if word.isalpha() and word.isupper()]
upppercases_count = len(upppercases)

# lowercase word count
lowercases = [word for word in splited_text if word.isalpha() and word.islower()]
lowercases_count = len(lowercases)

# number count
numbers = [word for word in splited_text if word.isdigit()]
    # adding words, that contains both alphabets and numbers
    ## Tady mi to nedalo pokoj, tak jsem si pohral a pridal i tuto variantu, ktera pojme i pripad v textu cislo '1'. kde se objevuje vyraz '30N'.
for word in splited_text:
    if any(character.isdigit() for character in word) and any(character.isalpha() for character in word):
        empty_word = ''
        filtered_word = empty_word.join(character for character in word if character.isdigit())
        numbers.append(filtered_word)

numbers_count = len(numbers)

# sum of numbers
numbers_integers = [int(number) for number in numbers]
sum_of_numbers = sum(numbers_integers)

# finding maximal lenght of word in text
lenghts_of_words = []
for word in splited_text:
    lenghts_of_words.append(len(word))
max_lenght = max(lenghts_of_words)

# occurences
occurences = {}
for number in range(1, (max_lenght + 1)):
    occurences[number] = lenghts_of_words.count(number)

# STATISTICS
print(f'{separator}\nAbout selected text:')
print(f'There is/are:\t{word_count} word(s)')
print(f'\t\t\t\t{titlecases_count} titlecase word(s)')
print(f'\t\t\t\t{upppercases_count} uppercase word(s)')
print(f'\t\t\t\t{lowercases_count} lowercase word(s)')
print(f'\t\t\t\t{numbers_count} number(s)')
print(f'The sum of all numbers is {sum_of_numbers}.')
print(separator)
print('LENGHT'.rjust(8), 'OCCURENCES'.center(20), 'NR.'.ljust(5), sep='|')
print(separator)
for key in occurences:
    print((str(key).rjust(8)), ('*' * int(occurences.get(key))).ljust(20), str(occurences.get(key)).ljust(5), sep='|')
print(separator)
