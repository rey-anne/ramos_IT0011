class Car:
    """
    Represents a car with ID, name, description, and price.
    """

    def __init__(self, car_id, name, description, price):
        """
        Initializes a Car object.

        Args:
            car_id (int): The unique ID of the car.
            name (str): The name of the car.
            description (str): A description of the car.
            price (float): The price of the car.

        Raises:
            TypeError: If car_id is not an integer or price is not a float.
            ValueError: If car_id or price is negative, or if name or description are empty.
        """
        if not isinstance(car_id, int):
            raise TypeError("Car ID must be an integer.")
        if car_id < 0:
            raise ValueError("Car ID cannot be negative.")
        if not isinstance(name, str) or not name:
            raise ValueError("Car name cannot be empty.")
        if not isinstance(description, str) or not description:
            raise ValueError("Car description cannot be empty.")
        if not isinstance(price, (int, float)):
            raise TypeError("Car price must be a number.")
        if price < 0:
            raise ValueError("Car price cannot be negative.")

        self.car_id = car_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return (
            f"Car ID: {self.car_id}\n"
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Price: ₱{self.price:,.2f}"
        )

class CarManager:
    """
    Manages a collection of Car objects.
    """

    def __init__(self):
        self.cars = {}

    def add_car(self, car):
        """
        Adds a car to the collection.

        Args:
            car (Car): The Car object to add.

        Raises:
            ValueError: If a car with the same ID already exists.
        """
        if car.car_id in self.cars:
            raise ValueError(f"Car with ID {car.car_id} already exists.")
        self.cars[car.car_id] = car

    def get_car(self, car_id):
        """
        Retrieves a car by its ID.

        Args:
            car_id (int): The ID of the car to retrieve.

        Returns:
            Car: The Car object, or None if not found.
        """
        return self.cars.get(car_id)

    def update_car(self, car_id, name=None, description=None, price=None):
        """
        Updates a car's information.

        Args:
            car_id (int): The ID of the car to update.
            name (str, optional): The new name of the car.
            description (str, optional): The new description of the car.
            price (float, optional): The new price of the car.

        Raises:
            ValueError: If the car with the given ID does not exist.
            TypeError: If the provided data types are incorrect.
        """
        car = self.get_car(car_id)
        if not car:
            raise ValueError(f"Car with ID {car_id} not found.")

        if name is not None:
            if not isinstance(name, str) or not name:
                raise ValueError("Car name cannot be empty.")
            car.name = name

        if description is not None:
            if not isinstance(description, str) or not description:
                raise ValueError("Car description cannot be empty.")
            car.description = description

        if price is not None:
            if not isinstance(price, (int, float)):
                raise TypeError("Car price must be a number.")
            if price < 0:
                raise ValueError("Car price cannot be negative.")
            car.price = price

    def delete_car(self, car_id):
        """
        Deletes a car by its ID.

        Args:
            car_id (int): The ID of the car to delete.

        Raises:
            ValueError: If the car with the given ID does not exist.
        """
        if car_id not in self.cars:
            raise ValueError(f"Car with ID {car_id} not found.")
        del self.cars[car_id]

    def list_cars(self):
        """
        Lists all cars in the collection.
        """
        return list(self.cars.values())

#executionm
car_manager = CarManager()

try:
    car1 = Car(202311829, "Toyota Vios", "The Philippines Best-selling Sedan.", 906000.00)
    car2 = Car(202311830, "Honda Civic", "A small sedan with high fuel economy and a refined design.", 1600000.00)
    car3 = Car(202311831, "Toyota Fortuner", "is a mid-size SUV", 1700000.00) 
    car_manager.add_car(car1)
    car_manager.add_car(car2)
    car_manager.add_car(car3) 

    print("")
    print("--------------------")
    print("")
    print("Car Inventory Manager:")
    print("")
    print("--------------------")
    print("")

    for car in car_manager.list_cars():
        print(f"Car ID: {car.car_id}")
        print(f"Name: {car.name}")
        print(f"Description: {car.description}")
        print(f"Price: ₱{car.price:,.2f}")
        print("-" * 20)

#Car update po here.
    car_manager.update_car(202311831, description="Tough and capable, the Fortuner conquers any terrain.", price=1775000.00)
    print("\nUpdated Car:")
    print(car_manager.get_car(202311831))
    print("-" * 20)

#Car will be deleted in this part, will show after run po
    car_manager.delete_car(202311830)
    print("\nCars after deletion:")
    for car in car_manager.list_cars():
        print(f"Car ID: {car.car_id}")
        print(f"Name: {car.name}")
        print(f"Description: {car.description}")
        print(f"Price: ₱{car.price:,.2f}")
        print("-" * 20)

except (TypeError, ValueError) as e:
    print(f"Error: {e}")

try:
    car_manager.add_car(Car(1,"duplicate car","description",1000))
except ValueError as e:
    print(f"Error: {e}")