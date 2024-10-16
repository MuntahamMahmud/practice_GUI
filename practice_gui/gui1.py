from PyQt6.QtWidgets import (QApplication,QWidget,QHBoxLayout,QVBoxLayout,QPushButton,QLineEdit,QListWidget,QListWidgetItem,QMessageBox)
from PyQt6.QtCore import Qt
import sys

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.layout=QHBoxLayout()
        self.task_layout=QVBoxLayout()
        self.task_input=QLineEdit()
        self.task_input.setPlaceholderText("input id")
        self.task_layout.addWidget(self.task_input)

        self.task_input1=QLineEdit()
        self.task_input1.setPlaceholderText("input name")
        self.task_layout.addWidget(self.task_input1)

        
     
        
        self.task_list=QListWidget()
        self.task_layout.addWidget(self.task_list)
        self.add_button=QPushButton("Add")
        self.task_layout.addWidget(self.add_button)
        self.add_button.clicked.connect(self.add_task)
        """self.task_layout.addWidget(self.task_list)
        self.task1=QListWidgetItem("Do this 1")
        self.task2=QListWidgetItem("Do this 2")
        self.task_list.addItem(self.task1)
        self.task_list.addItem(self.task2)     """ 
        self.remove_button=QPushButton("Remove")
        self.remove_button.clicked.connect(self.remove_b)
        self.task_layout.addWidget(self.remove_button)
        self.layout.addLayout(self.task_layout)
        self.setLayout(self.layout)
    def add_task(self):  
        task=self.task_input.text()
        task2=self.task_input1.text()
        if task:
            item=QListWidgetItem(task)
            self.task_list.addItem(item)
            
        else:
            QMessageBox.warning(self,'warning','task field no')
        if task2:
            items=QListWidgetItem(task2)
            self.task_list.addItem(items)
            
        else:
            QMessageBox.warning(self,'warning','task field no')
        
    def remove_b(self):
        selected_items=self.task_list.selectedItems()
        if selected_items:
            for itemz in selected_items:
                self.task_list.takeItem(self.task_list.row(itemz))
        else:
            QMessageBox.warning(self,'warning','No task found')



if __name__=="__main__":
    app=QApplication(sys.argv)
    window=ToDoApp()
    window.show()
    sys.exit(app.exec())