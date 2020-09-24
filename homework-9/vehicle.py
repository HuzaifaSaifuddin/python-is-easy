class Vehicle:
  def __init__(self, Make, Model, Year, Weight, NeedsMaintenance = False, TripsSinceMaintenance = 0):
    self.Make = Make
    self.Model = Model
    self.Year = Year
    self.Weight = Weight
    self.NeedsMaintenance = NeedsMaintenance
    self.TripsSinceMaintenance = TripsSinceMaintenance

  def Repair(self):
    self.TripsSinceMaintenance = 0
    self.NeedsMaintenance = False
    
class Car(Vehicle):
  def __init__(self, Make, Model, Year, Weight, isDriving):
    Vehicle.__init__(self, Make, Model, Year, Weight)
    self.isDriving = isDriving

  def Drive(self):
    self.isDriving = True

  def Stop(self):
    self.isDriving = False
    self.TripsSinceMaintenance += 1

    if self.TripsSinceMaintenance == 100:
      self.NeedsMaintenance = True

class Plane(Vehicle):
  def __init__(self, Make, Model, Year, Weight, isFlying):
    Vehicle.__init__(self, Make, Model, Year, Weight)
    self.isFlying = isFlying

  def Fly(self):
    if self.NeedsMaintenance == False:
      self.isFlying = True
      return "Plane is Flying"
    else:
      return "Plane cant fly until its repaired."

  def Land(self):
    self.isFlying = False
    self.TripsSinceMaintenance += 1

    if self.TripsSinceMaintenance == 100:
      self.NeedsMaintenance = True


# For CARS
def DriveStop(Car, Times):
  for num in range(Times):
    Car.Drive()

    Car.Stop()


Verna = Car("Hyundai", "Sx", 2018, "2000 KG", False)
DriveStop(Verna, 100)

Alto = Car("Maruti", "AC", 2010, "1600 KG", False)
DriveStop(Alto, 50)

Xarr = Car("Narr", "XN", 2014, "1300 KG", False)
DriveStop(Xarr, 75)

print("VERNA")
print("Make : " + str(Verna.Make))
print("Model : " + str(Verna.Model))
print("Year : " + str(Verna.Year))
print("Weight : " + str(Verna.Weight))
print("NeedsMaintenance : " + str(Verna.NeedsMaintenance))
print("TripsSinceMaintenance : " + str(Verna.TripsSinceMaintenance))
print("------------------------")
print("ALTO")
print("Make : " + str(Alto.Make))
print("Model : " + str(Alto.Model))
print("Year : " + str(Alto.Year))
print("Weight : " + str(Alto.Weight))
print("NeedsMaintenance : " + str(Alto.NeedsMaintenance))
print("TripsSinceMaintenance : " + str(Alto.TripsSinceMaintenance))
print("------------------------")
print("XARR")
print("Make : " + str(Xarr.Make))
print("Model : " + str(Xarr.Model))
print("Year : " + str(Xarr.Year))
print("Weight : " + str(Xarr.Weight))
print("NeedsMaintenance : " + str(Xarr.NeedsMaintenance))
print("TripsSinceMaintenance : " + str(Xarr.TripsSinceMaintenance))
print("------------------------")
print("------------------------")

# For PLANES
Zapa = Plane("SpiceJet", "A300", 2019, "41000 KG", False)
for num in range(99):
  Zapa.Fly()

  Zapa.Land()

print("ZAPA")
print(Zapa.Fly())
Zapa.Land() # 100
print(Zapa.Fly())