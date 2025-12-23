import turtle
import time

# 3.1 Define Disk class
class Disk:
    def __init__(self, name="", xpos=0, ypos=0, thickness=20, length=100):
        self.pname = name
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thickness
        self.plength = length
    
    def showdisk(self):
        """Display the disk using turtle module"""
        turtle.penup()
        turtle.goto(self.pxpos - self.plength/2, self.pypos)
        turtle.pendown()
        turtle.setheading(0)
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(self.plength)
            turtle.left(90)
            turtle.forward(self.pthick)
            turtle.left(90)
        turtle.end_fill()
    
    def cleardisk(self):
        """Clear the disk from its current position"""
        turtle.penup()
        turtle.goto(self.pxpos - self.plength/2, self.pypos)
        turtle.pendown()
        turtle.setheading(0)
        turtle.color("black")
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(self.plength)
            turtle.left(90)
            turtle.forward(self.pthick)
            turtle.left(90)
        turtle.end_fill()
        turtle.color("black")
    
    def moveto(self, xpos, ypos):
        """Move the disk to new position"""
        self.cleardisk()
        self.pxpos = xpos
        self.pypos = ypos
        self.showdisk()


# 3.2 Define Pole class
# class Pole:
#     def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
#         self.pname = name
#         self.stack = []
#         self.toppos = 0
#         self.pxpos = xpos
#         self.pypos = ypos
#         self.pthick = thick
#         self.plength = length
    
#     def showpole(self):
#         """Display only the pole (using turtle module)"""
#         turtle.penup()
#         turtle.goto(self.pxpos, self.pypos)
#         turtle.pendown()
#         turtle.setheading(90)
#         turtle.forward(self.plength)
    
#     def pushdisk(self, disk):
#         """Move the disk from top of another pole and push it on top of stacked disks"""
#         # Update disk position
#         disk.pxpos = self.pxpos
#         disk.pypos = self.pypos + self.toppos * disk.pthick
        
#         # Add to stack
#         self.stack.append(disk)
#         self.toppos += 1
        
#         # Draw the disk
#         disk.showdisk()
    
#     def popdisk(self):
#         """Move the top disk out of the pole and leave it above the pole"""
#         if len(self.stack) == 0:
#             return None
        
#         disk = self.stack.pop()
#         self.toppos -= 1
        
#         # Clear the disk from current position
#         disk.cleardisk()
        
#         return disk


# 3.3 Define Hanoi class
# class Hanoi:
#     def __init__(self, n=3, start="A", workspace="B", destination="C"):
#         # Initialize turtle
#         turtle.speed(50)
#         turtle.hideturtle()
#         turtle.title("Tower of Hanoi")
        
#         # Create three poles
#         self.startp = Pole(start, -200, 0, 10, 200)
#         self.workspacep = Pole(workspace, 0, 0, 10, 200)
#         self.destinationp = Pole(destination, 200, 0, 10, 200)
        
#         # Draw the poles
#         self.startp.showpole()
#         self.workspacep.showpole()
#         self.destinationp.showpole()
        
#         # Add labels
#         turtle.penup()
#         turtle.goto(-200, -30)
#         turtle.write(start, align="center", font=("Arial", 14, "bold"))
#         turtle.goto(0, -30)
#         turtle.write(workspace, align="center", font=("Arial", 14, "bold"))
#         turtle.goto(200, -30)
#         turtle.write(destination, align="center", font=("Arial", 14, "bold"))
        
#         # Create and place disks on start pole
#         self.n = n
#         for i in range(n):
#             disk = Disk("d"+str(i), 0, i*25, 20, (n-i)*30 + 40)
#             # Set color based on disk size
#             colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
#             turtle.color(colors[i % len(colors)])
#             self.startp.pushdisk(disk)
        
#         turtle.color("black")
#         turtle.speed(50)  # Slow down for animation
    
#     def move_disk(self, start, destination):
#         """Move one disk from start pole to destination pole"""
#         disk = start.popdisk()
#         if disk:
#             time.sleep(0.3)
#             destination.pushdisk(disk)
#             time.sleep(0.3)
    
#     def move_tower(self, n, s, d, w):
#         """Recursively move n disks from source to destination using workspace"""
#         if n == 1:
#             self.move_disk(s, d)
#         else:
#             self.move_tower(n-1, s, w, d)  # Move n-1 disks to workspace
#             self.move_disk(s, d)             # Move largest disk to destination
#             self.move_tower(n-1, w, d, s)  # Move n-1 disks from workspace to destination
    
#     def solve(self):
#         """Solve the Tower of Hanoi puzzle"""
#         print(f"Solving Tower of Hanoi with {self.n} disks...")
#         print(f"Moving from {self.startp.pname} to {self.destinationp.pname} using {self.workspacep.pname}")
#         self.move_tower(self.n, self.startp, self.destinationp, self.workspacep)
#         print("Done!")


# Main program
if __name__ == "__main__":
    # You can change the number of disks here (try 3, 4, or 5)
    n = 3
    h = Hanoi(n)
    h.solve()
    
    # Keep window open
    turtle.done()