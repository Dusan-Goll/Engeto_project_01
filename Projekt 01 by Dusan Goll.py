# author = Dušan Goll

from string import punctuation as pun

TEXTS = [
    '''Situated about 10 miles west of Kemmerer, 
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
100 feet below the top , of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
separator = '-' * 50
sep_long = '=' * 70
user_database = {'Denis': "01", 'Daniel': "02", 'Dusan': "03", 'Darek': "04"}

username = input('username: ')
password = input('password: ')
if password != user_database.get(username):
    quit()
print(separator)

select = input(f'Select text - enter number from 1 to {len(TEXTS)}: ')
if not (select.isnumeric() and int(select) in range(1, len(TEXTS) + 1)):
    quit()
else:
    t_select = TEXTS[int(select) - 1]
print(separator, '\nSELECTED TEXT:\n', t_select)

clean_words = [
    word.strip(pun) for word in t_select.split() if word.strip(pun)
]

word_count = len(clean_words)

titlecases = [word for word in clean_words if word.istitle()]
titlecases_count = len(titlecases)

upppercases = [word for word in clean_words
               if word.isalpha() and word.isupper()]
upppercases_count = len(upppercases)

lowercases = [word for word in clean_words
              if word.isalpha() and word.islower()]
lowercases_count = len(lowercases)

numbers = [int(word) for word in clean_words if word.isdigit()]
numbers_count = len(numbers)

sum_of_numbers = sum(numbers)

word_lenghts = [len(word) for word in clean_words]
max_lenght = max(word_lenghts)

occurences = {}
for number in range(1, (max_lenght + 1)):
    occurences[number] = word_lenghts.count(number)

print(f'{separator}\nAbout selected text:')
print('There is/are:'.ljust(15), f'{word_count}\tword(s)')
print(' '.ljust(15), f'{titlecases_count}\ttitlecase word(s)')
print(' '.ljust(15), f'{upppercases_count}\tuppercase word(s)')
print(' '.ljust(15), f'{lowercases_count}\tlowercase word(s)')
print(' '.ljust(15), f'{numbers_count}\tnumber(s)')
print(f'The sum of all numbers is {sum_of_numbers}.')
print(separator)
print('LENGHT'.rjust(8), 'OCCURENCES'.center(20), 'NR.'.ljust(5), sep='|')
print(separator)
for key in occurences:
    print((str(key).rjust(8)), ('*' * int(occurences.get(key))).ljust(20),
          str(occurences.get(key)).ljust(5), sep='|')
print(separator)
