import random 
class Gameclass:
    counter = 1
    scores = {}
    def __init__(self):
        self.noOfPlayers = int(input('Enter number of players: '))
        self.playgame()
    def playgame(self):
        
        name = input('Enter your name: ')
        key = int(input('Enter a key: '))
        self.luck(name,key)
    def luck(self,name,key):
        if key == 5:
            self.score(name)
        else:
            print('Please enter 5 to try your luck!!!!!!')
            self.playgame()
    def score(self,name):
        number = random.randint(50,100)
        print(f"{name}'s score is: ", number)
        self.scores[name] = number
        if(self.counter < self.noOfPlayers):
            self.counter = self.counter+1
            print('Involve you friend! Its his/her turn')
            self.playgame()
        elif(self.counter == self.noOfPlayers):
            print(self.scores)    
            
                            

player = Gameclass()