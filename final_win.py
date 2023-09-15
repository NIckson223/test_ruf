from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication , QWidget,QLabel,
                        QHBoxLayout,QVBoxLayout,QGroupBox,QRadioButton,
                        QLineEdit,QPushButton)

from instr import*


class Experiment():
  def __init__(self, age, t1, t2, t3):
    self.age = int(age)
    self.t1 = int(t1)
    self.t2 = int(t2)
    self.t3 = int(t3)



class FinalWin(QWidget):
  def __init__(self, exp):
    QWidget.__init__(self)
    self.exp = exp

    self.set_appear()
    self.initUI()
  
    self.show()

  def results(self):
    self.index = ((4 * (self.exp.t1+self.exp.t2+self.exp.t3)-200)/10)

    if self.exp.age >= 15:
      if self.index >= 15:
        return txt_res1
      elif self.index<15 and self.index>=11:
        return txt_res2
      elif self.index<11 and self.index>=6:
        return txt_res3
      elif self.index<6 and self.index>=0.5:
        return txt_res4
      else:
        return txt_res5


  def set_appear(self):
    self.setWindowTitle(title_txt)
    self.resize(win_width,win_height)
    self.move(win_x,win_y)

  def initUI(self):
    self.workh_test = QLabel(txt_workheart+self.results())
    self.index_text=QLabel(txt_index+str(round(self.index, 1)))

    self.line_layout=QVBoxLayout()

    self.line_layout.addWidget(self.index_text,alignment=Qt.AlignCenter)
    self.line_layout.addWidget(self.workh_test, alignment=Qt.AlignCenter)

    self.setLayout(self.line_layout)

def connects(self):
    pass