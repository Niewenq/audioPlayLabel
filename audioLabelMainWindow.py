# -*- encoding: utf-8 -*-
# @Author  :   Wenqing Nie
# @File    :   audioLabelMainWindow.py
# @Time    :   2022/03/06 18:05:46


import re
from os import path
from os import listdir
from sys import exit, argv
from Ui_audioLabelMainWindow import Ui_MainWindow

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import pyqtSlot, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QSplashScreen, QFileDialog, QActionGroup, QAction


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.openGLWidgetAudioPlayShow.setupUi()

        self.ui = Ui_MainWindow()

        self.jsonFilePath = None
        self.audioFilesPath = []
        self.audioFolder = None
        self.autoSavePeriod = 0

        self.mPlayer = QMediaPlayer()
        self.mList = QMediaPlaylist()
        self.mPlayer.durationChanged.connect(self.on_mPlayer_durationChanged)
        self.mPlayer.positionChanged.connect(self.on_mPlayer_positionChanged)
        self.mPlayer.currentMediaChanged.connect(
            self.on_mPlayer_currentMediaChanged)
        self.mPlayer.stateChanged.connect(self.on_mPlayer_stateChanged)
        self.mPlayer.error.connect(self.on_mPlayer_error)

        self.labelVolume.setText(f"{self.horizontalSliderVolume.value():2} %")
        self.labelCurrentAudioName.setText("")
        self.labelTimeTips.setText("00:00:00/00:00:00")
        self.__audioDurationTimeStr = ""

        self.qActionGroupAutoSave = QActionGroup(self)
        self.qActionGroupAutoSave.addAction(self.action0s)
        self.qActionGroupAutoSave.addAction(self.action60s)
        self.qActionGroupAutoSave.addAction(self.action120s)
        self.qActionGroupAutoSave.addAction(self.action180s)
        self.qActionGroupAutoSave.addAction(self.action300s)
        self.action0s.setChecked(True)
        self.autoSavePeriod = 0

        self.qActionGroupPlayBackRate = QActionGroup(self)
        self.qActionGroupPlayBackRate.addAction(self.action0_5)
        self.qActionGroupPlayBackRate.addAction(self.action1_0)
        self.qActionGroupPlayBackRate.addAction(self.action1_5)
        self.qActionGroupPlayBackRate.addAction(self.action2_0)
        self.action1_0.setChecked(True)
        self.playBackRate = 1.0

        self.qActionGroupStepTime = QActionGroup(self)
        self.qActionGroupStepTime.addAction(self.action1s)
        self.qActionGroupStepTime.addAction(self.action3s)
        self.qActionGroupStepTime.addAction(self.action5s)
        self.qActionGroupStepTime.addAction(self.action10s)
        self.qActionGroupStepTime.addAction(self.action30s)
        self.action1s.setChecked(True)
        self.stepTime = 1

        self.qActionGroupPlayBackMode = QActionGroup(self)
        self.qActionGroupPlayBackMode.addAction(self.actionCurrentItemOnce)
        self.qActionGroupPlayBackMode.addAction(self.actionCurrentItemInLoop)
        self.qActionGroupPlayBackMode.addAction(self.actionSequential)
        self.qActionGroupPlayBackMode.addAction(self.actionLoop)
        self.qActionGroupPlayBackMode.addAction(self.actionRandom)
        self.actionLoop.setChecked(True)
        self.playBackMode = QMediaPlaylist.PlaybackMode.Loop
        self.__playBackModeDict = {
            QMediaPlaylist.PlaybackMode.CurrentItemOnce: ["CurrentItemOnce", ":/icons/resources/currentItemOnce.svg", self.actionCurrentItemOnce],
            QMediaPlaylist.PlaybackMode.CurrentItemInLoop: ["CurrentItemInLoop", ":/icons/resources/currentItemInLoop.svg", self.actionCurrentItemInLoop],
            QMediaPlaylist.PlaybackMode.Sequential: ["Sequential", ":/icons/resources/sequential.svg", self.actionSequential],
            QMediaPlaylist.PlaybackMode.Loop: ["Loop", ":/icons/resources/loop.svg", self.actionLoop],
            QMediaPlaylist.PlaybackMode.Random: ["Random", ":/icons/resources/random.svg", self.actionRandom],
        }

        self.horizontalSliderVolume.setRange(0, 100)
        self.horizontalSliderVolume.setValue(100)

        self.__update_statusbar_message()

    @staticmethod
    def millisecondsToFormatedString(milliseconds: int) -> str:
        hours, minutes = divmod(milliseconds, 3600000)
        minutes, seconds = divmod(minutes, 60000)
        seconds = seconds // 1000
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def __update_statusbar_message(self):
        self.statusbar.showMessage(
            f"AutoSave:{self.autoSavePeriod}s✦PlayBackRate:{self.playBackRate}✦StepTime:{self.stepTime}s✦PlayBackMode:{self.__playBackModeDict[self.playBackMode][0]}✦AudioFolder:{self.audioFolder}✦JsonFile:{self.jsonFilePath}")

    @ pyqtSlot()
    def on_actionOpenJsonFile_triggered(self):
        self.jsonFilePath, _ = QFileDialog.getOpenFileName(parent=self, caption='Open JSON Files',
                                                           filter='JSON Files(*.json)')
        self.__update_statusbar_message()

    @ pyqtSlot()
    def on_actionOpenAudioFolder_triggered(self):
        folder = QFileDialog.getExistingDirectory(
            self, caption='Choose A Directory')
        if folder is not None:
            audioFilesPath = [path.join(folder, file) for file in listdir(
                folder) if re.match(r".+\.wav$|.+\.mp3$|.+\.m4a$", file)]
            if audioFilesPath:
                self.audioFolder = folder
                self.mList.clear()
                for audioFilePath in audioFilesPath:
                    self.mList.addMedia(QMediaContent(
                        QUrl.fromLocalFile(audioFilePath)))
                self.mList.setPlaybackMode(self.playBackMode)
                self.mPlayer.setPlaylist(self.mList)
                self.__update_statusbar_message()
            else:
                QMessageBox.information(
                    None, "Information", f"No m4a, mp3 or wav files in Folder {folder}.")

    @ pyqtSlot(int)
    def on_horizontalSliderVolume_valueChanged(self, value):
        self.labelVolume.setText(f"{value:3} %")
        self.mPlayer.setVolume(value)

    @ pyqtSlot()
    def on_actionExit_triggered(self):
        QApplication.instance().quit()

    @pyqtSlot()
    def on_toolButtonPlayPause_clicked(self):
        if self.mPlayer.state() == QMediaPlayer.State.PlayingState:
            self.mPlayer.pause()
        else:
            self.mPlayer.play()

    @pyqtSlot()
    def on_toolButtonVolume_clicked(self):
        icon = self.toolButtonVolume.icon()
        if self.mPlayer.isMuted():
            self.mPlayer.setMuted(False)
            icon.addPixmap(QPixmap(":/icons/resources/volume.svg"),
                           QIcon.Normal, QIcon.Off)
        else:
            self.mPlayer.setMuted(True)
            icon.addPixmap(QPixmap(":/icons/resources/mute.svg"),
                           QIcon.Normal, QIcon.Off)
        self.toolButtonVolume.setIcon(icon)

    @pyqtSlot(QAction)
    def on_menuPlayBackRate_triggered(self, action: QAction):
        self.playBackRate = float(action.text())
        self.mPlayer.setPlaybackRate(self.playBackRate)
        self.__update_statusbar_message()

    @pyqtSlot(QAction)
    def on_menuAutoSave_triggered(self, action: QAction):
        self.autoSavePeriod = int(re.match(r"\d+", action.text()).group())
        self.__update_statusbar_message()

    @pyqtSlot(QAction)
    def on_menuPlayBackMode_triggered(self, action: QAction):
        self.playBackMode = int(re.match(r"\d+", action.text()).group())
        self.mList.setPlaybackMode(self.playBackMode)
        icon = self.toolButtonPlayBackMode.icon()
        icon.addPixmap(QPixmap(self.__playBackModeDict[self.playBackMode][1]),
                       QIcon.Normal, QIcon.Off)
        self.toolButtonPlayBackMode.setIcon(icon)
        self.__update_statusbar_message()

    @pyqtSlot(QAction)
    def on_menuStepTime_triggered(self, action: QAction):
        self.stepTime = int(re.match(r"\d+", action.text()).group())
        self.__update_statusbar_message()

    def on_mPlayer_durationChanged(self, duration: int):
        self.horizontalSliderRateOfProcess.setRange(0, duration)
        self.horizontalSliderRateOfProcess.setValue(0)
        self.__audioDurationTimeStr = MainWindow.millisecondsToFormatedString(
            duration)

    def on_mPlayer_positionChanged(self, position: int):
        self.horizontalSliderRateOfProcess.setValue(position)
        self.labelTimeTips.setText(
            f"{MainWindow.millisecondsToFormatedString(position)}/{self.__audioDurationTimeStr}")

    def on_mPlayer_currentMediaChanged(self, media: QMediaContent):
        if media.resources():
            self.labelCurrentAudioName.setText(
                media.resources()[0].url().fileName())

    def on_mPlayer_stateChanged(self, state: QMediaPlayer.State):
        icon = self.toolButtonPlayPause.icon()
        if state == QMediaPlayer.State.PlayingState:
            icon.addPixmap(QPixmap(":/icons/resources/pause.svg"),
                           QIcon.Normal, QIcon.Off)
            self.openGLWidgetAudioPlayShow.start()
        else:
            icon.addPixmap(
                QPixmap(":/icons/resources/play.svg"))
            self.openGLWidgetAudioPlayShow.stop()
        self.toolButtonPlayPause.setIcon(icon)

    def on_mPlayer_error(self, error: QMediaPlayer.Error):
        print(error)

    @pyqtSlot()
    def on_toolButtonBackward_clicked(self):
        self.mPlayer.setPosition(
            self.mPlayer.position() - self.stepTime * 1000)

    @pyqtSlot()
    def on_toolButtonForward_clicked(self):
        self.mPlayer.setPosition(
            self.mPlayer.position() + self.stepTime * 1000)

    @pyqtSlot()
    def on_toolButtonPlayBackMode_clicked(self):
        self.playBackMode = (self.playBackMode + 1) % 5
        self.mList.setPlaybackMode(self.playBackMode)

        self.__playBackModeDict[self.playBackMode][2].setChecked(True)

        icon = self.toolButtonPlayBackMode.icon()
        icon.addPixmap(QPixmap(self.__playBackModeDict[self.playBackMode][1]),
                       QIcon.Normal, QIcon.Off)
        self.toolButtonPlayBackMode.setIcon(icon)

        self.__update_statusbar_message()

    @pyqtSlot()
    def on_toolButtonStop_clicked(self):
        self.mPlayer.stop()
        self.labelTimeTips.setText("00:00:00/00:00:00")

    @pyqtSlot()
    def on_toolButtonPre_clicked(self):
        self.mList.setCurrentIndex(self.mList.previousIndex())

    @pyqtSlot()
    def on_toolButtonNext_clicked(self):
        self.mList.setCurrentIndex(self.mList.nextIndex())

        print(self.__playBackModeDict[self.mList.playbackMode()][0])


if __name__ == "__main__":
    app = QApplication(argv)
    splash = QSplashScreen(QPixmap(":/icons/resources/owl.svg"))
    splash.show()
    ui = MainWindow()
    ui.show()
    splash.finish(ui)
    exit(app.exec_())
