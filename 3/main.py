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
        current_color = turtle.pencolor()
        turtle.pencolor("white")
        turtle.fillcolor("white")
        
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
        
        turtle.pencolor(current_color)
        turtle.fillcolor(current_color)
    
    def moveto(self, xpos, ypos):
        """Move the disk to new position"""
        self.cleardisk()
        self.pxpos = xpos
        self.pypos = ypos
        self.showdisk()


# 3.2 Define Pole class
class Pole:
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length
    
    def showpole(self):
        """Display only the pole (using turtle module)"""
        turtle.penup()
        turtle.goto(self.pxpos, self.pypos)
        turtle.pendown()
        turtle.setheading(90)
        turtle.pensize(3)
        turtle.forward(self.plength)
        turtle.pensize(1)
    
    def pushdisk(self, disk):
        """Move the disk from top of another pole and push it on top of stacked disks"""
        # Update disk position
        disk.pxpos = self.pxpos
        disk.pypos = self.pypos + self.toppos * disk.pthick
        
        # Add to stack
        self.stack.append(disk)
        self.toppos += 1
        
        # Draw the disk
        disk.showdisk()
    
    def popdisk(self):
        """Move the top disk out of the pole and leave it above the pole"""
        if len(self.stack) == 0:
            return None
        
        disk = self.stack.pop()
        self.toppos -= 1
        
        # Clear the disk from current position
        disk.cleardisk()
        
        # Redraw pole to ensure it's visible
        current_color = turtle.pencolor()
        turtle.pencolor("black")
        turtle.penup()
        turtle.goto(self.pxpos, self.pypos)
        turtle.pendown()
        turtle.setheading(90)
        turtle.pensize(3)
        turtle.forward(self.plength)
        turtle.pensize(1)
        turtle.pencolor(current_color)
        
        return disk


class Hanoi:
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        # Initialize turtle
        turtle.setup(800, 600)
        turtle.speed(10)
        turtle.hideturtle()
        turtle.title("Tower of Hanoi")
        turtle.bgcolor("white")
        
        # Create three poles
        self.startp = Pole(start, -200, -150, 10, 200)
        self.workspacep = Pole(workspace, 0, -150, 10, 200)
        self.destinationp = Pole(destination, 200, -150, 10, 200)
        
        # Draw base platforms
        turtle.pencolor("black")
        turtle.pensize(5)
        for pole in [self.startp, self.workspacep, self.destinationp]:
            turtle.penup()
            turtle.goto(pole.pxpos - 80, pole.pypos)
            turtle.pendown()
            turtle.forward(160)
        turtle.pensize(1)
        
        # Draw the poles
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        
        # Add labels
        turtle.penup()
        turtle.goto(-200, -180)
        turtle.write(start, align="center", font=("Arial", 14, "bold"))
        turtle.goto(0, -180)
        turtle.write(workspace, align="center", font=("Arial", 14, "bold"))
        turtle.goto(200, -180)
        turtle.write(destination, align="center", font=("Arial", 14, "bold"))
        
        # Create and place disks on start pole
        self.n = n
        colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
        for i in range(n):
            disk = Disk("d"+str(i), 0, 0, 20, (n-i)*30 + 40)
            # Set color based on disk size
            turtle.pencolor(colors[i % len(colors)])
            turtle.fillcolor(colors[i % len(colors)])
            self.startp.pushdisk(disk)
        
        turtle.pencolor("black")
        turtle.fillcolor("black")
        turtle.speed(10)  # Slow down for animation
    
    def move_disk(self, start, destination):
        """Move one disk from start pole to destination pole"""
        disk = start.popdisk()
        if disk:
            time.sleep(0.2)
            
            # Get the disk's current color
            colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
            disk_index = int(disk.pname[1])
            turtle.pencolor(colors[disk_index % len(colors)])
            turtle.fillcolor(colors[disk_index % len(colors)])
            
            destination.pushdisk(disk)
            time.sleep(0.2)
    
    def move_tower(self, n, s, d, w):
        """Recursively move n disks from source to destination using workspace"""
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n-1, s, w, d)  # Move n-1 disks to workspace
            self.move_disk(s, d)             # Move largest disk to destination
            self.move_tower(n-1, w, d, s)  # Move n-1 disks from workspace to destination
    
    def solve(self):
        """Solve the Tower of Hanoi puzzle"""
        print(f"Solving Tower of Hanoi with {self.n} disks...")
        print(f"Moving from {self.startp.pname} to {self.destinationp.pname} using {self.workspacep.pname}")
        self.move_tower(self.n, self.startp, self.destinationp, self.workspacep)
        print("Done!")
        
        # Display completion message
        turtle.penup()
        turtle.goto(0, 100)
        turtle.pencolor("green")


# Main program
if __name__ == "__main__":
    # You can change the number of disks here (try 3, 4, or 5)
    n = 3
    h = Hanoi(n)
    h.solve()
    
    # Keep window open
    turtle.done()