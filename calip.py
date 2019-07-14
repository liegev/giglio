import pyautogui, sys
print('')
print('Press Ctrl-C to quit.')
print('')
offx = int(input('enter x offset...  '))
offy = int(input('enter y offset...  '))
try:
    while True:
        x1, y1 = pyautogui.position()
        positionStr = 'X: ' + str(x1+offx).rjust(4) + ' Y: ' + str(y1+offy).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
