
import random
import time

word_level_1 = ['botas', 'bayas', 'croar']
word_level_2 = ['bolsillo', 'cerrojo', 'bonita']

level = 1 
correct = 0
strike = 0

def show_word():
    machine_word = random.choice(word_level_1)
    print(machine_word, end='\r')
    time.sleep(1.5)
    print('     ')
    return machine_word


def game(machine_word):
    global level, correct, strike
    human_word = input("¿Cuál era la palabra?")

    if machine_word == human_word:
        correct =+ 1
        print("level = {}, correct = {}, strike = {}".format(level, correct, strike))
        if correct == 3:
            level =+ 1
            correct = 0
            print("level = {}, correct = {}, strike = {}".format(level, correct, strike))
            if level == 3:
                correct =+ 1
                print("level = {}, correct = {}, strike = {}".format(level, correct, strike))
                if correct == 3:
                    print("Felicidades ganaste este juego")
                else:
                    show_word()
            else:
                show_word()
        else:
           game(show_word())
    else:
        if level == 1:
            strike =+ 1
            print("level = {}, correct = {}, strike = {}".format(level, correct, strike))
            if strike == 3:
                print("Reiniciando juego")
            else:
                show_word()
        else:
            level =- 1
            strike =+ 1
            print("level = {}, correct = {}, strike = {}".format(level, correct, strike))
            if strike == 3:
                print("Reiniciando juego")
            else:
                show_word()
    

if __name__ == '__main__':
    game(show_word())

