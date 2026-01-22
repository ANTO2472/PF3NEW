class MultiRobot:
    marque = "FANUC"

    def __init__(self, id=1):
        self.id = id
        self.state_OK = True
        self.nb_alarme = 0
        self.pos_Tool = [0, 0, 0]

        def MoveHome(self):
        self.pos_Tool = [10, 10, 500]

    def MovePick(self):
        self.pos_Tool = [100, 30, 120]

    def MovePlace(self):
        self.pos_Tool = [100, 150, 230]

    def RaiseDefault(self):
        self.state_OK = False
        self.nb_alarme = self.nb_alarme + 1

    def ClearDefault(self):
        self.state_OK = True

def__init__(self, id=1): #methodespeciale'__'=>constructeur
"constructeur passer l'identifiant (entier [1,n])"
self.id=id# attribut d'instance
self.state_ok=True
self.nb_alarme = 0 
self.pos_Tool =[0,0,0]