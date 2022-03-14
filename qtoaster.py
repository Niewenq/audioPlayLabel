# -*- encoding: utf-8 -*-
# @Author  :   Wenqing Nie
# @File    :   qtoaster.py
# @Time    :   2022/03/07 23:09:31

from PySide6 import QtWidgets, QtGui, QtCore


class Toast(QtWidgets.QWidget):
    def __init__(self):
        super(Toast, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.background_color = QtGui.QColor("#778899")
        self.toast_text_color = QtCore.Qt.black
        self.setFont(QtGui.QFont('Simsun', 10))
        self.toast_text = ""
        self.duration = 3000
        self.min_height = self.font().pointSizeF()
        self.min_width = self.font().pointSize()

        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.hide)

    @QtCore.Slot()
    def on_timer_timeout(self):
        self.timer.stop()
        self.close()

    def init_UI(self):
        height = self.get_font_size() * 2
        width = len(self.toast_text) * self.get_font_size()*0.8
        if height < self.min_height:
            height = self.min_height
        if width < self.min_width:
            width = self.min_width
        self.resize(int(width), int(height))
        self.move(self.position.x() - width // 2,
                  self.position.y() - height // 2)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHints(QtGui.QPainter.Antialiasing |
                               QtGui.QPainter.TextAntialiasing)
        rect_line_path = QtGui.QPainterPath()
        rectangle = QtCore.QRectF(0, 0, self.width(), self.height())
        rect_line_path.addRoundedRect(
            rectangle, self.height() / 2, self.height() / 2, QtCore.Qt.AbsoluteSize)
        painter.fillPath(rect_line_path, QtGui.QColor(self.background_color))

        pen = QtGui.QPen(QtGui.QColor(self.toast_text_color))
        painter.setPen(pen)
        painter.setFont(self.font())
        self.draw_text(painter)
        super(Toast, self).paintEvent(event)

    def get_font_size(self):
        return self.font().pointSizeF()

    def draw_text(self, painter: QtGui.QPainter):
        painter.drawText(QtCore.QRectF(0, 0, self.width(), self.height()),
                         QtCore.Qt.AlignCenter, self.toast_text)

    def toast(self, pos: QtCore.QPoint, toast_text: str, duration: int = None, background_color: QtGui.QColor = None):
        self.hide()

        if pos:
            self.position = pos
        if toast_text:
            self.toast_text = toast_text
        if duration:
            self.duration = duration
        if background_color:
            self.background_color = background_color
        self.init_UI()
        self.repaint()
        self.show()
        self.timer.start(self.duration)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    toast = Toast()
    toast.toast(QtCore.QPoint(1000, 1000),
                "Test Text!!!", 3000)
    sys.exit(app.exec())
