# Swedish sayings
swedish_response_dict = {'GREETINGS_IN': ['hej', 'tja', 'hallÃ¥'],
                         'GREETINGS_OUT': ["Hallå eller, jag heter Glenn. Behöver du hjälp?"],

                         'WEATHER_IN': ['klimat', 'väder'],
                         'WEATHER_OUT': ["I dag? Fruktansvärd! Eller i morgon, skit också!",
                                         "Dåligt väder!"],

                         'BRUNCH_IN': ['fika', 'mat'],
                         'BRUNCH_OUT': ["FIKA TIME!!"],

                         'SING_IN': ['sjunga', 'musik'],
                         'SING_OUT': ["Alla heter Glenn i Göteborg!",
                                      "Håkan Hellström, eller ABBA?"],

                         'COUNTRY_IN': ['schweiz'],
                         'COUNTRY_OUT': ["Nej!! Jag är från Sverige!"],

                         'NEWS_IN': ['nyheter', 'politik'],
                         'NEWS_OUT': ["Brexit är en katastrof!",
                                      "Stefan Löfven?"],

                         'PEOPLE_IN': ['glennson', 'långstrump'],
                         'PEOPLE_OUT': ["är fantastiskt", "har långt hår"],
                         'PEOPLE_NAMES': {'glennson': 'Glenn', 'långstrump': 'Pippi'},

                         'NONO_IN': ['norge', 'ryssland', 'amerika'],
                         'NONO_OUT': ["Jag vill inte prata om"],

                         'UNKNOWN': ['Bra', 'Okej', 'Va??', 'Ja', 'Tack!']
                         }

# English sayings
english_response_dict = {'GREETINGS_IN': ['hello', 'hi', 'hey'],
                         'GREETINGS_OUT': ['Hello, I am Glenn. How can I help you?'],

                         'WEATHER_IN': ['climate', 'weather'],
                         'WEATHER_OUT': ['Sunny today', 'Ah, another day in paradise! :)'],

                         'BRUNCH_IN': ['brunch', 'hungry', 'lunch', 'eat', 'food'],
                         'BRUNCH_OUT': ["Yes! I'm starving", 'Tacos sound good!', 'Mmm, pizza!'],

                         'SING_IN': ['sing', 'music'],
                         'SING_OUT': ['I can definitely sing for you!', 'Maybe some oldies?'],

                         'COUNTRY_IN': ['canada'],
                         'COUNTRY_OUT': ["Our neighbor to the north?",
                                         "I've only been a few times",
                                         "Definitely try a poutine! Amazing!"],

                         'NEWS_IN': ['news', 'politics'],
                         'NEWS_OUT': ["Brexit is turning into a nightmare!",
                                      "Hopefully the democrats can take back the White House in 2020"],

                         'PEOPLE_IN': ['gretzky', 'frobisher'],
                         'PEOPLE_OUT': ["is very talented", "is such a cool Canadian"],
                         'PEOPLE_NAMES': {'gretzky': 'Wayne', 'frobisher': 'Martin'},

                         'NONO_IN': ['trump', 'putin', 'hotdogs'],
                         'NONO_OUT': ["I don't want to talk about"],

                         'UNKNOWN': ['Good', 'Okay', 'Huh?', 'Yasssss!', 'Thank you!']
                         }

language_interface = {
    'english': english_response_dict,
    'swedish': swedish_response_dict
}