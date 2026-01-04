class Family():
    def __init__(self,name,age,height,haircolor,relation):
        self.name=name
        self.age=age
        self.height=height
        self.haircolor=haircolor
        self.relation=relation

    def eating(self):
        print('Lets have dinner together.')
    def travel(self):
        print('Lets travel together.')
    def reading(self):
        print('Lets read together.')
    def display(self):

        print('The name of the object is',self.name)
        print('The age of the object is',self.age)
        print('The height of the object is',self.height)
        print('The haircolor of the object is',self.haircolor)
        print('The relation of the object is',self.relation)

object1=Family('Gracy','12','160cm','dark brown','daughter')
object2=Family('Elina','16','170cm','dark brown','daughter')
object3=Family('Roseleen','43','163cm','black with purple bits','mother')
object4=Family('Prasanta','47','180cm','black','father')

print(object1.age)
print(object2.height)
print(object3.haircolor)
print(object4.relation)

object1.display()