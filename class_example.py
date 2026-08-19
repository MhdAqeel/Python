class Car:
    color = "blue"
    speed = 50      #default values
    type ="sport"

    def __init__(self):     #dummy constructor
        pass

    def __init__(self,color,speed,type):         #constructor
        self.color = color
        self.speed = speed
        self.type = type

    def getColor(self):
        return self.color

audi = Car("blue", 60 , "sedan")

print(audi.getColor())
audi.speed = 100
print(audi.speed)