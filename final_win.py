from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication , QWidget,QLabel,
                        QHBoxLayout,QVBoxLayout,QGroupBox,QRadioButton,
                        QLineEdit,QPushButton)

from instr import*


class FinalWin(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.set_appear()
    self.initUI()
  
    self.show()
  
  def set_appear(self):
    self.setWindowTitle(title_txt)
    self.resize(win_width,win_height)
    self.move(win_x,win_y)

  def initUI(self):
    self.workh_test = QLabel(txt_workheart)
    self.index_text=QLabel(txt_index)

    self.line_layout=QVBoxLayout()

    self.line_layout.addWidget(self.index_text,alignment=Qt.AlignCenter)
    self.line_layout.addWidget(self.workh_test, alignment=Qt.AlignCenter)

    self.setLayout(self.line_layout)

def connects(self):
    pass