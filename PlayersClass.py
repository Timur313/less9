import time

class Player():
    def __init__(self):
        self.ptype = None
        self.card = None
        self.status = False
        self.name = ""

    def action_remove(self, val):
        if self.ptype == "comp":
            if val in self.card.player_nums:
                #time.sleep(1)
                self.card.remove_num(val)
        elif self.ptype == "man":
            inp = input("Зачеркнуть цифру? (y) ")
            if inp.replace(" ", "") == "y":
                self.card.remove_num(val)
            else:
                pass
        else:
            pass

        if len([v for v in self.card.player_nums if not v is None]) == 0:
            self.status = True
