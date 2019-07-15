import pyautogui, sys, math
print('')
print('     You have some choices     ')
print('Type l for absolute location ')
print('Type lo to enter offset manually ')
print('Type lc to enter offset by clicking on screen  ')
print('Type d for distance ')
print('')
print('--Type Ctrl-c to exit--')
mode = input()
null = 1
keyTrig1 = 1
keyTrig2 = 1

## This is a comment - define your functions here....

## Make your nested fucntions here....

while True:
    while True:
        answer = input('Type y to continue (y/n): ')
        keyTrig2 = 1
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':


        try:
            if mode == 'l':
                while True:
                    x1, y1 = pyautogui.position()
                    positionStr = 'X: ' + str(x1).rjust(4) + ' Y: ' + str(y1).rjust(4) + ' (press ENTER to save position)'
                    print(positionStr, end='')
                    print('\b' * len(positionStr), end='', flush=True)
            if mode == 'lo':
                offx = int(input('enter x offset...  '))
                offy = int(input('enter y offset...  '))
                while True:
                    x1, y1 = pyautogui.position()
                    positionStr = 'X: ' + str(x1-offx).rjust(4) + ' Y: ' + str(y1-offy).rjust(4)
                    print(positionStr, end='')
                    print('\b' * len(positionStr), end='', flush=True)
            if mode == 'lc':
                print('Type 0 when mouse is a 0,0')
                while keyTrig1 == 1:
                    keyTrig1 = input()
                    offx, offy = pyautogui.position()
                while True:
                    x1, y1 = pyautogui.position()
                    positionStr = 'X: ' + str(x1-offx).rjust(4) + ' Y: ' + str(y1-offy).rjust(4)
                    print(positionStr, end='')
                    print('\b' * len(positionStr), end='', flush=True)
            if mode == 'd':
                print('Type ENTER at first location and ENTER at second location  ')
                while keyTrig2 == 1:
                    null = input()
                    xloc1, yloc1 = pyautogui.position()
                    keyTrig2 = input()
                    xloc2, yloc2 = pyautogui.position()
                xdist = xloc2-xloc1
                ydist = yloc2-yloc1
                ddist = math.ceil(math.sqrt((xdist^2)+(ydist^2)))
                print('The X distance is        = ' + str(xdist))
                print('The Y distance is        = ' + str(ydist))
                print('The diagonal distance is = ' + str(ddist))
            
        except KeyboardInterrupt:
            print('\n')


        continue
    else:
        print('Goodbye')
        break