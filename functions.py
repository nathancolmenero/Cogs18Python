import string
import random

def is_question(input_string):
    
    if '?' in input_string:
        output = True
    else:
        output = False
    return output


def remove_punctuation(input_string):
    
    out_string = ''
    
    for char in input_string:
        if char not in string.punctuation:
            out_string += char
    return out_string


def prepare_text(input_string):
    
    out_list = []
    
    input_string = input_string.lower()
    
    input_string = remove_punctuation(input_string)
    
    out_list = input_string.split()
    
    return out_list

def selector(input_list, check_list, return_list):
    
    output = None
    
    for item in input_list:
        if item in check_list:
            output = random.choice(return_list)
            break
    return output


def string_concatenator(string1, string2, separator):
    
    output = []
    
    output = string1 + separator + string2
    
    return output


def list_to_string(input_list, separator):
    
    output = input_list[0]
    
    for item in input_list[1:]:
        output = string_concatenator(output, item, separator)
    return output


def end_chat(input_list):
    
    output = bool()
    
    if 'quit' in input_list:
        output = True
    else:
        output = False
    return output


def is_in_list(list_one, list_two):
    
    for element in list_one:
        if element in list_two:
            return True
    return False


def find_in_list(list_one, list_two):
    
    for element in list_one:
        if element in list_two:
            return element
    return None

def select_language(language_input):
    """Lets the user choose the language they prefer.
    
    Parameters
    ----------
    language : dictionary
        name of language used input : language used output
    """
    if language_input.lower().startswith('eng'):
        language = 'english'
    elif language_input.lower().startswith('swe'):
        language = 'swedish'
    else:
        raise ValueError
    return language