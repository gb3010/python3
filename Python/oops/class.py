class Shape:
    type = 'polygon'
    def __init__(self,n,s):
        self.name = n
        self.sides = s
        
    def printsides(self):
        print("No of sides is in {} is {}".format(self.name,self.sides))
        

square = Shape('square',4);
square.printsides();
