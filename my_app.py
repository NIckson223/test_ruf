from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication , QWidget,QLabel,
                        QHBoxLayout,QVBoxLayout,QGroupBox,QRadioButton,
                        QLineEdit,QPushButton)

from instr import*
from second_win import*

class MainWin(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.set_appear()
    self.initUI()
    self.connects()
    self.show()
  
  def set_appear(self):
    self.setWindowTitle(title_txt)
    self.resize(win_width,win_height)
    self.move(win_x,win_y)

  def initUI(self):
    self.hello_txt=QLabel(txt_hello)
    self.btn_next=QPushButton(txt_next)
    self.instructions = QLabel(txt_instructions)
    self.layout=QVBoxLayout()

    self.layout.addWidget(self.hello_txt)
    self.layout.addWidget(self.btn_next)
    self.layout.addWidget(self.instructions)
    
    
    self.setLayout(self.layout)
  def connects(self):
    self.btn_next.clicked.connect(self.next_click)
  
  def next_click(self):
    self.tw = TestWin()
    self.hide()
    

app=QApplication([])
mw=MainWin()
app.exec_()