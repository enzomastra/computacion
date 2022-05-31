names=[]
ages=[]
directions=[]
class Client:
    def __init__ (self,name,age,direction):
        self.name=name
        self.age=age
        self.direction=direction
    def add(self):
        names.append(self.name)
        ages.append(self.age)
        directions.append(self.direction)
    def view(self):
        for i in range(len(names)):
            print("name: ",names[i])
            print("age: ",ages[i])
            print("direction: ",directions[i])
            print("------")