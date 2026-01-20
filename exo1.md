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
        self.nb_alarme += 1

    def ClearDefault(self):
        self.state_OK = True

    def GetStatus(self):
        if self.state_OK:
            status_text = "OK"
        else:
            status_text = "NOK"

        # Affichage selon le format : FANUC Status OK (0) Position X=...
        print("{} Status {} ({}) Position X={} Y={} Z={}".format(
            self.marque,
            status_text,
            self.nb_alarme,
            self.pos_Tool[0],
            self.pos_Tool[1],
            self.pos_Tool[2]
        ))

if __name__ == "__main__":
    print(Robot.marque)

    rob1 = Robot()
    rob2 = Robot()

    rob1.GetStatus()
    rob1.MoveHome()
    rob1.RaiseDefault()
    rob1.GetStatus()
    rob1.ClearDefault()
    rob1.GetStatus()

    rob2.GetStatus()
    rob2.RaiseDefault()
    rob2.GetStatus()