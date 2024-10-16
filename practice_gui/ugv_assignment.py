from PyQt6.QtWidgets import (QApplication,QWidget,QHBoxLayout,QVBoxLayout,QPushButton,QLineEdit,QListWidget,QListWidgetItem,QMessageBox,QGridLayout)
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import sys




class UGVApp(QWidget):
    def __init__(self):
        super().__init__()
        self.x=0
        self.y=0
      
        self.layoutH=QHBoxLayout()
        self.layoutV=QVBoxLayout()
        self.task_list=QListWidget()
        self.layoutV.addWidget(self.task_list)

        self.front_button=QPushButton("FRONT")
        self.layoutV.addWidget(self.front_button)
        self.front_button.clicked.connect(self.front)

        self.back_button=QPushButton("BACK")
        self.layoutV.addWidget(self.back_button)
        self.back_button.clicked.connect(self.back)

        self.right_button=QPushButton("RIGHT")
        self.layoutH.addWidget(self.right_button)
        self.right_button.clicked.connect(self.right)

        self.left_button=QPushButton("LEFT")
        self.layoutH.addWidget(self.left_button)
        self.left_button.clicked.connect(self.left)
        
        

       
        self.figs = Figure() ##This two line is for Figure Box in GUI
        self.canvas = FigureCanvasQTAgg(self.figs)
        self.ax = self.figs.add_subplot() #This is to add the subline in gui
        self.layoutV.addWidget(self.canvas)

        self.layoutH.addLayout(self.layoutV)
        self.setLayout(self.layoutH)

      


    def front(self):
        self.x=(self.x+5)
        item=QListWidgetItem(f"x={self.x}")
        self.plot_redraw()
        self.task_list.addItem(item)
      
     
        
        print("Went forward One step")
    def back(self):
        self.x=(self.x-5)
        item=QListWidgetItem(f"x={self.x}")
        self.plot_redraw()
        self.task_list.addItem(item)
      

        print("Went back One step")
    def right(self):
        self.y=(self.y+5)
        item=QListWidgetItem(f"y={self.y}")
        self.plot_redraw()
        self.task_list.addItem(item)

        print("Went right One step")
    def left(self):
        self.y=(self.y-5)
        item=QListWidgetItem(f"y={self.y}")
        self.plot_redraw()
        self.task_list.addItem(item)
        

        print("Went left One step")
    

    def plot_redraw(self):
        
       
        self.ax.plot(self.x,self.y,marker='o') #the last part of this bracket is for the figure plotting type
        self.ax.set_xlim(-50, 50) 
        self.ax.set_ylim(-50, 50)  
        
        self.canvas.draw()
  



if __name__=="__main__":
    app=QApplication(sys.argv)
    window=UGVApp()
    window.show()
    sys.exit(app.exec())
    

