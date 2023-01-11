class Score:
    def __init__(self):
        self.value = 0
    def save_score(self):
        with open("score.txt","w") as f:
            f.write(str(self.value))
    def load_score(self):
        with open("score.txt","r") as f:
            self.value = int(f.read())