
class Circle():

    # This is a Class Object Attribute
    # Notice how it is not under __init__
    pi = 3.14
    # Circle get instantiated with a radius (default is 1) __init__ is a spical method - creating atributes
    def __init__(self, input_radius=2):
        self.radius = input_radius
    # Area method calculates the area. Note the use of self.
    def area(self):
        return self.radius * self.radius * Circle.pi
    # Method for resetting Radius
    def setRadius(self, radius):
        self.radius = radius
    # Method for getting radius (Same as just calling .radius)
    def getRadius(self):
        return self.radius

c = Circle()
#c.setRadius(2)
print (c.radius)
print('Radius is: ')
print(c.getRadius())
print('Area is: ')
print(c.area())
print ('hi')


# add
2+1




'''
import json
import pandas as pd
with open('data.json', 'r') as f:
     data = json.load(f)
ls =(data['action'])
df= pd.DataFrame(ls)
print(df)
df.to_csv('instru2.csv', index = False, sep=',', encoding='utf-8')
'''