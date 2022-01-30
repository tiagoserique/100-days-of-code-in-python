
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER = "[name]"


def read_names():
    with open("input/names/invited_names.txt", "r") as names:
        names_content = names.readlines()
        
        for name in names_content:
            stripped_name = name.strip('\n')
            index = names_content.index(name)
            names_content[index] = stripped_name

    return names_content


def read_letter():
    with open("input/letters/starting_letter.txt", "r") as letters:
        letter_content = letters.read()

    return letter_content


def write_letters(names, letter_model):
    for name in names:
        new_letter = letter_model.replace(PLACEHOLDER, name)
        
        with open(f"output/ready_to_send/letter_for_{name}.txt", "w") as output:
            output.write(new_letter)
                


names           = read_names()
letter_model    = read_letter()

write_letters(names, letter_model)