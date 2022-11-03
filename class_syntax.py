class Rectangle :
    width = 3
    heigth = 2

    def calculate_area(self):
        return self.width * self.heigth


class Cake :
    flavor = "chocoloate"
    def __init__(self,flavor):
        self.flavor = flavor
    
    def cut_in_parts(self):
        print("Le gateau est coupé en parts")

class ToolBox:
    def __init__(self):
        self.tools=[]
    def add_tools(self,tool):
        self.tools.append(tool)
    def remove_tool(self,tool):
        assert tool in self.tools, f"{tool} is not in currently in toolbox !"
        self.tools.remove(tool)

class Screwdriver:
    def __init__(self, size):
        self.size = size
    def tighten(self,screw):
        screw.tighten()
    def loosen(self, screw):
        screw.loosen

class Hammer:
    def __init__(self, color="red"):
        self.color = color

    def pain(self, color):
        self.color = color

    def hammer_in(self, nail):
        nail.nail_in()

    def remove(self,nail):
        nail.remove()

class Screw:
    MAX_TIGHTNESS = 5
    def __init__(self):
        self.tightness = 0

    def loosen(self):
        if self.tightness > 0:
            self.tightness += -1

    def tighten(self):
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1
    
    def __str__(self):
        return f"Vis avec un serrage de {self.tightness}/{self.MAX_TIGHTNESS}."

class Nail:
    def __init__(self):
        self.in_wall = False

    def nail_in(self):
        self.in_wall = True

    def remove(self):
        self.in_wall = False

    def __str__(self):
        state = "dans le mur" if self.in_wall else "hors du mur"
        return f"Cloud {state}"

toolbox = ToolBox()
screwdriver = Screwdriver(15)
hammer = Hammer("blue")

toolbox.add_tools(screwdriver)
toolbox.add_tools(hammer)

screw = Screw()

print(f"Avant serrage : ")
print(screw)

screwdriver.tighten(screw)

print("Après serrage : ")
print(screw)

nail = Nail()

print(f"Avant serrage : ")
print(nail)

hammer.hammer_in(nail)

print("Après serrage : ")
print(nail)