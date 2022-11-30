import os, time, sys

os.system('clear')


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(9. / 100)


logo = '''\033[1;91m============================================
\033[1;92m  ██████  ███████  █████   ███    ███  █████
\033[1;93m ██    ██ ██      ██   ██  ██ ████ ██ ██   ██
\033[1;94m ██    ██ ███████ ███████  ██ ████ ██ ███████
\033[1;95m ██    ██      ██ ██   ██  ██  ██  ██ ██   ██
\033[1;96m   ████   ███████ ██   ██  ██      ██ ██   ██                                                                                                                                      
\033[1;91m=============================================
  '''
m = '''\033[1;31;40m [\033[1;33;40m01\033[1;31;40m]\033[1;36;40m Termux open google browser
\033[1;31;40m [\033[1;33;40m02\033[1;31;40m]\033[1;36;40m Termux fire
\033[1;31;40m [\033[1;33;40m03\033[1;31;40m]\033[1;36;40m Mathomatic
\033[1;31;40m [\033[1;33;40m04\033[1;31;40m]\033[1;36;40m Moving Train
\033[1;31;40m [\033[1;33;40m05\033[1;31;40m]\033[1;36;40m Cowsay
\033[1;31;40m [\033[1;33;40m06\033[1;31;40m]\033[1;36;40m Play Moon-buggy
\033[1;31;40m [\033[1;33;40m07\033[1;31;40m]\033[1;36;40m Open hacker Termux
\033[1;31;40m [\033[1;33;40m08\033[1;31;40m]\033[1;36;40m Play Basted
\033[1;31;40m [\033[1;33;40m09\033[1;31;40m]\033[1;36;40m Play Ninvaders\033[1;33;40m (\033[1;31;40mZoom Out On Terminal\033[1;33;40m)
\033[1;31;40m [\033[1;33;40m10\033[1;31;40m]\033[1;36;40m Play Snack\033[1;33;40m (\033[1;31;40mZoom Out On Terminal\033[1;33;40m) \n \033[1;31;40m[\033[1;33;40m11\033[1;31;40m]\033[1;36;40m Play nInvaders \n \033[1;31;40m[\033[1;33;40m12\033[1;31;40m]\033[1;36;40m Play Greed \n \033[1;31;40m[\033[1;33;40m13\033[1;31;40m]\033[1;36;40m Play Nethack \n \033[1;31;40m[\033[1;33;40m14\033[1;31;40m] \033[1;36;40mPlay Sudoku \n \033[1;31;40m[\033[1;33;40m15\033[1;31;40m]\033[1;36;40m Exit 
'''

print(logo)
time.sleep(1)
slowprint('\033[1;32;40m  Welcome To\033[1;33;40m OSAMA Tools')
# slowprintm('hjiiij sjsjdjdj djdjjdjdjdjd')


print('''
 \033[1;31;40m [\033[1;33;40m01\033[1;31;40m]\033[1;36;40m Start
 \033[1;31;40m [\033[1;33;40m02\033[1;31;40m]\033[1;36;40m Contact Facebook
 \033[1;31;40m [\033[1;33;40m03\033[1;31;40m]\033[1;36;40m Github
 \033[1;31;40m [\033[1;33;40m04\033[1;31;40m]\033[1;36;40m Website
 \033[1;31;40m [\033[1;33;40m05\033[1;31;40m]\033[1;36;40m Exit
''')

mo4 = input('\033[1;33;40m  Enter \033[1;31;40m>>> \033[1;33;40m')

if mo4 == '1' or mo4 == '01':
    os.system('xdg-open https://www.facebook.com/profile.php?id=100024557781911')
    time.sleep(2)

    os.system('clear')

    print(logo)

    print(m)

    mo = input('\033[1;33;40m Enter \033[1;31;40m>>> \033[1;33;40m')

    if mo == '1' or mo == '01':
        os.system('apt install w3m')
        os.system('clear')
        print(logo)
        print('continue To Type Main.py')
        os.system('w3m google.com')

    elif mo == '2' or mo == '02':
        os.system('pkg install libcaca')
        os.system('clear')
        os.system('cacafire')

    elif mo == '3' or mo == '03':
        os.system('apt install mathomatic')
        os.system('clear')
        os.system('mathomatic')

    elif mo == '4' or mo == '04':
        os.system('pkg install sl')
        os.system('clear')
        os.system('sl')

    elif mo == '5' or mo == '05':
        os.system('pkg  install cowsay')
        os.system('clear')
        os.system('cowsay Hello')

    elif mo == '6' or mo == '06':
        os.system('pkg inatall moon-buggy')
        os.system('clear')
        print('press scape to jump')
        time.sleep(1.5)
        os.system('moon-buggy')

    elif mo == '7' or mo == '07':
        os.system('apt install cmatrix')
        os.system('clear')
        os.system('cmatrix')

    elif mo == '8' or mo == '08':
        os.system('pkg install bastet')
        os.system('clear')
        os.system('bastet')

    elif mo == '9' or mo == '09':
        os.system('pkg install ninvaders')
        os.system('clear')
        os.system('ninvaders')

    elif mo == '10':
        os.system('pkg install nsnake')
        os.system('clear')
        os.system('nsnake')

    elif mo == '11':
        os.system('pkg install ninvaders')
        os.system('clear')
        os.system('ninvaders')

    elif mo == '12':
        os.system('pkg install greed')
        os.system('clear')
        os.system('greed')


    elif mo == '13':
        os.system('pkg install nethack')
        os.system('clear')
        os.system('nethack')

    elif mo == '14':
        os.system('pkg install nudoku && apt install nudoku')
        os.system('clear')
        os.system('nudoku')

    elif mo == '15':
        os.system('exit')
        os.system('')

elif mo4 == '2' or mo4 == '02':
    os.system('xdg-open https://www.facebook.com/profile.php?id=100024557781911')
    os.system('python main.py')
elif mo4 == '3' or mo4 == '03':
    os.system('xdg-open https://www.facebook.com/profile.php?id=100024557781911')
    os.system('python main.py')
elif mo4 == '4' or mo4 == '04':
    os.system('xdg-open https://www.facebook.com/profile.php?id=100024557781911')
    os.system('python main.py')
elif mo4 == '5' or mo4 == '05':
    os.system('exit')