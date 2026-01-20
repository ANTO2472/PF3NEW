class Robot:
    marque = "FANUC"

    def __init__(self):
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

    def GetStatus(self):
        if self.state_OK == True:
            status_text = "OK"
        else:
            status_text = "NOK"

        # Affichage avec .format()
        print("{} Status {} ({}) Position X={} Y={} Z={}".format(
            self.marque,
            status_text,
            self.nb_alarme,
            self.pos_Tool[0],
            self.pos_Tool[1],
            self.pos_Tool[2]
        ))

# ==========================================
# JEU DE TEST (Copie exacte de l'énoncé)
# ==========================================

print(Robot.marque) # utilisation attribut de class sans instanciation

rob1 = Robot() # premiere instance de robot
rob2 = Robot() # seconde instance de robot

# Ordres sur robot 1
rob1.GetStatus()
rob1.MoveHome()
rob1.RaiseDefault()
rob1.GetStatus()
rob1.ClearDefault()
rob1.GetStatus()

# Ordres sur robot 2
rob2.GetStatus()
rob2.RaiseDefault()
rob2.GetStatus()