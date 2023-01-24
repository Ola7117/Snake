class Score:

    def __init__(self):
        self.value = 0
        self.highscore = self.load_score() 

    def save_score(self):
        with open("score.txt", "w") as f:
            f.write(str(self.value))
            
    def load_score(self):
        with open("score.txt", "r") as f:
            return int(f.read())
    
    def update_highscore(self):
        if self.value > self.highscore:
            self.save_score()
            self.highscore = self.load_score()