class Transportation(object):
   """Abstract base class"""

   def __init__(self, start, end, distance):
      if self.__class__ == Transportation:
         raise NotImplementedError
      self.start = start
      self.end = end
      self.distance = distance

   def find_cost(self):
      """Abstract method; derived classes must override"""
      raise NotImplementedError


class Walk(Transportation):
   """Walking has no cost for any distance"""

   def __init__(self, start, end, distance):
      Transportation.__init__(self, start, end, distance)

   def find_cost(self):
      return 0


class Taxi(Transportation):
   """Taxi charges 40 Bahts per kilometer"""

   def __init__(self, start, end, distance):
      Transportation.__init__(self, start, end, distance)

   def find_cost(self):
      return 40 * self.distance


class Train(Transportation):
   """Train costs 5 Bahts per station"""

   def __init__(self, start, end, distance, stations):
      Transportation.__init__(self, start, end, distance)
      self.stations = stations

   def find_cost(self):
      return 5 * self.stations


# Team Member 3

travel_cost = 0

trip = [Walk("KMITL", "KMITL SCB Bank", 0.6),
        Taxi("KMITL SCB Bank", "Ladkrabang Station", 5),
        Train("Ladkrabang Station", "Payathai Station", 40, 6),
        Taxi("Payathai Station", "The British Council", 3)]

for travel in trip:
   travel_cost += travel.find_cost()

print("Total travel cost:", travel_cost, "Bahts")

# Display detailed breakdown
# print("\nTrip Breakdown:")
# print("-" * 60)
# for i, travel in enumerate(trip, 1):
#    print(f"{i}. {travel.__class__.__name__:10} | {travel.start:25} -> {travel.end:25}")
#    print(f"   Distance: {travel.distance} km | Cost: {travel.find_cost()} Bahts")
# print("-" * 60)
# print(f"Total Cost: {travel_cost} Bahts")