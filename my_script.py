import string
import random

# Functions used for the chatbot
from data import language_interface

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
    """Check if any element of list_one is in list_two."""

    for element in list_one:
        if element in list_two:
            return True
    return False


def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""

    for element in list_one:
        if element in list_two:
            return element
    return None


# Chatbot input messages
def lets_chat():
    """Function that runs the chatbot"""
    # Input message from user
    inp = None
    while not inp == 'quit':
        language_input = input('Please input the language you want to chat(english or swedish): ')
        if language_input.lower().startswith('eng'):
            language = 'english'
            break
        elif language_input.lower().startswith('swe'):
            language = 'swedish'
            break
        else:
            print('Please enter a valid choice. Type "quit" to enter')
            continue

    while True:

        msg = input('INPUT :\t')
        out_msg = None

        language_dict =  language_interface[language]

        # Check if input is a question
        question = is_question(msg)

        # Prepare input message
        msg = prepare_text(msg)

        # Checks for end message
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False
            break

        if not out_msg:
            
            outs = []

            outs.append(selector(msg, language_dict['GREETINGS_IN'], language_dict['GREETINGS_OUT']))

            outs.append(selector(msg, language_dict['WEATHER_IN'], language_dict['WEATHER_OUT']))

            outs.append(selector(msg, language_dict['BRUNCH_IN'], language_dict['BRUNCH_OUT']))

            outs.append(selector(msg, language_dict['SING_IN'], language_dict['SING_OUT']))

            outs.append(selector(msg, language_dict['COUNTRY_IN'], language_dict['COUNTRY_OUT']))

            outs.append(selector(msg, language_dict['NEWS_IN'], language_dict['NEWS_OUT']))

            if is_in_list(msg, language_dict['PEOPLE_IN']):
                name = find_in_list(msg, language_dict['PEOPLE_IN'])
                outs.append(list_to_string([language_dict['PEOPLE_NAMES'][name], name.capitalize(),
                                            selector(msg, language_dict['PEOPLE_IN'], language_dict['PEOPLE_OUT'])],
                                           ' '))

            # Taboo words Glenn won't talk about
            if is_in_list(msg, language_dict['NONO_IN']):
                outs.append(list_to_string([selector(msg, language_dict['NONO_IN'], language_dict['NONO_OUT']),
                                            find_in_list(msg, language_dict['NONO_IN'])], ' '))

            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)
        # Words Glenn doesn't know yet
        if not out_msg:
            out_msg = random.choice(language_dict['UNKNOWN'])

        print('OUTPUT:', out_msg)


lets_chat()