class vehicle():
    def start(self):
        print("vehicle started")
class car(vehicle):
    def start(self):
        #super().start()
        print("car started!!")
res = car()
res.start()
        
