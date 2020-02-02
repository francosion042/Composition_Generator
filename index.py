
import random
from functions import *
from compositions import *


def prompt():
    return input('do you want to run again? [y/n]')


def compose():

    questions = [name_age, height_weight, occupation_hobby,
                 complextion_race, city_country]

    randomQuestions = random.choice(questions)

    if randomQuestions == name_age:
        name_and_age = name_age()

        print(intro + name_and_age[0] + intro_2 +
              name_and_age[1] + 'years.' + mid + end + '\n')
        if prompt() == 'y' or 'yes':
            compose()
        else:
            break

    elif randomQuestions == height_weight:
        height_and_weight = height_weight()

        print(start_1_1 + height_and_weight[0] + start_1_2 +
              height_and_weight[1] + mid_1_1 + end_1_1 + '\n')
        if prompt() == 'y' or 'yes':
            compose()
        else:
            break

    elif randomQuestions == occupation_hobby:
        occupation_and_hobby = occupation_hobby()

        print(start_2_1 + occupation_and_hobby[0] +
              mid_2_1 + occupation_and_hobby[1] + end_2_1 + '\n')
        if prompt() == 'y' or 'yes':
            compose()

    elif randomQuestions == complextion_race:
        complextion_and_race = complextion_race()

        print(start_3_1 + complextion_and_race[0] +
              mid_3_1 + complextion_and_race[1] + end_3_1 + '\n')
        if prompt() == 'y' or 'yes':
            compose()
    else:
        city_and_country = city_country()

        print(city_and_country[0] + start_4_1 +
              mid_4_1 + city_and_country[1] + end_4_1 + '\n')
        if prompt() == 'y' or 'yes':
            compose()


compose()
