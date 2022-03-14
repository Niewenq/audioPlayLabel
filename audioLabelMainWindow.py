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

from PySide6.QtGui import QPixmap, QAction, QActionGroup, QCursor
from PySide6.QtCore import QPoint, QEvent, Slot, QEvent, QTimer, QRect
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QMainWindow, QApplication, QSplashScreen, QFileDialog, QToolButton, QToolTip


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.openGLWidgetAudioPlayShow.setupUi()
        self._toast = Toast()

        self._jsonFilePath = None
        self._audioFilesName = None
        self._audioFolder = None
        self._recentOpened = None
        self._audioFilesPath = None
        self._audioDurationTimeStr = None
        self._current_index = None
        self.labelCurrentAudioName.setText("")
        self.labelTimeTips.setText("00:00:00/00:00:00")
        self._audioDurationTimeStr = "00:00:00"

        # QMediaPlayer Initilizing
        self._audioOutput = QAudioOutput()  # define eralier than  QMediaPlayer
        self._mPlayer = QMediaPlayer()
        # volume settings
        self._mPlayer.setAudioOutput(self._audioOutput)
        self._volume_ratio = 100 / self._audioOutput.volume()
        self.horizontalSliderVolume.setRange(0, 100)
        self.horizontalSliderVolume.setValue(100)
        self.volumeSliderWidget = VolumeSliderWidget()
        self.volumeSliderWidget.volumeSlider.setRange(0, 100)
        self.volumeSliderWidget.volumeSlider.setValue(100)
        self.labelVolume.setText(f"{100:<4d} %")
        self.volumeSliderWidgetTimer = QTimer()
        self.volumeSliderWidgetTimer.timeout.connect(
            self.on_volumeSliderWidgetTimer_timeout)

        # autoSave Action Group
        self.qActionGroupAutoSave = QActionGroup(self)
        self.qActionGroupAutoSave.addAction(self.action0s)
        self.qActionGroupAutoSave.addAction(self.action60s)
        self.qActionGroupAutoSave.addAction(self.action120s)
        self.qActionGroupAutoSave.addAction(self.action180s)
        self.qActionGroupAutoSave.addAction(self.action300s)
        self.action0s.setChecked(True)
        self._autoSavePeriod = 0

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
        self.action5s.setChecked(True)
        self._stepTime = 5

        self.actionOpenJsonFile.triggered.connect(
            self.on_actionOpenJsonFile_triggered)
        self.actionOpenAudioFolder.triggered.connect(
            self.on_actionOpenAudioFolder_triggered)
        self.actionExit.triggered.connect(self.on_actionExit_triggered)

        self.menuPlayBackRate.triggered.connect(
            self.on_menuPlayBackRate_triggered)
        self.menuStepTime.triggered.connect(self.on_menuStepTime_triggered)
        self.menuAutoSave.triggered.connect(self.on_menuAutoSave_triggered)

        self._mPlayer.playbackStateChanged.connect(
            self.on_mPlayer_playbackStateChanged)
        self._mPlayer.errorOccurred.connect(self.on_mPlayer_errorOccurred)
        self._mPlayer.durationChanged.connect(self.on_mPlayer_durationChanged)
        self._mPlayer.positionChanged.connect(self.on_mPlayer_positionChanged)
        self._mPlayer.mediaStatusChanged.connect(
            self.on_mPlayer_mediaStatusChanged)
        self._mPlayer.metaDataChanged.connect(self.on_mPlayer_metaDataChanged)

        self.toolButtonPlayPause.clicked.connect(
            self.on_toolButtonPlayPause_clicked)
        self.toolButtonPre.clicked.connect(self.on_toolButtonPre_clicked)
        self.toolButtonNext.clicked.connect(self.on_toolButtonNext_clicked)
        self.toolButtonForward.clicked.connect(
            self.on_toolButtonForward_clicked)
        self.toolButtonBackward.clicked.connect(
            self.on_toolButtonBackward_clicked)
        self.toolButtonVolume.clicked.connect(self.on_toolButtonVolume_clicked)
        self.toolButtonStop.clicked.connect(self._mPlayer.stop)
        self.toolButtonVolume.enterEvent = self.on_toolButtonVolume_enterEvent

        self.horizontalSliderVolume.valueChanged.connect(
            self.on_horizontalSliderVolume_valueChanged)
        self.volumeSliderWidget.volumeSlider.valueChanged.connect(
            self.on_volumeSlider_valueChanged)
        self.horizontalSliderRateOfProcess.valueChanged.connect(
            self._mPlayer.setPosition)

        self._update_statusbar_message()

    @staticmethod
    def millisecondsToFormatedString(milliseconds: int) -> str:
        hours, minutes = divmod(milliseconds, 3600000)
        minutes, seconds = divmod(minutes, 60000)
        seconds = seconds // 1000
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def _update_statusbar_message(self):
        self.statusbar.showMessage(
            f"AutoSave:{self._autoSavePeriod:3d}s✦PlayBackRate:{self._mPlayer.playbackRate()}✦StepTime:{self._stepTime:2d}s")

    @Slot()
    def on_actionOpenJsonFile_triggered(self):
        self._jsonFilePath, _ = QFileDialog.getOpenFileName(parent=self, caption='Open JSON Files',
                                                            filter='JSON Files(*.json)')

    @Slot()
    def on_actionOpenAudioFolder_triggered(self):
        folder = QFileDialog.getExistingDirectory(
            self, caption='Choose A Directory')
        if folder:
            audioFilesName = [file for file in listdir(
                folder) if re.match(r".+\.wav$|.+\.mp3$|.+\.m4a$", file)]
            if audioFilesName:
                self._audioFilesPath = [
                    folder + '/' + file for file in audioFilesName]
                self._audioFolder = folder
                self._audioFilesName = audioFilesName
                self._current_index = 0
            else:
                self._toast.toast(
                    pos=QPoint(self.pos().x() + self.geometry().width() // 2,
                               self.pos().y() + self.geometry().height()), toast_text=f"No m4a, mp3 or wav files in Folder {folder}.")

    @Slot()
    def on_actionExit_triggered(self):
        QApplication.instance().quit()

    @Slot(QAction)
    def on_menuPlayBackRate_triggered(self, action: QAction):
        self._mPlayer.setPlaybackRate(float(action.text()))
        self._update_statusbar_message()

    @Slot(QAction)
    def on_menuStepTime_triggered(self, action: QAction):
        self._stepTime = int(re.match(r"^\d+", action.text()).group())
        self.toolButtonForward.setToolTip(f"前进{self._stepTime}秒")
        self.toolButtonBackward.setToolTip(f"后退{self._stepTime}秒")
        self._update_statusbar_message()

    @Slot(QAction)
    def on_menuAutoSave_triggered(self, action: QAction):
        self._autoSavePeriod = int(re.match(r"^\d+", action.text()).group())
        self._update_statusbar_message()

    @Slot()
    def on_toolButtonPlayPause_clicked(self):
        if self._mPlayer.mediaStatus() == QMediaPlayer.NoMedia:
            if self._audioFilesPath:
                self._mPlayer.setSource(
                    self._audioFilesPath[self._current_index])
                self._mPlayer.play()
            else:
                self._toast.toast(
                    pos=QPoint(self.pos().x() + self.geometry().width() // 2,
                               self.pos().y() + self.geometry().height()), toast_text="Please choose audio files before play.")
        else:
            if self._mPlayer.playbackState() == QMediaPlayer.PlayingState:
                self._mPlayer.pause()
            else:
                self._mPlayer.play()

    @Slot()
    def on_toolButtonPre_clicked(self):
        # Go to previous track if we are within the first 5 seconds of playback
        # Otherwise, seek to the beginning.
        if self._mPlayer.position() <= 5000:
            self._current_index = (
                self._current_index - 1) % len(self._audioFilesPath)
            self._mPlayer.setSource(self._audioFilesPath[self._current_index])
            self._mPlayer.play()
        else:
            self._mPlayer.setPosition(0)

    @Slot()
    def on_toolButtonNext_clicked(self):
        self._current_index = (self._current_index +
                               1) % len(self._audioFilesPath)
        self._mPlayer.setSource(self._audioFilesPath[self._current_index])
        self._mPlayer.play()

    @Slot()
    def on_toolButtonForward_clicked(self):
        self._mPlayer.setPosition(
            self._mPlayer.position() + self._stepTime * 1000)

    @Slot()
    def on_toolButtonBackward_clicked(self):
        self._mPlayer.setPosition(
            self._mPlayer.position() - self._stepTime * 1000)

    def on_toolButtonVolume_clicked(self):
        if self._audioOutput.isMuted():
            self._audioOutput.setMuted(False)
            self.toolButtonVolume.setIcon(
                QPixmap(":/icons/resources/volume.svg"))
            self.toolButtonVolume.setToolTip("静音")
        else:
            self._audioOutput.setMuted(True)
            self.toolButtonVolume.setIcon(
                QPixmap(":/icons/resources/mute.svg"))
            self.toolButtonVolume.setToolTip("解除静音")

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
            self.toolButtonPlayPause.setToolTip("暂停")
        else:
            self.openGLWidgetAudioPlayShow.stop()
            self.toolButtonPlayPause.setIcon(
                QPixmap(":/icons/resources/play.svg"))
            self.toolButtonPlayPause.setToolTip("播放")
            if newState == QMediaPlayer.StoppedState:
                self.labelTimeTips.setText("00:00:00/00:00:00")
                self._audioDurationTimeStr = "00:00:00"

    @ Slot(QMediaPlayer.Error, str)
    def on_mPlayer_errorOccurred(self, error: QMediaPlayer.Error, errorString: str):
        self._toast.toast(
            pos=QPoint(self.pos().x() + self.geometry().width() // 2,
                       self.pos().y() + self.geometry().height()), toast_text=f"{self._audioFilesName[self._current_index]}:{errorString}")
        self.on_toolButtonNext_clicked()

    @Slot(int)
    def on_mPlayer_durationChanged(self, duration: int):
        self.horizontalSliderRateOfProcess.setRange(0, duration)
        self.horizontalSliderRateOfProcess.setValue(0)
        self._audioDurationTimeStr = MainWindow.millisecondsToFormatedString(
            duration)

    @Slot(int)
    def on_mPlayer_positionChanged(self, position: int):
        self.horizontalSliderRateOfProcess.setValue(position)
        self.labelTimeTips.setText(
            f"{MainWindow.millisecondsToFormatedString(position)}/{self._audioDurationTimeStr}")

    @Slot(int)
    def on_mPlayer_mediaStatusChanged(self, status: QMediaPlayer.MediaStatus):
        if status == QMediaPlayer.EndOfMedia:
            self._current_index = (self._current_index +
                                   1) % len(self._audioFilesPath)
            self._mPlayer.setSource(self._audioFilesPath[self._current_index])
            self._mPlayer.play()

    @Slot()
    def on_mPlayer_metaDataChanged(self):
        self.labelCurrentAudioName.setText(
            self._audioFilesName[self._current_index])

    @ Slot(int)
    def on_horizontalSliderVolume_valueChanged(self, value: int):
        self._audioOutput.setVolume(value / self._volume_ratio)
        self.labelVolume.setText(f"{value:<4d} %")
        self.volumeSliderWidget.volumeSlider.setValue(value)

    @Slot(int)
    def on_volumeSlider_valueChanged(self, value: int):
        self._audioOutput.setVolume(value / self._volume_ratio)
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
