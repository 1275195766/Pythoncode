class people:
    #name="wangwu"
    def eat(self):
        print "�ԳԳԡ�������"
class student(people):
    def write(self):
        print"�һ�д��"
    def eat(self):
        print"�Һ��ܳ�"
s=student()
s.name="wangwu"
s.__class__.name="lisi"
print s.__dict__
#s.eat()
print s.__class__.__dict__
