'''
h2) Toll Plaza Simulation (Circular Queue)
A toll plaza has a fixed capacity of 5 vehicles. If full, new vehicles must wait Implement a Circular Queue to simulate this, since it reuses empty slots without wasting memory.
'''

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, vehicle):
        # Queue Full
        if (self.rear + 1) % self.size == self.front:
            print("Toll Plaza Full! Vehicle", vehicle, "must wait.")
            return

        # First Element
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = vehicle
        print(vehicle, "entered the toll plaza.")

    def dequeue(self):
        # Queue Empty
        if self.front == -1:
            print("No vehicles at the toll plaza.")
            return

        vehicle = self.queue[self.front]
        print(vehicle, "has crossed the toll.")

        # Only one element
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        print("Vehicles in Toll Plaza:")

        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


# Driver Code
cq = CircularQueue(5)

cq.enqueue("Car1")
cq.enqueue("Car2")
cq.enqueue("Bus1")
cq.enqueue("Truck1")
cq.enqueue("Car3")

cq.display()

cq.enqueue("Bus2")   # Queue Full

cq.dequeue()
cq.dequeue()

cq.display()

cq.enqueue("Bus2")
cq.enqueue("Car4")

cq.display()