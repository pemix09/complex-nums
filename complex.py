class ComplexNumber:

    real = 0
    imagine = 0

    def __init__(self, _real, _imagine):
        
        self.real = _real
        self.imagine = _imagine

    def Print(self):

        print("Number: "+ str(self.real) +"+"+ str(self.imagine) + "i")


number = ComplexNumber(12, 2)
number.Print()