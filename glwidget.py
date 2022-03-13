#!/usr/bin/env python


#############################################################################
##
# Copyright (C) 2015 Riverbank Computing Limited.
# Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
# All rights reserved.
##
# This file is part of the examples of PyQt.
##
# $QT_BEGIN_LICENSE:BSD$
# You may use this file under the terms of the BSD license as follows:
##
# "Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in
# the documentation and/or other materials provided with the
# distribution.
# * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
# the names of its contributors may be used to endorse or promote
# products derived from this software without specific prior written
# permission.
##
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
# $QT_END_LICENSE$
##
#############################################################################


import sys
import random

from PySide6.QtCore import (QPointF, QRectF, QSize, QTimer)
from PySide6.QtGui import (QBrush, QColor, QPainter,
                           QRadialGradient, QSurfaceFormat)
from PySide6.QtWidgets import QApplication
from PySide6.QtOpenGLWidgets import QOpenGLWidget

import OpenGL.GL as gl


class Bubble(object):
    def __init__(self, position, radius, velocity):
        self.position = position
        self.vel = velocity
        self.radius = radius

        self.innerColor = self.randomColor()
        self.outerColor = self.randomColor()
        self.updateBrush()

    def updateBrush(self):
        gradient = QRadialGradient(QPointF(self.radius, self.radius),
                                   self.radius, QPointF(self.radius * 0.5, self.radius * 0.5))

        gradient.setColorAt(0, QColor(255, 255, 255, 255))
        gradient.setColorAt(0.25, self.innerColor)
        gradient.setColorAt(1, self.outerColor)
        self.brush = QBrush(gradient)

    def drawBubble(self, painter):
        painter.save()
        painter.translate(self.position.x() - self.radius,
                          self.position.y() - self.radius)
        painter.setBrush(self.brush)
        painter.drawEllipse(0, 0, int(2 * self.radius), int(2 * self.radius))
        painter.restore()

    def randomColor(self):
        red = random.randrange(205, 256)
        green = random.randrange(205, 256)
        blue = random.randrange(205, 256)
        alpha = random.randrange(91, 192)

        return QColor(red, green, blue, alpha)

    def move(self, bbox):
        self.position += self.vel
        leftOverflow = self.position.x() - self.radius - bbox.left()
        rightOverflow = self.position.x() + self.radius - bbox.right()
        topOverflow = self.position.y() - self.radius - bbox.top()
        bottomOverflow = self.position.y() + self.radius - bbox.bottom()

        if leftOverflow < 0.0:
            self.position.setX(self.position.x() - 2 * leftOverflow)
            self.vel.setX(-self.vel.x())
        elif rightOverflow > 0.0:
            self.position.setX(self.position.x() - 2 * rightOverflow)
            self.vel.setX(-self.vel.x())

        if topOverflow < 0.0:
            self.position.setY(self.position.y() - 2 * topOverflow)
            self.vel.setY(-self.vel.y())
        elif bottomOverflow > 0.0:
            self.position.setY(self.position.y() - 2 * bottomOverflow)
            self.vel.setY(-self.vel.y())

    def rect(self):
        return QRectF(self.position.x() - self.radius,
                      self.position.y() - self.radius, 2 * self.radius,
                      2 * self.radius)


class GLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        self.trolltechGreen = QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)
        self.animationTimer = QTimer()
        self.animationTimer.setSingleShot(False)
        self.animationTimer.timeout.connect(self.animate)

    def setupUi(self):
        self.object = 0
        self.bubbles = []

        self.setAutoFillBackground(False)
        self.setMinimumSize(200, 200)

    def initializeGL(self):
        self.object = self.makeObject()

    def paintEvent(self, event):
        self.makeCurrent()

        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glPushMatrix()

        self.setClearColor(self.trolltechPurple.darker())
        gl.glShadeModel(gl.GL_SMOOTH)
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glEnable(gl.GL_LIGHTING)
        gl.glEnable(gl.GL_LIGHT0)
        gl.glEnable(gl.GL_MULTISAMPLE)
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION,
                     (0.5, 5.0, 7.0, 1.0))

        self.setupViewport(self.width(), self.height())

        gl.glClear(
            gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity()
        gl.glTranslated(0.0, 0.0, -10.0)
        gl.glCallList(self.object)

        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glPopMatrix()

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for bubble in self.bubbles:
            if bubble.rect().intersects(QRectF(event.rect())):
                bubble.drawBubble(painter)

        painter.end()

    def resizeGL(self, width, height):
        self.setupViewport(width, height)

    def showEvent(self, event):
        self.createBubbles(30 - len(self.bubbles))

    def sizeHint(self):
        return QSize(400, 400)

    def makeObject(self):
        genList = gl.glGenLists(1)
        gl.glNewList(genList, gl.GL_COMPILE)

        gl.glBegin(gl.GL_QUADS)

        gl.glEnd()
        gl.glEndList()

        return genList

    def quad(self, x1, y1, x2, y2, x3, y3, x4, y4):
        gl.glNormal3d(0.0, 0.0, -1.0)
        gl.glVertex3d(x1, y1, -0.05)
        gl.glVertex3d(x2, y2, -0.05)
        gl.glVertex3d(x3, y3, -0.05)
        gl.glVertex3d(x4, y4, -0.05)

        gl.glNormal3d(0.0, 0.0, 1.0)
        gl.glVertex3d(x4, y4, +0.05)
        gl.glVertex3d(x3, y3, +0.05)
        gl.glVertex3d(x2, y2, +0.05)
        gl.glVertex3d(x1, y1, +0.05)

    def extrude(self, x1, y1, x2, y2):
        self.setColor(self.trolltechGreen.darker(250 + int(100 * x1)))

        gl.glNormal3d((x1 + x2) / 2.0, (y1 + y2) / 2.0, 0.0)
        gl.glVertex3d(x1, y1, +0.05)
        gl.glVertex3d(x2, y2, +0.05)
        gl.glVertex3d(x2, y2, -0.05)
        gl.glVertex3d(x1, y1, -0.05)

    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle

    def createBubbles(self, number):
        for i in range(number):
            position = QPointF(self.width() * (0.1 + 0.8 * random.random()),
                               self.height() * (0.1 + 0.8 * random.random()))
            radius = min(self.width(), self.height()) * \
                (0.0125 + 0.0875 * random.random())
            velocity = QPointF(self.width() * 0.0125 * (-0.5 + random.random()),
                               self.height() * 0.0125 * (-0.5 + random.random()))

            self.bubbles.append(Bubble(position, radius, velocity))

    def animate(self):
        for bubble in self.bubbles:
            bubble.move(self.rect())

        self.update()

    def setupViewport(self, width, height):
        side = min(width, height)
        gl.glViewport((width - side) // 2, (height - side) // 2, side,
                      side)

        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)

    def setClearColor(self, c):
        gl.glClearColor(c.redF(), c.greenF(), c.blueF(), c.alphaF())

    def setColor(self, c):
        gl.glColor4f(c.redF(), c.greenF(), c.blueF(), c.alphaF())

    def start(self):
        self.animationTimer.start(25)

    def stop(self):
        self.animationTimer.stop()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    fmt = QSurfaceFormat()
    fmt.setSamples(8)
    QSurfaceFormat.setDefaultFormat(fmt)
    window = GLWidget()
    window.setupUi()
    window.start()
    window.show()
    sys.exit(app.exec())
