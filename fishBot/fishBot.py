import pyautogui
import time
import logging
import pydirectinput



def skrypt(sec, point):
    while True:

        Lokalizacja_czegos = pyautogui.locateOnScreen('pandora_fish.png', region=(point), confidence=0.6)
        if Lokalizacja_czegos:
           # print("[!] COŚ BIERZE!!")
            combination(sec)



def combination(sec):
    #czas do wyciągnięcia wędki z wody (3.3 najlepszy)
    time.sleep(float(sec))
    pydirectinput.keyDown('w')
    time.sleep(0.2)
    pydirectinput.keyUp('w')

    time.sleep(2)
    print("[!] Jest branie")
    print("____________________")
    pydirectinput.keyDown("f1")
    time.sleep(0.2)
    pydirectinput.keyUp("f1")
    time.sleep(3)
    pydirectinput.keyDown("space")
    time.sleep(0.2)
    pydirectinput.keyUp("space")

    global loop
    loop +=1

    print("[" + str(loop) + "] Próba")
    print("[!] Łowienie...")


def skan():
    while True:
        point = pyautogui.locateOnScreen('pandora_fish.png', confidence=0.6)
        if point:
            left , top, x, y= point[0], point[1], point[2], point[3]
            print(point)

            #############powiększanie zakresu skanowania dla większego marginesu błędu

            left-=50
            top-=20
            x+=100
            y+=100
            return (left,top,x,y)




# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

print('__________.__    .___                ______________ ')
print('\______   \__| __| _/____   ____    /  |  \______  \\' )
print(' |    |  _/  |/ __ |/  _ \ /    \  /   |  |_  /    /')
print(' |    |   \  / /_/ (  <_> )   |  \/    ^   / /    / ')
print(' |______  /__\____ |\____/|___|  /\____   | /____/  ')
print('        \/        \/           \/      |__|        \n')
print('FISHBOT V1.1 by Bidon47')
print('INSTRUKCJA: ')
print('[*] Upewnij się że grasz na rozdzielczości 800x600, w trybie okienkowym')
print('[*] Bindujemy robaczki pod klawisz F1 ' )
print('[*] Stając nad wodą oddalamy maksymalnie kamerę, a następnie ustawiamy ją w taki sposób, \n aby komunikat złowionej ryby wyświetlał się na tle wody')
print('[*] Nie ruszaj kamerą podczas działania bota')
print('[*] Okno gry zawsze musi być aktywne' )
print('[*] Zakończenie działania bota: CTRL+C')
print('[*] Wszystkie problemy z programem zgłaszać do Bidon47')
sec = input('Podaj interwał (zalecany: 3.3): ')
print("\n\n\n\n\n\n\n")
print("[!] Rozpocznij łowienie w celu zeskanowania ekranu")



#########START#####################
loop = 1
global left, top, x, y
point = skan()
test=pyautogui.screenshot(region=(point))
test.save('test22.png')
skrypt(sec, point)

