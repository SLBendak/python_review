class Car():
    def __init__(self, color, year, make):
        self.color = color 
        self.year = year
        self.make = make

        

    def paint_job(self, the_color):
        self.color = the_color

    def year(self, the_year):
        self.year = the_year
    
    def make(self, the_make):
        self.make = the_make

    
the_car = Car("purple", "2013", "Kia")
the_car.paint_job("blue")
print("I have a {} {}.".format(the_car.color, the_car.make))
    
