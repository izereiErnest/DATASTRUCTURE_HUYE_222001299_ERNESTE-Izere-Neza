print("WELCOME TO WONDERWISE")
from collections import deque
class TravelItineraryPlanner:
    def __init__(self):
        self.undostack=[]
        self.travelrequests=deque()
        self.destinations=[]
    def adddestination(self, destinations):
      for destination in destinations:
        self.undostack.append(('remove',destination))
        self.destinations.append(destination.strip())
        print(f"Added Destination: {destination.strip()}")
    def removedestination(self, destinations):
      for destination in destinations:
       if destination.strip() in self.destinations:
          self.undostack.append(('add', destination.strip()))
          self.destinations.remove(destination.strip())
          print(f"Removed Destination: {destination.strip()}")
       else:
          print(f"Destination {destination.strip()} is not found in itinerary") 
    def undo(self,count=1):
      for _ in range(count):
       if self.undostack:
          action, destination=self.undostack.pop()
          if action=='add':
             self.destinations.append(destination)
             print("Added back destination:"  f"  {destination}")  
          elif action=='remove':
             self.destinations.pop(destination)
             print("Removed destination:"  f"  {destination}")
          else:
             print("There are no actions to undo.")
             break
    def addtravelrequests(self, requests):
      for request in requests:
       self.travelrequests.append(request.strip())
       print(f"Added travel request:{request.strip()}")
    def processtravelrequest(self):
       if self.travelrequests:
         while self.travelrequests:
          request=self.travelrequests.popleft()
          print(f"Processing your travel request: {request}")
       else:
         print("No travel requests to process.")
    def  showitinerary(self):
       if self.destinations:
          print("Current itinerary:")
          for i, destination in enumerate(self.destinations, 1):
             print(f"{i}. {destination}")
       else:
            print("Itinerary is empty.")
def menu():
   planner=TravelItineraryPlanner()
   while True:
      print("\n1. Add destination.")
      print("2. Remove destination.")
      print("3. Show itinerary.")
      print("4. Undo last action.")
      print("5. Add travel request.")
      print("6. Process travel requests.")
      print("7. Quit.")
      choice=input("Enter your choice:")
      if choice=='1':
         destinations=input("Enter destinations to add(SEPARATE WITH COMMA!):").split(',')
         planner.adddestination(destinations)
      elif choice=='2':
         destinations=input("Enter destination to remove(SEPARATE WITH COMMA!):").split(',')
         planner.removedestination(destinations)
      elif choice=='3':
         planner.showitinerary()
      elif choice=='4':
         count=int(input("How many actions would you like to undo?"))
         planner.undo(count)
      elif choice=='5':
         requests=input("Enter travel requests(SEPARATE WITH COMMA!):").split(',')
         planner.addtravelrequests(requests)
      elif choice=='6':
         planner.processtravelrequest()
      elif choice=='7':
         print("Exiting the planner.")
         print("Thanks for using our service!!!")
         break
      else:
         print("Invalid choice. please try again.")
menu()
