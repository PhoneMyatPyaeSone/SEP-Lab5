import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("Simple GitHub Drawing")
        self.rabbit = QPixmap("images/rabbit.png")
    
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        # Original drawing - polygon and pie
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint(70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
        ])
        
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)
        
        p.drawPolygon([
            QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),
        ])
        
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()


# Team Member 1
class Simple_drawing_window1(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("Drawing Window 1 - Stars and Circles")
        self.rabbit = QPixmap("images/rabbit.png")
    
    def draw_star(self, p, center_x, center_y, size):
        """Draw a 5-pointed star"""
        import math
        points = []
        for i in range(10):
            angle = math.pi * 2 * i / 10 - math.pi / 2
            if i % 2 == 0:
                r = size
            else:
                r = size * 0.4
            x = center_x + int(r * math.cos(angle))
            y = center_y + int(r * math.sin(angle))
            points.append(QPoint(x, y))
        p.drawPolygon(points)
    
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint(70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
        ])
        
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)
        
        p.drawPolygon([
            QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),
        ])
        
        p.setPen(QPen(QColor(0, 100, 200), 2))
        p.setBrush(QColor(100, 200, 255, 150))
        p.drawEllipse(250, 50, 80, 80)
        p.drawEllipse(350, 70, 60, 60)
        p.drawEllipse(300, 130, 70, 70)
        
        p.setPen(QPen(QColor(255, 215, 0), 2))
        p.setBrush(QColor(255, 255, 0))
        self.draw_star(p, 450, 100, 40)
        
        p.drawPixmap(QRect(200, 250, 250, 250), self.rabbit)
        p.end()


# Team Member 2
class Simple_drawing_window2(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("Drawing Window 2 - Hexagons and Hearts")
        self.rabbit = QPixmap("images/rabbit.png")
    
    def draw_hexagon(self, p, center_x, center_y, size):
        """Draw a regular hexagon"""
        import math
        points = []
        for i in range(6):
            angle = math.pi * 2 * i / 6
            x = center_x + int(size * math.cos(angle))
            y = center_y + int(size * math.sin(angle))
            points.append(QPoint(x, y))
        p.drawPolygon(points)
    
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint(70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
        ])
        
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)
        
        p.drawPolygon([
            QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),
        ])
        
        p.setPen(QPen(QColor(150, 0, 150), 3))
        p.setBrush(QColor(200, 100, 200, 150))
        self.draw_hexagon(p, 280, 80, 40)
        self.draw_hexagon(p, 360, 80, 35)
        self.draw_hexagon(p, 320, 140, 30)
        
        p.setPen(QPen(QColor(200, 0, 0), 2))
        p.setBrush(QColor(255, 50, 50))
        heart_path = QPainterPath()
        heart_path.moveTo(450, 90)
        heart_path.cubicTo(450, 70, 430, 50, 410, 50)
        heart_path.cubicTo(390, 50, 380, 70, 380, 80)
        heart_path.cubicTo(380, 70, 370, 50, 350, 50)
        heart_path.cubicTo(330, 50, 310, 70, 310, 90)
        heart_path.cubicTo(310, 120, 380, 160, 380, 160)
        heart_path.cubicTo(380, 160, 450, 120, 450, 90)
        p.drawPath(heart_path)
        
        p.drawPixmap(QRect(200, 250, 250, 250), self.rabbit)
        p.end()


# Team Member 3 - Extended with spiral/rectangle pattern drawing
class Simple_drawing_window3(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("Drawing Window 3 - Spirals and Patterns")
        self.rabbit = QPixmap("images/rabbit.png")
    
    def draw_spiral(self, p, start_x, start_y):
        """Draw a colorful spiral"""
        import math
        points = []
        for i in range(100):
            angle = i * 0.3
            radius = i * 0.5
            x = start_x + int(radius * math.cos(angle))
            y = start_y + int(radius * math.sin(angle))
            points.append(QPoint(x, y))
        
        # Draw spiral with gradient colors
        for i in range(len(points) - 1):
            color = QColor.fromHsv(int(i * 360 / len(points)), 255, 255)
            p.setPen(QPen(color, 2))
            p.drawLine(points[i], points[i + 1])
    
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        # Original drawings
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint(70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
        ])
        
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)
        
        p.drawPolygon([
            QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),
        ])
        
        # NEW: Draw spiral
        self.draw_spiral(p, 300, 80)
        
        # NEW: Draw rectangle pattern
        p.setPen(QPen(QColor(0, 150, 100), 2))
        for i in range(5):
            p.setBrush(QColor(50 * i, 200 - 30 * i, 150, 100))
            p.drawRect(400 + i * 10, 50 + i * 10, 80 - i * 10, 80 - i * 10)
        
        p.drawPixmap(QRect(200, 250, 250, 250), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)
    
    w1 = Simple_drawing_window1()
    w2 = Simple_drawing_window2()
    w3 = Simple_drawing_window3()
    
    w1.setGeometry(50, 100, 600, 500)
    w2.setGeometry(700, 100, 600, 500)
    w3.setGeometry(1350, 100, 600, 500)
    
    w1.show()
    w2.show()
    w3.show()
    
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())