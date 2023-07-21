#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

DFT_LETTER_PATH = "./Input/Letters/starting_letter.txt"
NAMES_PATH = "./Input/Names/invited_names.txt"
OUTPUT_FOLDER = "./Output/"

with open(DFT_LETTER_PATH, 'r') as dft_letter:
    letter = dft_letter.read()

with open(NAMES_PATH, 'r') as names:
    names_list = names.read().split('\n')

# for name in names_list:
#     output_file_name = OUTPUT_FOLDER + "letter_for_" + name + '.txt'
#     with open(output_file_name, 'w') as output:
#         output.write(letter.replace('[name]', name))







