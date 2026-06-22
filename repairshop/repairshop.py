# Commit forçado do banco de dados
import sqlite3


def init_db():
  conn = sqlite3.connect("repairshop.db")
  cursor = conn.cursor()

  cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      brand TEXT,
      model TEXT,
      year INTEGER,
      color TEXT,
      engine_displacement INTEGER,
      bike_type TEXT,
      services TEXT,
      budget REAL,
      status TEXT
    )
  """)

  conn.commit()
  conn.close()
init_db()


class OrderOfService:
  def __init__(self, motorcycle):
    self.motorcycle = motorcycle
    self.services = []
    self.id = None

  def add_service(self, service_description):
    self.services.append(service_description)
    print(f"The service '{service_description}' added to the {self.motorcycle.model}.")

  def save_to_db(self):
    conn = sqlite3.connect("repairshop.db")
    cursor = conn.cursor()

    bike_type = "Custom" if isinstance(self.motorcycle, CustomMoto) else "Sports"
    services_str = ", ".join(self.services)

    if self.id is None:
      cursor.execute(
        """
        INSERT INTO orders (brand, model, year, color, engine_displacement, bike_type, services, budget, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
          self.motorcycle.brand,
          self.motorcycle.model,
          self.motorcycle.year,
          self.motorcycle.color,
          self.motorcycle.engine_displacement,
          bike_type,
          services_str,
          self.motorcycle.estimated_cost,
          self.motorcycle.service_status,
        ),
      )

      self.id = cursor.lastrowid
      print(f"New order of service was generated in our bank! ID: {self.id}")

    else:
      cursor.execute(
        """
      UPDATE orders 
      SET services = ?, budget = ?, status = ?
      WHERE id = ?
    """,
            (
              services_str,
              self.motorcycle.estimated_cost,
              self.motorcycle.service_status,
              self.id,
            ),
    )

    print(f"Order ID {self.id} has updated succesfully!")

    conn.commit()
    conn.close()


  def show_summary(self):
    print("\n========================================")
    print(f"       SUMMARY - ORDER OF SERVICE       ")
    print("========================================")
    print(f"Motorcycle: {self.motorcycle.brand} {self.motorcycle.model} ({self.motorcycle.color})")
    print(f"Status: {self.motorcycle._service_status}")
    print(f"Total Budget: R$ {self.motorcycle._estimated_cost}")
    print("----------------------------------------")
    print("Services Performed:")
    for service in self.services:
      print(f" - {service}")
    print("========================================\n")


class Motorcycle:
  def __init__(self, brand, year, model, color, engine_displacement):
    self.brand = brand
    self.year = year
    self.model = model
    self.color = color
    self.engine_displacement = engine_displacement

    self._service_status = "In process"
    self._estimated_cost = 0.0

  @property
  def service_status(self):
    return self._service_status

  @property
  def estimated_cost(self):
    return self._estimated_cost

  def define_budget(self, value):
    self._estimated_cost = value
    print(f"The budget for {self.model} update to: R$ {self._estimated_cost}.")

  def change_status(self, new_status):
    self._service_status = new_status
    print(f"Status of {self.model} update to: '{self._service_status}'.")

class CustomMoto(Motorcycle):
  def __init__(self, brand, year, model, color, engine_displacement, type_transmission, handlebar_style,):

    super().__init__(brand, year, model, color, engine_displacement)
    self.type_transmission = type_transmission
    self.handlebar_style = handlebar_style

class SportsMoto(Motorcycle):
  def __init__(self, brand, year, model, color, engine_displacement, has_fairing, top_speed):
    
    super().__init__(brand, year, model, color, engine_displacement)
    self.has_fairing = has_fairing
    self.top_speed = top_speed


current_order = None

while True:
  print("\n--- PRISCA REPAIR & CUSTOMIZATION MENU ---")
  print("1. Register New Motorcycle")
  print("2. Add Service to Order")
  print("3. Show Order Summary")
  print("4. Update Budget")
  print("5. Update Status")
  print("6. Exit")

  option = input("Choose an option: ")

  if option == "1":
    print("\nSelect the type of motorcycle:")
    print("1. Custom Moto")
    print("2. Sports Moto")
    bike_type = input("Choose an option: ")

    brand = input("Enter the brand of the motorcycle: ")
    year = int(input("Type the year of the bike: "))
    model = input("Digit the model: ")
    color = input("Enter the color of the motorcycle: ")
    engine_displacement = int(input("Type the engine displacement: "))

    if bike_type == "1":
      type_transmission = input("Type transmission (chain/belt): ")
      handlebar_style = input("Handlebar style: ")

      user_moto = CustomMoto(brand, year, model, color, engine_displacement, type_transmission, handlebar_style)

    elif bike_type == "2":
      has_fairing = input("Does it have fairing? (yes/no): ")
      top_speed = int(input("Type the top speed (km/h): "))

      user_moto = SportsMoto(brand, year, model, color, engine_displacement, has_fairing, top_speed)

    else:
      print("Invalid bike type! Defaulting to Custom.")
      user_moto = CustomMoto(brand, year, model, color, engine_displacement, "chain", "standard")

    current_order = OrderOfService(user_moto)
    print(f"\n{model} successfully registered in the shop!")

  elif option == "2":
    if current_order is None:
      print("Error! You need to register a motorcycle first (Option 1)!")

    else:
      service_name = input("What maintenance/customization is desired for the motorcycle?: ")
      current_order.add_service(service_name)
      current_order.save_to_db()
      

  elif option == "3":
    if current_order is None:
      print("Error: No active order found. Register a bike first!")

    else:
      current_order.show_summary()
        

  elif option == "4":
    if current_order is None:
      print("Error! Register a bike first!")

    else:
      new_value = float(input("Enter the new budget value (R$): "))
      current_order.motorcycle.define_budget(new_value)
      current_order.save_to_db()

  elif option == "5":
    if current_order is None:
      print("Error! Register a bike first!")

    else:
      print("\nAvailable Statuses: In process, Waiting for parts, Ready to deliver")
      new_status = input("Enter the new status: ")
      current_order.motorcycle.change_status(new_status)
      current_order.save_to_db()

  elif option == "6":
    print("Closing system. See you space cowboy!")
    break

  else:
    print("Invalid option!")
