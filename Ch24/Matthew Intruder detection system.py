StateList = ["System Inactive","System Active","Alert Mode","Alarm Bell Ringing"]
ActionList = ["Press Start","Enter PIN","Activate Sensor","2 Minute Passed","Quit"]

def ShowAction():
    print("Choose your action: ")
    for i in range (len(ActionList)):
        print(i+1,": ",ActionList[i])

class system():
    def __init__(self):
        self.state = StateList[0]
        self.action = ""
        self.time = 0
    def displayStatus(self):
        print("Current State: ",self.state, "Time: ",self.time)
    def action1(self):
        if self.state == StateList[0]:
            self.state = StateList[1]
    def action2(self):
        if self.state != StateList[0]:
            self.state = StateList[0]
    def action3(self):
        if self.state == StateList[1]:
            self.state = StateList[2]
    def action4(self):
        if self.state == StateList[2]:
            self.state = StateList[3]
    def main(self):
        print("Intruder Detection System")
        while True:
            ShowAction()
            self.action = input("Enter your action: ")
            print(self.action)
            if self.action == "1":
                print("Start button pushed")
                self.action1()
            elif self.action == "2":
                self.action2()
                print("PIN Entered")
            elif self.action == "3":
                self.action3()
                print("Sensor Activated")
            elif self.action == "4":
                self.action4()
                print("Alarm Bell Ringing")
            elif self.action =="5":
                break
            self.time += 1
            self.displayStatus()

s = system()
s.main()
