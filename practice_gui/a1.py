from PyQt6.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QListWidget, QListWidgetItem)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import sys


class UGVApp(QWidget):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.prev_x = 0  # To keep track of the previous x position
        self.prev_y = 0  # To keep track of the previous y position
        self.layoutH = QHBoxLayout()
        self.layoutV = QVBoxLayout()
        
        self.task_list = QListWidget()
        self.layoutV.addWidget(self.task_list)

        self.front_button = QPushButton("FRONT")
        self.layoutV.addWidget(self.front_button)
        self.front_button.clicked.connect(self.front)

        self.back_button = QPushButton("BACK")
        self.layoutV.addWidget(self.back_button)
        self.back_button.clicked.connect(self.back)

        self.right_button = QPushButton("RIGHT")
        self.layoutH.addWidget(self.right_button)
        self.right_button.clicked.connect(self.right)

        self.left_button = QPushButton("LEFT")
        self.layoutH.addWidget(self.left_button)
        self.left_button.clicked.connect(self.left)

        # Set up the matplotlib figure and canvas
        self.figs = Figure()
        self.canvas = FigureCanvasQTAgg(self.figs)
        self.ax = self.figs.add_subplot()
        self.layoutV.addWidget(self.canvas)

        self.layoutH.addLayout(self.layoutV)
        self.setLayout(self.layoutH)

        # Initialize plot with the starting point
        self.ax.plot(self.x, self.y, 'b-', marker='o')  # Initial point with a line
        self.canvas.draw()

    def front(self):
        self.prev_x, self.prev_y = self.x, self.y  # Save previous position
        self.x += 5
        self.update_plot()
        print("Went forward One step")

    def back(self):
        self.prev_x, self.prev_y = self.x, self.y  # Save previous position
        self.x -= 5
        self.update_plot()
        print("Went back One step")

    def right(self):
        self.prev_x, self.prev_y = self.x, self.y  # Save previous position
        self.y += 5
        self.update_plot()
        print("Went right One step")

    def left(self):
        self.prev_x, self.prev_y = self.x, self.y  # Save previous position
        self.y -= 5
        self.update_plot()
        print("Went left One step")

    def update_plot(self):
        # Clear the axes and plot the line from the previous point to the new point
        self.ax.clear()
        self.ax.plot([self.prev_x, self.x], [self.prev_y, self.y], 'b-')  # Draw a line
        self.ax.plot(self.x, self.y, 'bo')  # Mark the new position
        self.ax.set_xlim(-50, 50)  # Set limits for x-axis
        self.ax.set_ylim(-50, 50)  # Set limits for y-axis
        self.canvas.draw()  # Redraw the canvas

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UGVApp()
    window.show()
    sys.exit(app.exec())
