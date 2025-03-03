import random

movies = ['anand', 'drishyam', 'nayak', 'gol maal', 'vikram vedha', 'chava', 'Titanic', 'avatar', 'kgf', 'bahubali', 'dangal']

def create_question(movie):
    return ''.join(' ' if ch == ' ' else '*' for ch in movie)

def is_present(letter, movie):
    return letter in movie

def unlock(qn, movie, letter):
    return ''.join(movie[i] if movie[i] == letter or movie[i] == ' ' else qn[i] for i in range(len(movie)))

def play():
    p1name = input("Player 1, please enter your name: ")
    p2name = input("Player 2, please enter your name: ")
    pp1, pp2 = 0, 0
    turn = 0
    
    willing = True
    
    while willing:
        current_player = p1name if turn % 2 == 0 else p2name
        print(f"{current_player}, your turn!")
        picked_movie = random.choice(movies)
        
        qn = create_question(picked_movie)
        modified_qn = qn
        print(qn)
        
        not_said = True
        
        while not_said:
            letter = input("Your letter: ")
            
            if is_present(letter, picked_movie):
                modified_qn = unlock(modified_qn, picked_movie, letter)
                print(modified_qn)
                
                try:
                    d = int(input("Press 1 to guess the movie or 2 to unlock another letter: "))
                except ValueError:
                    print("Invalid input. Try again.")
                    continue
                
                if d == 1:
                    ans = input("Your answer: ")
                    if ans.lower() == picked_movie.lower():
                        if turn % 2 == 0:
                            pp1 += 1
                        else:
                            pp2 += 1
                        
                        print("Correct!")
                        print(f"{current_player}, your score is: {pp1 if turn % 2 == 0 else pp2}")
                        not_said = False
                    else:
                        print("Wrong answer, try again.")
                
            else:
                print(f"{letter} not found.")
        
        try:
            c = int(input("Press 1 to continue or 0 to quit: "))
        except ValueError:
            print("Invalid input. Exiting game.")
            break
        
        if c == 0:
            print(f"{p1name}, your score: {pp1}")
            print(f"{p2name}, your score: {pp2}")
            print("Thanks for playing!")
            willing = False
        
        turn += 1

play()
