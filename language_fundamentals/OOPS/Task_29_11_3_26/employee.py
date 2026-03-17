class Employee:
    def work(self): pass

class Manager(Employee):
    def work(self):
        print("Team management")

class Developer(Employee):
    def work(self):
        print("Software development")

manager_instance = Manager()
manager_instance.work()
developer_inst = Developer()
developer_inst.work()