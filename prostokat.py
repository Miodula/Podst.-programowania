class Rectangle:
    def __init__(self, width, height):
        """
        Ustawia wartości długości i szerokości
        width: szerokość
        height: długość 
        """
        self.resize(width, height)

    def __str__(self) -> str:
        """
        Metoda wypisuje podane wartości, pole i obwód  
        """
        return (f"Szerokość: {self.width}, Długość: {self.height}, Pole powierzchni: {self.area()}, Obwód: {self.perimeter()}")
    
    def area(self) -> float:
        """
        Metoda obliczająca pole powierzchni prostokąta 
        P = width * height 
        """
        return (f"Pole powierzchni: ({self.width} * {self.height}) = {self.width * self.height}")
    
    def perimeter(self) -> float:
        """
        Metoda obliczająca obwód prostokąta 
        Obw = 2*width+2*height
        """
        return (f"Obwód wynosi: {(self.width*2)+(self.height*2)}")
    
    def resize(self, width, height) :
        """
        Metoda zmieniająca rozmiar prostokąta
        """ 
        self.width = width
        self.height = height 
       
pros = Rectangle(2,4)
print(pros.area())
print(pros.perimeter())
print(pros.__str__())