# -*- encoding: utf-8 -*-
# @Author  :   Wenqing Nie
# @File    :   audioLabelMainWindow.py
# @Time    :   2022/03/06 18:05:46


import re
from os import listdir
from sys import exit, argv
from Ui_audioLabelMainWindow import Ui_MainWindow
from qtoaster import Toast
from volumeslider import VolumeSliderWidget
from time import sleep

from PySide6.QtGui import QPixmap, QAction, QActionGroup, QCursor
from PySide6.QtCore import QPoint, QEvent, Slot, QEvent, Signal, QTimer
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QMainWindow, QApplication, QSplashScreen, QFileDialog


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.openGLWidgetAudioPlayShow.setupUi()
        self.__toast = Toast()

        self.ui = Ui_MainWindow()

        self.__jsonFilePath = None
        self.__audioFilesName = None
        self.__audioFolder = None
        self.__recentOpened = None
        self.__audioFilesPath = None

        self.__current_index = None

        # QMediaPlayer Initilizing
        self.__audioOutput = QAudioOutput()  # define eralier than  QMediaPlayer
        self.__mPlayer = QMediaPlayer()
        # volume settings
        self.__mPlayer.setAudioOutput(self.__audioOutput)
        self.__volume_ratio = 100 / self.__audioOutput.volume()
        self.horizontalSliderVolume.setRange(0, 100)
        self.horizontalSliderVolume.setValue(100)
        self.volumeSliderWidget = VolumeSliderWidget()
        self.volumeSliderWidget.volumeSlider.setRange(0, 100)
        self.volumeSliderWidget.volumeSlider.setValue(100)
        self.labelVolume.setText(f"{100:<4d} %")
        self.volumeSliderWidgetTimer = QTimer()
        self.volumeSliderWidgetTimer.timeout.connect(
            self.on_volumeSliderWidgetTimer_timeout)
        # self.volumeSliderWidget.leaveEvent = self.on_volumeSliderWidget_leaveEvent
        # self.volumeSliderWidget.enterEvent = self.on_volumeSliderWidget_enterEvent

        # autoSave Action Group
        self.qActionGroupAutoSave = QActionGroup(self)
        self.qActionGroupAutoSave.addAction(self.action0s)
        self.qActionGroupAutoSave.addAction(self.action60s)
        self.qActionGroupAutoSave.addAction(self.action120s)
        self.qActionGroupAutoSave.addAction(self.action180s)
        self.qActionGroupAutoSave.addAction(self.action300s)
        self.action0s.setChecked(True)
        self.__autoSavePeriod = 0

        # playBackRate Action Group
        self.qActionGroupPlayBackRate = QActionGroup(self)
        self.qActionGroupPlayBackRate.addAction(self.action0_5)
        self.qActionGroupPlayBackRate.addAction(self.action1_0)
        self.qActionGroupPlayBackRate.addAction(self.action1_5)
        self.qActionGroupPlayBackRate.addAction(self.action2_0)
        self.action1_0.setChecked(True)

        # stepTime Action Group
        self.qActionGroupStepTime = QActionGroup(self)
        self.qActionGroupStepTime.addAction(self.action1s)
        self.qActionGroupStepTime.addAction(self.action3s)
        self.qActionGroupStepTime.addAction(self.action5s)
        self.qActionGroupStepTime.addAction(self.action10s)
        self.qActionGroupStepTime.addAction(self.action30s)
        self.action1s.setChecked(True)
        self.__stepTime = 1

        self.actionOpenJsonFile.triggered.connect(
            self.on_actionOpenJsonFile_triggered)
        self.actionOpenAudioFolder.triggered.connect(
            self.on_actionOpenAudioFolder_triggered)

        self.menuPlayBackRate.triggered.connect(
            self.on_menuPlayBackRate_triggered)
        self.menuStepTime.triggered.connect(self.on_menuStepTime_triggered)
        self.menuAutoSave.triggered.connect(self.on_menuAutoSave_triggered)

        self.__mPlayer.playbackStateChanged.connect(
            self.on_mPlayer_playbackStateChanged)
        self.__mPlayer.errorOccurred.connect(self.on_mPlayer_errorOccurred)

        self.toolButtonPlayPause.clicked.connect(
            self.on_toolButtonPlayPause_clicked)
        self.toolButtonVolume.enterEvent = self.on_toolButtonVolume_enterEvent
        # self.toolButtonVolume.leaveEvent = self.on_toolButtonVolume_leaveEvent

        self.horizontalSliderVolume.valueChanged.connect(
            self.on_horizontalSliderVolume_valueChanged)
        self.volumeSliderWidget.volumeSlider.valueChanged.connect(
            self.on_volumeSlider_valueChanged)

        self.__update_statusbar_message()

    @staticmethod
    def millisecondsToFormatedString(milliseconds: int) -> str:
        hours, minutes = divmod(milliseconds, 3600000)
        minutes, seconds = divmod(minutes, 60000)
        seconds = seconds // 1000
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def __update_statusbar_message(self):
        self.statusbar.showMessage(
            f"AutoSave:{self.__autoSavePeriod:3d}s✦PlayBackRate:{self.__mPlayer.playbackRate()}✦StepTime:{self.__stepTime:2d}s")

    @Slot()
    def on_actionOpenJsonFile_triggered(self):
        self.__jsonFilePath, _ = QFileDialog.getOpenFileName(parent=self, caption='Open JSON Files',
                                                             filter='JSON Files(*.json)')

    @Slot()
    def on_actionOpenAudioFolder_triggered(self):
        folder = QFileDialog.getExistingDirectory(
            self, caption='Choose A Directory')
        if folder:
            audioFilesName = [file for file in listdir(
                folder) if re.match(r".+\.wav$|.+\.mp3$|.+\.m4a$", file)]
            if audioFilesName:
                self.__audioFilesPath = [
                    folder + '/' + file for file in audioFilesName]
                self.__audioFolder = folder
                self.__audioFilesName = audioFilesName
                self.__current_index = 0
            else:
                self.__toast.toast(
                    pos=QPoint(self.pos().x() + self.geometry().width() // 2,
                               self.pos().y() + self.geometry().height()), toast_text=f"No m4a, mp3 or wav files in Folder {folder}.")

    @Slot(QAction)
    def on_menuPlayBackRate_triggered(self, action: QAction):
        self.__mPlayer.setPlaybackRate(float(action.text()))
        self.__update_statusbar_message()

    @Slot(QAction)
    def on_menuStepTime_triggered(self, action: QAction):
        self.__stepTime = int(re.match(r"^\d+", action.text()).group())
        self.__update_statusbar_message()

    @Slot(QAction)
    def on_menuAutoSave_triggered(self, action: QAction):
        self.__autoSavePeriod = int(re.match(r"^\d+", action.text()).group())
        self.__update_statusbar_message()

    @Slot()
    def on_toolButtonPlayPause_clicked(self):
        if self.__mPlayer.mediaStatus() == QMediaPlayer.NoMedia:
            if self.__audioFilesPath:
                self.__mPlayer.setSource(
                    self.__audioFilesPath[self.__current_index])
                self.__mPlayer.play()
            else:
                self.__toast.toast(
                    pos=QPoint(self.pos().x() + self.geometry().width() // 2,
                               self.pos().y() + self.geometry().height()), toast_text="Please choose audio files before play.")
        else:
            if self.__mPlayer.playbackState() == QMediaPlayer.PlayingState:
                self.__mPlayer.pause()
            else:
                self.__mPlayer.play()

    def on_toolButtonVolume_enterEvent(self, event: QEvent):
        if not self.volumeSliderWidget.isVisible():
            pos = self.toolButtonVolume.mapToGlobal(QPoint(0, 0))
            pos.setX(pos.x() + (self.toolButtonVolume.geometry().width() // 2 -
                                self.volumeSliderWidget.geometry().width() // 2))

            pos.setY(pos.y() - self.volumeSliderWidget.geometry().height())
            self.volumeSliderWidget.move(pos)
            self.volumeSliderWidget.show()

            self.toolButtonVolumeTopLeft = self.toolButtonVolume.mapToGlobal(
                QPoint(0, 0))
            toolButtonVolumeGeometry = self.toolButtonVolume.geometry()
            self.toolButtonVolumeBottomRight = self.toolButtonVolume.mapToGlobal(
                QPoint(toolButtonVolumeGeometry.width(), toolButtonVolumeGeometry.height()))
            self.volumeSliderWidgetTopLeft = self.volumeSliderWidget.mapToGlobal(
                QPoint(0, 0))
            volumeSliderWidgetGeometry = self.volumeSliderWidget.geometry()
            self.volumeSliderWidgetBottomRight = self.volumeSliderWidget.mapToGlobal(
                QPoint(volumeSliderWidgetGeometry.width(), volumeSliderWidgetGeometry.height()))

            self.volumeSliderWidgetTimer.start(300)

    @Slot()
    def on_volumeSliderWidgetTimer_timeout(self):
        x = QCursor.pos().x()
        y = QCursor.pos().y()

        if not ((self.toolButtonVolumeTopLeft.x() <= x <= self.toolButtonVolumeBottomRight.x() and self.toolButtonVolumeTopLeft.y() <= y <= self.toolButtonVolumeBottomRight.y()) or (self.volumeSliderWidgetTopLeft.x() <= x <= self.volumeSliderWidgetBottomRight.x() and self.volumeSliderWidgetTopLeft.y() <= y <= self.volumeSliderWidgetBottomRight.y())):
            self.volumeSliderWidget.close()
            self.volumeSliderWidgetTimer.stop()

    @ Slot(QMediaPlayer.PlaybackState)
    def on_mPlayer_playbackStateChanged(self, newState: QMediaPlayer.PlaybackState):
        if newState == QMediaPlayer.PlayingState:
            self.openGLWidgetAudioPlayShow.start()
            self.toolButtonPlayPause.setIcon(
                QPixmap(":/icons/resources/pause.svg"))
        else:
            self.openGLWidgetAudioPlayShow.stop()
            self.toolButtonPlayPause.setIcon(
                QPixmap(":/icons/resources/play.svg"))

    @ Slot(QMediaPlayer.Error, str)
    def on_mPlayer_errorOccurred(self, error: QMediaPlayer.Error, errorString: str):
        self.__toast.toast(
            pos=QPoint(self.pos().x() + self.geometry().width() // 2,
                       self.pos().y() + self.geometry().height()), toast_text=errorString)

    @ Slot(int)
    def on_horizontalSliderVolume_valueChanged(self, value: int):
        self.__audioOutput.setVolume(value / self.__volume_ratio)
        self.labelVolume.setText(f"{value:<4d} %")
        self.volumeSliderWidget.volumeSlider.setValue(value)

    @Slot(int)
    def on_volumeSlider_valueChanged(self, value: int):
        self.__audioOutput.setVolume(value / self.__volume_ratio)
        self.labelVolume.setText(f"{value:<4d} %")
        self.horizontalSliderVolume.setValue(value)


if __name__ == "__main__":
    app = QApplication(argv)
    splash = QSplashScreen(QPixmap(":/icons/resources/owl.svg"))
    splash.show()
    ui = MainWindow()
    ui.show()
    splash.finish(ui)
    exit(app.exec())
