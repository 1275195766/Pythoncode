class people:
    #name="wangwu"
    def eat(self):
        print "吃吃吃。。。。"
class student(people):
    def write(self):
        print"我会写字"
    def eat(self):
        print"我很能吃"
s=student()
s.name="wangwu"
s.__class__.name="lisi"
print s.__dict__
#s.eat()
print s.__class__.__dict__
