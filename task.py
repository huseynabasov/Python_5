class Hedef:

    def __init__(self):
        self.ededler = []

    def eded_elaveEt(self, eded):
        self.ededler.append(eded)

    def eded_tap(self, hedef):
        newlist = []
        for i in range(len(self.ededler)):
            for a in range(i + 1, len(self.ededler)):
                if self.ededler[i] + self.ededler[a] == hedef:
                    newlist.append((self.ededler[i], self.ededler[a])) 
        if newlist:
            newlist
        else:
            return -1    
        return newlist


newlist = Hedef()
newlist.eded_elaveEt(1) 
newlist.eded_elaveEt(2) 
newlist.eded_elaveEt(3) 
newlist.eded_elaveEt(4) 
newlist.eded_elaveEt(5) 
newlist.eded_elaveEt(6) 
newlist.eded_elaveEt(7) 
newlist.eded_elaveEt(8) 
newlist.eded_elaveEt(9) 
hedef_eded = 10
netice = newlist.eded_tap(hedef_eded)

print(
    f"Hedef qoyulan eded - {hedef_eded} : Hedef qoyulmus ededin cemini beraber olan kombinasiya {netice}"
)
