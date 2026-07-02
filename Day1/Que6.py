'''
H3) The GPS Navigation System (Backtracking)
You're building a GPS app like Google Maps for a hiking trail. The hiker moves through checkpoints. If they take a wrong tum, they hit "Go Back" to return to the previous checkpoint. But once they go back, they can also "Go Forward" if they change their mind again just like a browser's back/forward buttons
Operations:
visit(place)-move to a new place
back()- go to previous place
forward-go forward if available
'''


class GPS:
    def __init__(self):
        self.back=[]
        self.forward=[]
    def visit(self,place):
        self.back.append(place)
    def go_back(self):
        if len(self.back) > 1:
            self.forward.append(self.back.pop())
        else:
            print("Cannot go back")

    def go_forward(self):
        if self.forward:
            self.back.append(self.forward.pop())
        else:
            print("Cannot go forward")

    def current_place(self):
        print("Current:", self.back[-1])



gps = GPS()

gps.visit("Home")
gps.visit("A")
gps.visit("B")
gps.visit("C")

gps.current_place()   

gps.go_back()
gps.current_place()   

gps.go_back()
gps.current_place()  

gps.go_forward()
gps.current_place()  