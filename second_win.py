from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication , QWidget,QLabel,
                        QHBoxLayout,QVBoxLayout,QGroupBox,QRadioButton,
                        QLineEdit,QPushButton)


from instr import*


class TestWin(QWidget):
    def set_appear(self):
        self.setWindowTitle(title_txt)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)

    def initUI(self):
        pass

    def connects(self):
        pass