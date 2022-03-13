# -*- encoding: utf-8 -*-
# @Author  :   Wenqing Nie
# @File    :   volumeSlider.py
# @Time    :   2022/03/08 01:09:28

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QSlider, QVBoxLayout
from PySide6.QtGui import QPalette


class VolumeSliderWidget(QWidget):
    def __init__(self):
        super(VolumeSliderWidget, self).__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.verticalLayout = QVBoxLayout(self)
        self.volumeSlider = QSlider(self)
        self.volumeSlider.setOrientation(Qt.Orientation.Vertical)
        self.verticalLayout.addWidget(self.volumeSlider)

        self.resize(40, 110)
        self.volumeSlider.resize(20, 100)

        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.black)
        self.setAutoFillBackground(True)
        self.setPalette(pal)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    vs = VolumeSliderWidget()
    vs.show()
    sys.exit(app.exec())
