class Game:
    def rollDice(self, die):
        diceBag = [4,6,8,10,12,20]
        if die in diceBag:
            roll = random.randrange(die)
            message = {'roll': roll}
        else:
            message = { 'error' : 'You do not have that die in your Dice Bag...'}
        return message