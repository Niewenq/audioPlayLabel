# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\12588\OneDrive\nwq_study\studyProjects\audioLabel\audioLabelMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from glwidget import GLWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 617)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/owl.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidgetMain = QtWidgets.QWidget(MainWindow)
        self.centralwidgetMain.setObjectName("centralwidgetMain")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidgetMain)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidgetMain)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.listWidgetAudioList = QtWidgets.QListWidget(self.splitter)
        self.listWidgetAudioList.setObjectName("listWidgetAudioList")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayoutAudioMainArea = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayoutAudioMainArea.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutAudioMainArea.setObjectName("verticalLayoutAudioMainArea")
        self.labelCurrentAudioName = QtWidgets.QLabel(self.layoutWidget)
        self.labelCurrentAudioName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCurrentAudioName.setObjectName("labelCurrentAudioName")
        self.verticalLayoutAudioMainArea.addWidget(self.labelCurrentAudioName)
        self.openGLWidgetAudioPlayShow = GLWidget(self.layoutWidget)
        self.openGLWidgetAudioPlayShow.setObjectName("openGLWidgetAudioPlayShow")
        self.verticalLayoutAudioMainArea.addWidget(self.openGLWidgetAudioPlayShow)
        self.horizontalSliderRateOfProcess = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSliderRateOfProcess.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderRateOfProcess.setObjectName("horizontalSliderRateOfProcess")
        self.verticalLayoutAudioMainArea.addWidget(self.horizontalSliderRateOfProcess)
        self.horizontalLayoutAudioOperationArea = QtWidgets.QHBoxLayout()
        self.horizontalLayoutAudioOperationArea.setObjectName("horizontalLayoutAudioOperationArea")
        self.labelTimeTips = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTimeTips.sizePolicy().hasHeightForWidth())
        self.labelTimeTips.setSizePolicy(sizePolicy)
        self.labelTimeTips.setObjectName("labelTimeTips")
        self.horizontalLayoutAudioOperationArea.addWidget(self.labelTimeTips)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutAudioOperationArea.addItem(spacerItem)
        self.toolButtonPlayBackMode = QtWidgets.QToolButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resources/loop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonPlayBackMode.setIcon(icon1)
        self.toolButtonPlayBackMode.setIconSize(QtCore.QSize(30, 30))
        self.toolButtonPlayBackMode.setObjectName("toolButtonPlayBackMode")
        self.horizontalLayoutAudioOperationArea.addWidget(self.toolButtonPlayBackMode)
        self.toolButtonStop = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButtonStop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/resources/stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonStop.setIcon(icon2)
        self.toolButtonStop.setIconSize(QtCore.QSize(30, 30))
        self.toolButtonStop.setObjectName("toolButtonStop")
        self.horizontalLayoutAudioOperationArea.addWidget(self.toolButtonStop)
        self.toolButtonPre = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButtonPre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/resources/pre.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonPre.setIcon(icon3)
        self.toolButtonPre.setIconSize(QtCore.QSize(30, 30))
        self.toolButtonPre.setObjectName("toolButtonPre")
        self.horizontalLayoutAudioOperationArea.addWidget(self.toolButtonPre)
        self.toolButtonBackward = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButtonBackward.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/resources/backward.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonBackward.setIcon(icon4)
        self.toolButtonBackward.setIconSize(QtCore.QSize(30, 30))
        self.toolButtonBackward.setObjectName("toolButtonBackward")
        self.horizontalLayoutAudioOperationArea.addWidget(self.toolButtonBackward)
        self.toolButtonPlayPause = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButtonPlayPause.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/resources/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonPlayPause.setIcon(icon5)
        self.toolButtonPlayPause.setIconSize(QtCore.QSize(50, 50))
        self.toolButtonPlayPause.setObjectName("toolButtonPlayPause")
        self.horizontalLayoutAudioOperationArea.addWidget(self.toolButtonPlayPause)
        self.toolButtonForward = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButtonForward.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/resources/forward.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonForward.setIcon(icon6)
        self.toolButtonForward.setIconSize(QtCore.QSize(30, 30))
        self.toolButtonForward.setObjectName("toolButtonForward")
        self.horizontalLayoutAudioOperationArea.addWidget(self.toolButtonForward)
        self.toolButtonNext = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButtonNext.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/resources/next.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonNext.setIcon(icon7)
        self.toolButtonNext.setIconSize(QtCore.QSize(30, 30))
        self.toolButtonNext.setObjectName("toolButtonNext")
        self.horizontalLayoutAudioOperationArea.addWidget(self.toolButtonNext)
        self.toolButtonVolume = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButtonVolume.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/resources/volume.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonVolume.setIcon(icon8)
        self.toolButtonVolume.setIconSize(QtCore.QSize(30, 30))
        self.toolButtonVolume.setAutoRaise(False)
        self.toolButtonVolume.setArrowType(QtCore.Qt.NoArrow)
        self.toolButtonVolume.setObjectName("toolButtonVolume")
        self.horizontalLayoutAudioOperationArea.addWidget(self.toolButtonVolume)
        self.horizontalSliderVolume = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSliderVolume.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSliderVolume.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderVolume.setObjectName("horizontalSliderVolume")
        self.horizontalLayoutAudioOperationArea.addWidget(self.horizontalSliderVolume)
        self.labelVolume = QtWidgets.QLabel(self.layoutWidget)
        self.labelVolume.setObjectName("labelVolume")
        self.horizontalLayoutAudioOperationArea.addWidget(self.labelVolume)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutAudioOperationArea.addItem(spacerItem1)
        self.verticalLayoutAudioMainArea.addLayout(self.horizontalLayoutAudioOperationArea)
        self.verticalLayoutAudioMainArea.setStretch(1, 1)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidgetMain)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpenRecently = QtWidgets.QMenu(self.menuFile)
        self.menuOpenRecently.setObjectName("menuOpenRecently")
        self.menuAutoSave = QtWidgets.QMenu(self.menuFile)
        self.menuAutoSave.setObjectName("menuAutoSave")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuStepTime = QtWidgets.QMenu(self.menuSettings)
        self.menuStepTime.setObjectName("menuStepTime")
        self.menuPlayBackRate = QtWidgets.QMenu(self.menuSettings)
        self.menuPlayBackRate.setObjectName("menuPlayBackRate")
        self.menuPlayBackMode = QtWidgets.QMenu(self.menuSettings)
        self.menuPlayBackMode.setObjectName("menuPlayBackMode")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenFile = QtWidgets.QAction(MainWindow)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.actionOpenAudioFolder = QtWidgets.QAction(MainWindow)
        self.actionOpenAudioFolder.setObjectName("actionOpenAudioFolder")
        self.action12 = QtWidgets.QAction(MainWindow)
        self.action12.setObjectName("action12")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.action0s = QtWidgets.QAction(MainWindow)
        self.action0s.setCheckable(True)
        self.action0s.setObjectName("action0s")
        self.action60s = QtWidgets.QAction(MainWindow)
        self.action60s.setCheckable(True)
        self.action60s.setObjectName("action60s")
        self.action120s = QtWidgets.QAction(MainWindow)
        self.action120s.setCheckable(True)
        self.action120s.setObjectName("action120s")
        self.action180s = QtWidgets.QAction(MainWindow)
        self.action180s.setCheckable(True)
        self.action180s.setChecked(False)
        self.action180s.setObjectName("action180s")
        self.action300s = QtWidgets.QAction(MainWindow)
        self.action300s.setCheckable(True)
        self.action300s.setObjectName("action300s")
        self.actionUserDefined = QtWidgets.QAction(MainWindow)
        self.actionUserDefined.setCheckable(True)
        self.actionUserDefined.setObjectName("actionUserDefined")
        self.actionGetStarted = QtWidgets.QAction(MainWindow)
        self.actionGetStarted.setObjectName("actionGetStarted")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpenAudioFiles = QtWidgets.QAction(MainWindow)
        self.actionOpenAudioFiles.setObjectName("actionOpenAudioFiles")
        self.actionOpenJsonFile = QtWidgets.QAction(MainWindow)
        self.actionOpenJsonFile.setObjectName("actionOpenJsonFile")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.action0point25 = QtWidgets.QAction(MainWindow)
        self.action0point25.setCheckable(True)
        self.action0point25.setObjectName("action0point25")
        self.action0point5 = QtWidgets.QAction(MainWindow)
        self.action0point5.setCheckable(True)
        self.action0point5.setObjectName("action0point5")
        self.action0point75 = QtWidgets.QAction(MainWindow)
        self.action0point75.setCheckable(True)
        self.action0point75.setObjectName("action0point75")
        self.action1point0 = QtWidgets.QAction(MainWindow)
        self.action1point0.setCheckable(True)
        self.action1point0.setObjectName("action1point0")
        self.action1point25 = QtWidgets.QAction(MainWindow)
        self.action1point25.setCheckable(True)
        self.action1point25.setObjectName("action1point25")
        self.action1point5 = QtWidgets.QAction(MainWindow)
        self.action1point5.setCheckable(True)
        self.action1point5.setObjectName("action1point5")
        self.action1point75 = QtWidgets.QAction(MainWindow)
        self.action1point75.setCheckable(True)
        self.action1point75.setObjectName("action1point75")
        self.action2point0 = QtWidgets.QAction(MainWindow)
        self.action2point0.setCheckable(True)
        self.action2point0.setObjectName("action2point0")
        self.action2point5 = QtWidgets.QAction(MainWindow)
        self.action2point5.setCheckable(True)
        self.action2point5.setObjectName("action2point5")
        self.action5s = QtWidgets.QAction(MainWindow)
        self.action5s.setCheckable(True)
        self.action5s.setObjectName("action5s")
        self.action1s = QtWidgets.QAction(MainWindow)
        self.action1s.setCheckable(True)
        self.action1s.setObjectName("action1s")
        self.action3s = QtWidgets.QAction(MainWindow)
        self.action3s.setCheckable(True)
        self.action3s.setObjectName("action3s")
        self.action0_5 = QtWidgets.QAction(MainWindow)
        self.action0_5.setCheckable(True)
        self.action0_5.setObjectName("action0_5")
        self.action0_75 = QtWidgets.QAction(MainWindow)
        self.action0_75.setObjectName("action0_75")
        self.action1_0 = QtWidgets.QAction(MainWindow)
        self.action1_0.setCheckable(True)
        self.action1_0.setObjectName("action1_0")
        self.action1_25 = QtWidgets.QAction(MainWindow)
        self.action1_25.setObjectName("action1_25")
        self.action1_75 = QtWidgets.QAction(MainWindow)
        self.action1_75.setObjectName("action1_75")
        self.action1_5 = QtWidgets.QAction(MainWindow)
        self.action1_5.setCheckable(True)
        self.action1_5.setObjectName("action1_5")
        self.action2_0 = QtWidgets.QAction(MainWindow)
        self.action2_0.setCheckable(True)
        self.action2_0.setObjectName("action2_0")
        self.action2_5 = QtWidgets.QAction(MainWindow)
        self.action2_5.setObjectName("action2_5")
        self.action10s = QtWidgets.QAction(MainWindow)
        self.action10s.setCheckable(True)
        self.action10s.setObjectName("action10s")
        self.action30s = QtWidgets.QAction(MainWindow)
        self.action30s.setCheckable(True)
        self.action30s.setObjectName("action30s")
        self.actionCurrentItemOnce = QtWidgets.QAction(MainWindow)
        self.actionCurrentItemOnce.setCheckable(True)
        self.actionCurrentItemOnce.setObjectName("actionCurrentItemOnce")
        self.actionCurrentItemInLoop = QtWidgets.QAction(MainWindow)
        self.actionCurrentItemInLoop.setCheckable(True)
        self.actionCurrentItemInLoop.setObjectName("actionCurrentItemInLoop")
        self.actionSequential = QtWidgets.QAction(MainWindow)
        self.actionSequential.setCheckable(True)
        self.actionSequential.setObjectName("actionSequential")
        self.actionLoop = QtWidgets.QAction(MainWindow)
        self.actionLoop.setCheckable(True)
        self.actionLoop.setObjectName("actionLoop")
        self.actionRandom = QtWidgets.QAction(MainWindow)
        self.actionRandom.setCheckable(True)
        self.actionRandom.setObjectName("actionRandom")
        self.menuAutoSave.addAction(self.action0s)
        self.menuAutoSave.addAction(self.action60s)
        self.menuAutoSave.addAction(self.action120s)
        self.menuAutoSave.addAction(self.action180s)
        self.menuAutoSave.addAction(self.action300s)
        self.menuFile.addAction(self.actionOpenJsonFile)
        self.menuFile.addAction(self.actionOpenAudioFolder)
        self.menuFile.addAction(self.menuOpenRecently.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.menuAutoSave.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionGetStarted)
        self.menuHelp.addAction(self.actionAbout)
        self.menuStepTime.addAction(self.action1s)
        self.menuStepTime.addAction(self.action3s)
        self.menuStepTime.addAction(self.action5s)
        self.menuStepTime.addAction(self.action10s)
        self.menuStepTime.addAction(self.action30s)
        self.menuPlayBackRate.addAction(self.action0_5)
        self.menuPlayBackRate.addAction(self.action1_0)
        self.menuPlayBackRate.addAction(self.action1_5)
        self.menuPlayBackRate.addAction(self.action2_0)
        self.menuPlayBackMode.addAction(self.actionCurrentItemOnce)
        self.menuPlayBackMode.addAction(self.actionCurrentItemInLoop)
        self.menuPlayBackMode.addAction(self.actionSequential)
        self.menuPlayBackMode.addAction(self.actionLoop)
        self.menuPlayBackMode.addAction(self.actionRandom)
        self.menuSettings.addAction(self.menuStepTime.menuAction())
        self.menuSettings.addAction(self.menuPlayBackRate.menuAction())
        self.menuSettings.addAction(self.menuPlayBackMode.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AudioLabel"))
        self.labelCurrentAudioName.setText(_translate("MainWindow", "TextLabel"))
        self.labelTimeTips.setText(_translate("MainWindow", "TextLabel"))
        self.toolButtonPlayBackMode.setText(_translate("MainWindow", "..."))
        self.toolButtonStop.setText(_translate("MainWindow", "..."))
        self.toolButtonPre.setText(_translate("MainWindow", "..."))
        self.toolButtonPre.setShortcut(_translate("MainWindow", "Up"))
        self.toolButtonBackward.setText(_translate("MainWindow", "..."))
        self.toolButtonBackward.setShortcut(_translate("MainWindow", "Left"))
        self.toolButtonPlayPause.setText(_translate("MainWindow", "..."))
        self.toolButtonPlayPause.setShortcut(_translate("MainWindow", "Space"))
        self.toolButtonForward.setText(_translate("MainWindow", "..."))
        self.toolButtonForward.setShortcut(_translate("MainWindow", "Right"))
        self.toolButtonNext.setText(_translate("MainWindow", "..."))
        self.toolButtonNext.setShortcut(_translate("MainWindow", "Down"))
        self.toolButtonVolume.setText(_translate("MainWindow", "..."))
        self.labelVolume.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpenRecently.setTitle(_translate("MainWindow", "Open Recently"))
        self.menuAutoSave.setTitle(_translate("MainWindow", "Auto Save"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuStepTime.setTitle(_translate("MainWindow", "Step Time"))
        self.menuPlayBackRate.setTitle(_translate("MainWindow", "Play Back Rate"))
        self.menuPlayBackMode.setTitle(_translate("MainWindow", "Play Back Mode"))
        self.actionOpenFile.setText(_translate("MainWindow", "Open File..."))
        self.actionOpenFile.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpenAudioFolder.setText(_translate("MainWindow", "Open Audio Folder"))
        self.actionOpenAudioFolder.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action12.setText(_translate("MainWindow", "12"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As..."))
        self.actionSaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.action0s.setText(_translate("MainWindow", "0 s"))
        self.action60s.setText(_translate("MainWindow", "60 s"))
        self.action120s.setText(_translate("MainWindow", "120 s"))
        self.action180s.setText(_translate("MainWindow", "180 s"))
        self.action300s.setText(_translate("MainWindow", "300 s"))
        self.actionUserDefined.setText(_translate("MainWindow", "User Defined"))
        self.actionGetStarted.setText(_translate("MainWindow", "Get Started"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpenAudioFiles.setText(_translate("MainWindow", "Open Audio Files"))
        self.actionOpenAudioFiles.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpenJsonFile.setText(_translate("MainWindow", "Open Json File"))
        self.actionOpenJsonFile.setShortcut(_translate("MainWindow", "Ctrl+J"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action0point25.setText(_translate("MainWindow", "0.25"))
        self.action0point5.setText(_translate("MainWindow", "0.5"))
        self.action0point75.setText(_translate("MainWindow", "0.75"))
        self.action1point0.setText(_translate("MainWindow", "1.0"))
        self.action1point25.setText(_translate("MainWindow", "1.25"))
        self.action1point5.setText(_translate("MainWindow", "1.5"))
        self.action1point75.setText(_translate("MainWindow", "1.75"))
        self.action2point0.setText(_translate("MainWindow", "2.0"))
        self.action2point5.setText(_translate("MainWindow", "2.5"))
        self.action5s.setText(_translate("MainWindow", "5 s"))
        self.action1s.setText(_translate("MainWindow", "1 s"))
        self.action3s.setText(_translate("MainWindow", "3 s"))
        self.action0_5.setText(_translate("MainWindow", "0.5"))
        self.action0_75.setText(_translate("MainWindow", "0.75"))
        self.action1_0.setText(_translate("MainWindow", "1.0"))
        self.action1_25.setText(_translate("MainWindow", "1.25"))
        self.action1_75.setText(_translate("MainWindow", "1.75"))
        self.action1_5.setText(_translate("MainWindow", "1.5"))
        self.action2_0.setText(_translate("MainWindow", "2.0"))
        self.action2_5.setText(_translate("MainWindow", "2.5"))
        self.action10s.setText(_translate("MainWindow", "10 s"))
        self.action30s.setText(_translate("MainWindow", "30 s"))
        self.actionCurrentItemOnce.setText(_translate("MainWindow", "0 Current Item Once"))
        self.actionCurrentItemInLoop.setText(_translate("MainWindow", "1 Current Item In Loop"))
        self.actionSequential.setText(_translate("MainWindow", "2 Sequential"))
        self.actionLoop.setText(_translate("MainWindow", "3 Loop"))
        self.actionRandom.setText(_translate("MainWindow", "4 Random"))
import resources_rc