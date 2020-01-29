
import random


def name_age():
    return [input('Enter name: '), input('enter age: ')]


def height_weight():
    return [input('Enter height: '), input('enter weight: ')]


def occupation_hobby():
    return [input('Enter occupation: '), input('enter hobby: ')]


def complextion_race():
    return [input('Enter complextion: '), input('enter race: ')]


def city_country():
    return [input('Enter city: '), input('enter country: ')]


questions = [name_age, height_weight, occupation_hobby,
             complextion_race, city_country]

#####NAME AND AGE ANSWERS#################
intro = random.choice(['my name is ', 'I am ', 'my friend\'s name is ',
                       'there\'s a human whose name is '])

intro_2 = random.choice(
    [' i am ', ' my age is ', 'i have the age of ', ' i am very young that my age is '])

mid = random.choice([' i love ice cream so much that i can kill for it ',
                     ' i am so much in love with programming ', ' i am a very good christian that loves not going to church '])

end = random.choice([' i promise to be serious with my studies and skills learning', ' from today onwards, i will never miss deadline for a task',
                     ' as ive known that putting much effort will make you achieve more, ill try to put more effort'])

###### HEIGHT AND WEIGHT ############################

start_1_1 = random.choice(['height is something that makes a man handsome ', 'humans often have the height of ',
                           'most animals that stand on two legs and eat other animals have the height of and not only '])

start_1_2 = random.choice([' not only height matters, but weight also add a lot to humans, some humans have the weight of ',
                           'just as the human that has the height above, humans also have much weight just such as ', 'anyone that has that height above should have the weight of '])

mid_1_1 = random.choice([' let\'s not forget that obesity is measured with the human\'s height and weight. ',
                         ' height and weight also is of very huge consideration in sports', 'omo, make sure say u get better height ooooo, else nobody go gree marry you '])

end_1_1 = random.choice(
    [' finally, make sure say u dey drink enough water if you want to get enough height', ' my advice to you is that you should start drinking enough water cause you are weightless'])

randomQuestions = random.choice(questions)

if randomQuestions == name_age:
    name_and_age = name_age()

    print(intro + name_and_age[0] + intro_2 +
          name_and_age[1] + 'years.' + mid + end)

elif randomQuestions == height_weight:
    height_and_weight = height_weight()

elif randomQuestions == occupation_hobby:
    occupation_and_hobby = occupation_hobby()

    print(occupation_and_hobby)

elif randomQuestions == complextion_race:
    complextion_and_race = complextion_race()

    print(complextion_and_race)
else:
    city_and_country = city_country()

    print(city_and_country)
