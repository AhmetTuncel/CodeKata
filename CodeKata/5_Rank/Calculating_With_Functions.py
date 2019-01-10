def zero(*args): 
    if not args:
        return 0
    elif args[0][1] == '+':
        return args[0][0]
    elif args[0][1] == '-':
        return 0 - args[0][0] 
    elif args[0][1] == '*':
        return 0
    elif args[0][1] == '/':
        return 0

def one(*args): 
    if not args:
        return 1
    elif args[0][1] == '+':
        return 1 + args[0][0]
    elif args[0][1] == '-':
        return 1 - args[0][0] 
    elif args[0][1] == '*':
        return args[0][0]
    elif args[0][1] == '/':
        return int(1 /args[0][0])


def two(*args): 
    if not args:
        return 2
    elif args[0][1] == '+':
        return args[0][0] + 2
    elif args[0][1] == '-':
        return 2 - args[0][0] 
    elif args[0][1] == '*':
        return args[0][0] * 2
    elif args[0][1] == '/':
        return int(2 / args[0][0])



def three(*args): 
    if not args:
        return 3
    elif args[0][1] == '+':
        return args[0][0] + 3
    elif args[0][1] == '-':
        return 3 - args[0][0]
    elif args[0][1] == '*':
        return args[0][0] * 3
    elif args[0][1] == '/':
        return int(3 / args[0][0])



def four(*args): 
    if not args:
        return 4
    elif args[0][1] == '+':
        return args[0][0] + 4
    elif args[0][1] == '-':
        return 4 - args[0][0]
    elif args[0][1] == '*':
        return args[0][0] * 4
    elif args[0][1] == '/':
        return int(4 / args[0][0])



def five(*args): 
    if not args:
        return 5
    elif args[0][1] == '+':
        return args[0][0] + 5
    elif args[0][1] == '-':
        return 5 - args[0][0]
    elif args[0][1] == '*':
        return args[0][0] * 5
    elif args[0][1] == '/':
        return int(5 / args[0][0])

def six(*args): 
    if not args:
        return 6
    elif args[0][1] == '+':
        return args[0][0] + 6
    elif args[0][1] == '-':
        return 6 - args[0][0]
    elif args[0][1] == '*':
        return args[0][0] * 6
    elif args[0][1] == '/':
        return int(6 / args[0][0])


def seven(*args): 
    if not args:
        return 7
    elif args[0][1] == '+':
        return args[0][0] + 7
    elif args[0][1] == '-':
        return 7 - args[0][0]
    elif args[0][1] == '*':
        return args[0][0] * 7
    elif args[0][1] == '/':
        return int(7 / args[0][0])


def eight(*args): 
    if not args:
        return 8
    elif args[0][1] == '+':
        return args[0][0] + 8
    elif args[0][1] == '-':
        return 8 - args[0][0]
    elif args[0][1] == '*':
        return args[0][0] * 8
    elif args[0][1] == '/':
        return int(8 / args[0][0])

def nine(*args): 
    if not args:
        return 9
    elif args[0][1] == '+':
        return args[0][0] + 9
    elif args[0][1] == '-':
        return 9 - args[0][0]
    elif args[0][1] == '*':
        return args[0][0] * 9
    elif args[0][1] == '/':
        return int(9 / args[0][0])



def plus(number): 
    return number,'+'

def minus(number): 
    return number,'-'

def times(number): 
    return number,'*'

def divided_by(number): 
    return number,'/'