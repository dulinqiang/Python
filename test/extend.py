class father():
    __age=0
    def __init__(self,name):
        print("我是父类构造器!")
class son(father):
    def getname(self):
        print(self.name)
q=son("666")
print(q._father__age)