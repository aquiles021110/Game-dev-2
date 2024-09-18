class student:
    def __init__(self,name,house):
        self.name=name
        self.house=house
        self.age=13
        self.teacher='Guenebaud J'
    def display_details(self):
        print(f'Name is {self.name},\nhouse is {self.house}, \nteacher is {self.teacher},\nAge is {self.age}')
S1=student('Aiach','Matisse')
S2=student('Brise','Picasso')
S3=student('Lerda','Red')
S1.display_details()
S1.name='Farrugia'
print(S1.name)

class fruits:
    def __init__(self,name,colour,shape,taste):
        self.name=name
        self.coulour=colour
        self.shape=shape
        self.taste=taste
    def display(self):
        print(f'The fruit is a(n) {self.name},\nthe coulour is {self.coulour},\nthe shape is {self.shape},\nthe taste is {self.taste}')

apple=fruits('apple','red or green','round','sweet')
orange=fruits('orange','orange','round','tangy')
banana=fruits('banana','yellow','curved','sweet')
banana.coulour='Green'
print(banana.display())



#python inheritance


class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(f'Person name is {self.name}, id is {self.id}.')
class worker(person):
    def __init__(self, name, id,profession,salary):
        person.__init__(self,name,id)
        self.profession=profession
        self.salary=salary
    def display_work(self):
        print(f'Worker is {self.name},{self.id},works as {self.profession} for {self.salary} per year.')
W1=worker('Izard','TB103452B','Teacher','70K')
W1.display_work()    