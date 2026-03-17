"""
Self is the keyword used for point current instance
memory location is allocated for a class only if object is created

"""


class Animals:
    colour:str
    size:str
    sound:str

    def walk(self):
        print("Animal walk method.")

    def jump(self):
        print("Animal jump method.")

cat_instance = Animals()

cat_instance.walk()