class Cars():
    """Class to create cars"""
    def __init__(self, brand, model, year):
        """Initiate cars"""
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 80000

    def show_car(self):
        """Print all parameters of car"""
        description = (" Brand is: " + self.brand + " Model is: " + self.model + " Year is: " + str(self.year) + " Mileage is: " + str(self.mileage))


