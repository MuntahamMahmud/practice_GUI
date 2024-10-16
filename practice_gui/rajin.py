import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout
from PyQt6.QtCore import QTimer, Qt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

class UGVNavigation(QWidget):
    def __init__(self):
        super().__init__()

        # UGV Position and Movement Speed
        self.x = 0
        self.y = 0
        self.step_size = 0.1  # Small steps for smooth movement

        # Set up the window
        self.setWindowTitle("UGV Navigation System")
        self.setGeometry(100, 100, 400, 300)

        # Layouts for buttons
        self.layout = QVBoxLayout()
        self.button_layout = QGridLayout()

        # Navigation buttons (WASD layout)
        self.button_w = QPushButton('W', self)
        self.button_a = QPushButton('A', self)
        self.button_s = QPushButton('S', self)
        self.button_d = QPushButton('D', self)

        # Position buttons in a grid like a keyboard's WASD layout
        self.button_layout.addWidget(self.button_w, 0, 1)  # W is at the top middle
        self.button_layout.addWidget(self.button_a, 1, 0)  # A is in the middle left
        self.button_layout.addWidget(self.button_s, 1, 1)  # S is in the center
        self.button_layout.addWidget(self.button_d, 1, 2)  # D is in the middle right

        self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)

        # Connect buttons to movement functions
        self.button_w.clicked.connect(self.move_up)
        self.button_a.clicked.connect(self.move_left)
        self.button_s.clicked.connect(self.move_down)
        self.button_d.clicked.connect(self.move_right)

        # Matplotlib figure for real-time plotting
        self.fig, self.ax = plt.subplots()
        self.trajectory, = self.ax.plot([], [], 'ro-', lw=2)  # Red line for trajectory
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.grid(True)
        self.positions = [[self.x, self.y]]  # Storing all positions

        # Timer for updating the plot
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(50)  # Update every 50 ms for smoother movement

        # State for diagonal movement
        self.keys_pressed = set()  # Track keys currently pressed

        # Show matplotlib window
        self.fig.show()

    def keyPressEvent(self, event):
        key = event.key()
        self.keys_pressed.add(key)  # Add key to the pressed keys set

        if Qt.Key.Key_W in self.keys_pressed and Qt.Key.Key_A in self.keys_pressed:
            self.move_up_left()
        elif Qt.Key.Key_W in self.keys_pressed and Qt.Key.Key_D in self.keys_pressed:
            self.move_up_right()
        elif Qt.Key.Key_S in self.keys_pressed and Qt.Key.Key_A in self.keys_pressed:
            self.move_down_left()
        elif Qt.Key.Key_S in self.keys_pressed and Qt.Key.Key_D in self.keys_pressed:
            self.move_down_right()
        else:
            if key == Qt.Key.Key_W:
                self.move_up()
            elif key == Qt.Key.Key_A:
                self.move_left()
            elif key == Qt.Key.Key_S:
                self.move_down()
            elif key == Qt.Key.Key_D:
                self.move_right()

    def keyReleaseEvent(self, event):
        key = event.key()
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)

    def move_up(self):
        self.y += self.step_size
        self.update_position()

    def move_down(self):
        self.y -= self.step_size
        self.update_position()

    def move_left(self):
        self.x -= self.step_size
        self.update_position()

    def move_right(self):
        self.x += self.step_size
        self.update_position()

    def move_up_left(self):
        self.y += self.step_size / np.sqrt(2)
        self.x -= self.step_size / np.sqrt(2)
        self.update_position()

    def move_up_right(self):
        self.y += self.step_size / np.sqrt(2)
        self.x += self.step_size / np.sqrt(2)
        self.update_position()

    def move_down_left(self):
        self.y -= self.step_size / np.sqrt(2)
        self.x -= self.step_size / np.sqrt(2)
        self.update_position()

    def move_down_right(self):
        self.y -= self.step_size / np.sqrt(2)
        self.x += self.step_size / np.sqrt(2)
        self.update_position()

    def update_position(self):
        self.positions.append([self.x, self.y])

    def update_plot(self):
        x_data = [pos[0] for pos in self.positions]
        y_data = [pos[1] for pos in self.positions]
        self.trajectory.set_data(x_data, y_data)
        self.ax.set_xlim(min(x_data) - 1, max(x_data) + 1)
        self.ax.set_ylim(min(y_data) - 1, max(y_data) + 1)
        self.fig.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UGVNavigation()
    window.show()
    sys.exit(app.exec())