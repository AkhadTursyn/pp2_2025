class siclass:
    def getString(self):
        self.text = input()
    
    def printString(self):
        print(self.text.upper())


obj = siclass()
obj.getString()
obj.printString()
