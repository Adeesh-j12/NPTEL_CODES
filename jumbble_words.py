#Jumbal words game.
import random
def choose():
  words=["adeesh","youtube","nidhi","spekar","motherbord","lucifer","pushpa","newspaper","rectangle","institute"]
  pick=random.choice(words )
  return pick
def jumble(word):
  jumbled="".join(random.sample(word,len(word)))
  return jumbled

def play():
    p1name=input("enter your name player 1")
    p2name=input("enter your name player 2")
    pp1=0  # points of player 1.
    pp2=0  # pointes of player 2.
    turn=0 # to track whose turn is this.
    while(1):
      #computers task
      picked_word=choose()
      #creat quastion
      qn=jumble(picked_word)
      print(qn)
      #player 1turn
      if turn%2==0:
        print(p1name,"your turn")
        ans=input("what is in your mind")
        if (ans==picked_word):
          pp1=pp1+1
          print("your score is",pp1)
        else:
          print("better luck next time")
        c=int(input("press 1 to continue and 0 to quit"))
        if (c==0):
          print(p1name,"your final score is",pp1)
          print(p2name,"your final score is",pp2)
          break
        #player 2 turn
      else:
        print(p2name,"your turn")
        ans=input("what is in your mind")
        if (ans==picked_word):
          pp2=pp2+1
          print("your score is",pp2)
        else:
          print("better luck next time")
        c=int(input("press 1 to continue and 0 to quit"))
        if (c==0):
          print(p1name,"your final score is",pp1)
          print(p2name,"your final score is",pp2)
          break
      turn=turn+1
play()