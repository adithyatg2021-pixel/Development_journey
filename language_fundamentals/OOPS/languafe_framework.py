class Language:
    def __init__(self,name):
        self.lang_name = name
    def display(self):
        print("Name of language:",self.lang_name)

class Framework(Language):
    def __init__(self,fname,lname):
        super().__init__(lname)
        self.frame_name = fname
    def display(self):
        super().display()
        print("Name of framework:",self.frame_name)

framework_instance1 = Framework("Django","Python")
framework_instance1.display()
framework_instance2 = Framework("Express","Javascript")
framework_instance2.display()
