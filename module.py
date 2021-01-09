class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def talk(self,text):
        print(f"{self.name.title()} said {text}.")
    def ask(self,text):
        print(f"{self.name.title()} asked {text}.")