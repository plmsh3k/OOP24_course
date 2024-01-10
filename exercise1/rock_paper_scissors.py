from random import randint

choices = ['R', 'P', 'S']
player = {
    'choice' : '',
    'score' : 0
} 
computer = {
    'choice' : '',
    'score' : 0
}

def main():
    while (player['score'] < 3) and (computer['score'] < 3):
        round()
    if player['score'] == 3:
        print('You won!')
    if computer['score'] == 3:
        print('You lost!')
 
def round():
    player['choice'] = input('Give your choice (R, P, S): ')   
    computer['choice'] = choices[randint(0,2)]
    match computer['choice']:
        case 'R': print("Computer's choice is Rock.")
        case 'P': print("Computer's choice is Paper.")
        case 'S': print("Computer's choice is Scissors.")
    evaluation()

def evaluation():
    match player['choice']: 
        case 'R': 
            match computer['choice']:
                case 'R':
                    print("It's a tie!")
                case 'P':
                    print('Paper covers Rock.')
                    computer['score'] += 1
                case 'S':
                    print('Rock crushes Scissors.')
                    player['score'] += 1
        case 'P': 
            match computer['choice']:
                case 'R':
                    print('Paper covers Rock.')
                    player['score'] += 1
                case 'P':
                    print("It's a tie!")
                case 'S':
                    print('Scissors cuts Paper.')
                    computer['score'] += 1
        case 'S': 
            match computer['choice']:
                case 'R':
                    print('Rock crushes Scissors.')
                    computer['score'] += 1
                case 'P':
                    print('Scissors cuts Paper.')
                    player['score'] += 1
                case 'S':
                    print("It's a tie!")
    print(f"Computer {computer['score']} | {player['score']} You")
    print()

main()