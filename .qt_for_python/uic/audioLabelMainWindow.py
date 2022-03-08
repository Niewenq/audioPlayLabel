/********************************************************************************
** Form generated from reading UI file 'audioLabelMainWindow.ui'
**
** Created by: Qt User Interface Compiler version 6.2.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef AUDIOLABELMAINWINDOW_H
#define AUDIOLABELMAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QIcon>
#include <QtOpenGLWidgets/QOpenGLWidget>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QSlider>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionOpenFile;
    QAction *actionOpenAudioFolder;
    QAction *action12;
    QAction *actionSave;
    QAction *actionSaveAs;
    QAction *action0s;
    QAction *action60s;
    QAction *action120s;
    QAction *action180s;
    QAction *action300s;
    QAction *actionUserDefined;
    QAction *actionGetStarted;
    QAction *actionAbout;
    QAction *actionOpenAudioFiles;
    QAction *actionOpenJsonFile;
    QAction *actionExit;
    QAction *action0point25;
    QAction *action0point5;
    QAction *action0point75;
    QAction *action1point0;
    QAction *action1point25;
    QAction *action1point5;
    QAction *action1point75;
    QAction *action2point0;
    QAction *action2point5;
    QAction *action5s;
    QAction *action1s;
    QAction *action3s;
    QAction *action0_5;
    QAction *action0_75;
    QAction *action1_0;
    QAction *action1_25;
    QAction *action1_75;
    QAction *action1_5;
    QAction *action2_0;
    QAction *action2_5;
    QAction *action10s;
    QAction *action30s;
    QAction *actionCurrentItemOnce;
    QAction *actionCurrentItemInLoop;
    QAction *actionSequential;
    QAction *actionLoop;
    QAction *actionRandom;
    QWidget *centralwidgetMain;
    QVBoxLayout *verticalLayout;
    QSplitter *splitter;
    QListWidget *listWidgetAudioList;
    QWidget *layoutWidget;
    QVBoxLayout *verticalLayoutAudioMainArea;
    QLabel *labelCurrentAudioName;
    QOpenGLWidget *openGLWidgetAudioPlayShow;
    QSlider *horizontalSliderRateOfProcess;
    QHBoxLayout *horizontalLayoutAudioOperationArea;
    QLabel *labelTimeTips;
    QSpacerItem *horizontalSpacerLeft;
    QToolButton *toolButtonPlayBackMode;
    QToolButton *toolButtonStop;
    QToolButton *toolButtonPre;
    QToolButton *toolButtonBackward;
    QToolButton *toolButtonPlayPause;
    QToolButton *toolButtonForward;
    QToolButton *toolButtonNext;
    QToolButton *toolButtonVolume;
    QSlider *horizontalSliderVolume;
    QLabel *labelVolume;
    QSpacerItem *horizontalSpacerRight;
    QMenuBar *menubar;
    QMenu *menuFile;
    QMenu *menuOpenRecently;
    QMenu *menuAutoSave;
    QMenu *menuHelp;
    QMenu *menuSettings;
    QMenu *menuStepTime;
    QMenu *menuPlayBackRate;
    QMenu *menuPlayBackMode;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(900, 617);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icons/resources/owl.svg"), QSize(), QIcon::Normal, QIcon::Off);
        MainWindow->setWindowIcon(icon);
        actionOpenFile = new QAction(MainWindow);
        actionOpenFile->setObjectName(QString::fromUtf8("actionOpenFile"));
        actionOpenAudioFolder = new QAction(MainWindow);
        actionOpenAudioFolder->setObjectName(QString::fromUtf8("actionOpenAudioFolder"));
        action12 = new QAction(MainWindow);
        action12->setObjectName(QString::fromUtf8("action12"));
        actionSave = new QAction(MainWindow);
        actionSave->setObjectName(QString::fromUtf8("actionSave"));
        actionSaveAs = new QAction(MainWindow);
        actionSaveAs->setObjectName(QString::fromUtf8("actionSaveAs"));
        action0s = new QAction(MainWindow);
        action0s->setObjectName(QString::fromUtf8("action0s"));
        action0s->setCheckable(true);
        action60s = new QAction(MainWindow);
        action60s->setObjectName(QString::fromUtf8("action60s"));
        action60s->setCheckable(true);
        action120s = new QAction(MainWindow);
        action120s->setObjectName(QString::fromUtf8("action120s"));
        action120s->setCheckable(true);
        action180s = new QAction(MainWindow);
        action180s->setObjectName(QString::fromUtf8("action180s"));
        action180s->setCheckable(true);
        action180s->setChecked(false);
        action300s = new QAction(MainWindow);
        action300s->setObjectName(QString::fromUtf8("action300s"));
        action300s->setCheckable(true);
        actionUserDefined = new QAction(MainWindow);
        actionUserDefined->setObjectName(QString::fromUtf8("actionUserDefined"));
        actionUserDefined->setCheckable(true);
        actionGetStarted = new QAction(MainWindow);
        actionGetStarted->setObjectName(QString::fromUtf8("actionGetStarted"));
        actionAbout = new QAction(MainWindow);
        actionAbout->setObjectName(QString::fromUtf8("actionAbout"));
        actionOpenAudioFiles = new QAction(MainWindow);
        actionOpenAudioFiles->setObjectName(QString::fromUtf8("actionOpenAudioFiles"));
        actionOpenJsonFile = new QAction(MainWindow);
        actionOpenJsonFile->setObjectName(QString::fromUtf8("actionOpenJsonFile"));
        actionExit = new QAction(MainWindow);
        actionExit->setObjectName(QString::fromUtf8("actionExit"));
        action0point25 = new QAction(MainWindow);
        action0point25->setObjectName(QString::fromUtf8("action0point25"));
        action0point25->setCheckable(true);
        action0point5 = new QAction(MainWindow);
        action0point5->setObjectName(QString::fromUtf8("action0point5"));
        action0point5->setCheckable(true);
        action0point75 = new QAction(MainWindow);
        action0point75->setObjectName(QString::fromUtf8("action0point75"));
        action0point75->setCheckable(true);
        action1point0 = new QAction(MainWindow);
        action1point0->setObjectName(QString::fromUtf8("action1point0"));
        action1point0->setCheckable(true);
        action1point25 = new QAction(MainWindow);
        action1point25->setObjectName(QString::fromUtf8("action1point25"));
        action1point25->setCheckable(true);
        action1point5 = new QAction(MainWindow);
        action1point5->setObjectName(QString::fromUtf8("action1point5"));
        action1point5->setCheckable(true);
        action1point75 = new QAction(MainWindow);
        action1point75->setObjectName(QString::fromUtf8("action1point75"));
        action1point75->setCheckable(true);
        action2point0 = new QAction(MainWindow);
        action2point0->setObjectName(QString::fromUtf8("action2point0"));
        action2point0->setCheckable(true);
        action2point5 = new QAction(MainWindow);
        action2point5->setObjectName(QString::fromUtf8("action2point5"));
        action2point5->setCheckable(true);
        action5s = new QAction(MainWindow);
        action5s->setObjectName(QString::fromUtf8("action5s"));
        action5s->setCheckable(true);
        action1s = new QAction(MainWindow);
        action1s->setObjectName(QString::fromUtf8("action1s"));
        action1s->setCheckable(true);
        action3s = new QAction(MainWindow);
        action3s->setObjectName(QString::fromUtf8("action3s"));
        action3s->setCheckable(true);
        action0_5 = new QAction(MainWindow);
        action0_5->setObjectName(QString::fromUtf8("action0_5"));
        action0_5->setCheckable(true);
        action0_75 = new QAction(MainWindow);
        action0_75->setObjectName(QString::fromUtf8("action0_75"));
        action1_0 = new QAction(MainWindow);
        action1_0->setObjectName(QString::fromUtf8("action1_0"));
        action1_0->setCheckable(true);
        action1_25 = new QAction(MainWindow);
        action1_25->setObjectName(QString::fromUtf8("action1_25"));
        action1_75 = new QAction(MainWindow);
        action1_75->setObjectName(QString::fromUtf8("action1_75"));
        action1_5 = new QAction(MainWindow);
        action1_5->setObjectName(QString::fromUtf8("action1_5"));
        action1_5->setCheckable(true);
        action2_0 = new QAction(MainWindow);
        action2_0->setObjectName(QString::fromUtf8("action2_0"));
        action2_0->setCheckable(true);
        action2_5 = new QAction(MainWindow);
        action2_5->setObjectName(QString::fromUtf8("action2_5"));
        action10s = new QAction(MainWindow);
        action10s->setObjectName(QString::fromUtf8("action10s"));
        action10s->setCheckable(true);
        action30s = new QAction(MainWindow);
        action30s->setObjectName(QString::fromUtf8("action30s"));
        action30s->setCheckable(true);
        actionCurrentItemOnce = new QAction(MainWindow);
        actionCurrentItemOnce->setObjectName(QString::fromUtf8("actionCurrentItemOnce"));
        actionCurrentItemOnce->setCheckable(true);
        actionCurrentItemInLoop = new QAction(MainWindow);
        actionCurrentItemInLoop->setObjectName(QString::fromUtf8("actionCurrentItemInLoop"));
        actionCurrentItemInLoop->setCheckable(true);
        actionSequential = new QAction(MainWindow);
        actionSequential->setObjectName(QString::fromUtf8("actionSequential"));
        actionSequential->setCheckable(true);
        actionLoop = new QAction(MainWindow);
        actionLoop->setObjectName(QString::fromUtf8("actionLoop"));
        actionLoop->setCheckable(true);
        actionRandom = new QAction(MainWindow);
        actionRandom->setObjectName(QString::fromUtf8("actionRandom"));
        actionRandom->setCheckable(true);
        centralwidgetMain = new QWidget(MainWindow);
        centralwidgetMain->setObjectName(QString::fromUtf8("centralwidgetMain"));
        verticalLayout = new QVBoxLayout(centralwidgetMain);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        splitter = new QSplitter(centralwidgetMain);
        splitter->setObjectName(QString::fromUtf8("splitter"));
        splitter->setOrientation(Qt::Horizontal);
        listWidgetAudioList = new QListWidget(splitter);
        listWidgetAudioList->setObjectName(QString::fromUtf8("listWidgetAudioList"));
        splitter->addWidget(listWidgetAudioList);
        layoutWidget = new QWidget(splitter);
        layoutWidget->setObjectName(QString::fromUtf8("layoutWidget"));
        verticalLayoutAudioMainArea = new QVBoxLayout(layoutWidget);
        verticalLayoutAudioMainArea->setObjectName(QString::fromUtf8("verticalLayoutAudioMainArea"));
        verticalLayoutAudioMainArea->setContentsMargins(0, 0, 0, 0);
        labelCurrentAudioName = new QLabel(layoutWidget);
        labelCurrentAudioName->setObjectName(QString::fromUtf8("labelCurrentAudioName"));
        labelCurrentAudioName->setAlignment(Qt::AlignCenter);

        verticalLayoutAudioMainArea->addWidget(labelCurrentAudioName);

        openGLWidgetAudioPlayShow = new QOpenGLWidget(layoutWidget);
        openGLWidgetAudioPlayShow->setObjectName(QString::fromUtf8("openGLWidgetAudioPlayShow"));

        verticalLayoutAudioMainArea->addWidget(openGLWidgetAudioPlayShow);

        horizontalSliderRateOfProcess = new QSlider(layoutWidget);
        horizontalSliderRateOfProcess->setObjectName(QString::fromUtf8("horizontalSliderRateOfProcess"));
        horizontalSliderRateOfProcess->setOrientation(Qt::Horizontal);

        verticalLayoutAudioMainArea->addWidget(horizontalSliderRateOfProcess);

        horizontalLayoutAudioOperationArea = new QHBoxLayout();
        horizontalLayoutAudioOperationArea->setObjectName(QString::fromUtf8("horizontalLayoutAudioOperationArea"));
        labelTimeTips = new QLabel(layoutWidget);
        labelTimeTips->setObjectName(QString::fromUtf8("labelTimeTips"));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(labelTimeTips->sizePolicy().hasHeightForWidth());
        labelTimeTips->setSizePolicy(sizePolicy);

        horizontalLayoutAudioOperationArea->addWidget(labelTimeTips);

        horizontalSpacerLeft = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayoutAudioOperationArea->addItem(horizontalSpacerLeft);

        toolButtonPlayBackMode = new QToolButton(layoutWidget);
        toolButtonPlayBackMode->setObjectName(QString::fromUtf8("toolButtonPlayBackMode"));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/icons/resources/loop.svg"), QSize(), QIcon::Normal, QIcon::Off);
        toolButtonPlayBackMode->setIcon(icon1);
        toolButtonPlayBackMode->setIconSize(QSize(30, 30));

        horizontalLayoutAudioOperationArea->addWidget(toolButtonPlayBackMode);

        toolButtonStop = new QToolButton(layoutWidget);
        toolButtonStop->setObjectName(QString::fromUtf8("toolButtonStop"));
        toolButtonStop->setCursor(QCursor(Qt::PointingHandCursor));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/icons/resources/stop.svg"), QSize(), QIcon::Normal, QIcon::Off);
        toolButtonStop->setIcon(icon2);
        toolButtonStop->setIconSize(QSize(30, 30));

        horizontalLayoutAudioOperationArea->addWidget(toolButtonStop);

        toolButtonPre = new QToolButton(layoutWidget);
        toolButtonPre->setObjectName(QString::fromUtf8("toolButtonPre"));
        toolButtonPre->setCursor(QCursor(Qt::PointingHandCursor));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/icons/resources/pre.svg"), QSize(), QIcon::Normal, QIcon::Off);
        toolButtonPre->setIcon(icon3);
        toolButtonPre->setIconSize(QSize(30, 30));

        horizontalLayoutAudioOperationArea->addWidget(toolButtonPre);

        toolButtonBackward = new QToolButton(layoutWidget);
        toolButtonBackward->setObjectName(QString::fromUtf8("toolButtonBackward"));
        toolButtonBackward->setCursor(QCursor(Qt::PointingHandCursor));
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/icons/resources/backward.svg"), QSize(), QIcon::Normal, QIcon::Off);
        toolButtonBackward->setIcon(icon4);
        toolButtonBackward->setIconSize(QSize(30, 30));

        horizontalLayoutAudioOperationArea->addWidget(toolButtonBackward);

        toolButtonPlayPause = new QToolButton(layoutWidget);
        toolButtonPlayPause->setObjectName(QString::fromUtf8("toolButtonPlayPause"));
        toolButtonPlayPause->setCursor(QCursor(Qt::PointingHandCursor));
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/icons/resources/play.svg"), QSize(), QIcon::Normal, QIcon::Off);
        toolButtonPlayPause->setIcon(icon5);
        toolButtonPlayPause->setIconSize(QSize(50, 50));

        horizontalLayoutAudioOperationArea->addWidget(toolButtonPlayPause);

        toolButtonForward = new QToolButton(layoutWidget);
        toolButtonForward->setObjectName(QString::fromUtf8("toolButtonForward"));
        toolButtonForward->setCursor(QCursor(Qt::PointingHandCursor));
        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/icons/resources/forward.svg"), QSize(), QIcon::Normal, QIcon::Off);
        toolButtonForward->setIcon(icon6);
        toolButtonForward->setIconSize(QSize(30, 30));

        horizontalLayoutAudioOperationArea->addWidget(toolButtonForward);

        toolButtonNext = new QToolButton(layoutWidget);
        toolButtonNext->setObjectName(QString::fromUtf8("toolButtonNext"));
        toolButtonNext->setCursor(QCursor(Qt::PointingHandCursor));
        QIcon icon7;
        icon7.addFile(QString::fromUtf8(":/icons/resources/next.svg"), QSize(), QIcon::Normal, QIcon::Off);
        toolButtonNext->setIcon(icon7);
        toolButtonNext->setIconSize(QSize(30, 30));

        horizontalLayoutAudioOperationArea->addWidget(toolButtonNext);

        toolButtonVolume = new QToolButton(layoutWidget);
        toolButtonVolume->setObjectName(QString::fromUtf8("toolButtonVolume"));
        toolButtonVolume->setCursor(QCursor(Qt::PointingHandCursor));
        QIcon icon8;
        icon8.addFile(QString::fromUtf8(":/icons/resources/volume.svg"), QSize(), QIcon::Normal, QIcon::Off);
        toolButtonVolume->setIcon(icon8);
        toolButtonVolume->setIconSize(QSize(30, 30));
        toolButtonVolume->setAutoRaise(false);
        toolButtonVolume->setArrowType(Qt::NoArrow);

        horizontalLayoutAudioOperationArea->addWidget(toolButtonVolume);

        horizontalSliderVolume = new QSlider(layoutWidget);
        horizontalSliderVolume->setObjectName(QString::fromUtf8("horizontalSliderVolume"));
        horizontalSliderVolume->setCursor(QCursor(Qt::PointingHandCursor));
        horizontalSliderVolume->setOrientation(Qt::Horizontal);

        horizontalLayoutAudioOperationArea->addWidget(horizontalSliderVolume);

        labelVolume = new QLabel(layoutWidget);
        labelVolume->setObjectName(QString::fromUtf8("labelVolume"));

        horizontalLayoutAudioOperationArea->addWidget(labelVolume);

        horizontalSpacerRight = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayoutAudioOperationArea->addItem(horizontalSpacerRight);


        verticalLayoutAudioMainArea->addLayout(horizontalLayoutAudioOperationArea);

        verticalLayoutAudioMainArea->setStretch(1, 1);
        splitter->addWidget(layoutWidget);

        verticalLayout->addWidget(splitter);

        MainWindow->setCentralWidget(centralwidgetMain);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 900, 26));
        menuFile = new QMenu(menubar);
        menuFile->setObjectName(QString::fromUtf8("menuFile"));
        menuOpenRecently = new QMenu(menuFile);
        menuOpenRecently->setObjectName(QString::fromUtf8("menuOpenRecently"));
        menuAutoSave = new QMenu(menuFile);
        menuAutoSave->setObjectName(QString::fromUtf8("menuAutoSave"));
        menuHelp = new QMenu(menubar);
        menuHelp->setObjectName(QString::fromUtf8("menuHelp"));
        menuSettings = new QMenu(menubar);
        menuSettings->setObjectName(QString::fromUtf8("menuSettings"));
        menuStepTime = new QMenu(menuSettings);
        menuStepTime->setObjectName(QString::fromUtf8("menuStepTime"));
        menuPlayBackRate = new QMenu(menuSettings);
        menuPlayBackRate->setObjectName(QString::fromUtf8("menuPlayBackRate"));
        menuPlayBackMode = new QMenu(menuSettings);
        menuPlayBackMode->setObjectName(QString::fromUtf8("menuPlayBackMode"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuFile->menuAction());
        menubar->addAction(menuSettings->menuAction());
        menubar->addAction(menuHelp->menuAction());
        menuFile->addAction(actionOpenJsonFile);
        menuFile->addAction(actionOpenAudioFolder);
        menuFile->addAction(menuOpenRecently->menuAction());
        menuFile->addSeparator();
        menuFile->addAction(actionSave);
        menuFile->addAction(actionSaveAs);
        menuFile->addAction(menuAutoSave->menuAction());
        menuFile->addSeparator();
        menuFile->addAction(actionExit);
        menuAutoSave->addAction(action0s);
        menuAutoSave->addAction(action60s);
        menuAutoSave->addAction(action120s);
        menuAutoSave->addAction(action180s);
        menuAutoSave->addAction(action300s);
        menuHelp->addAction(actionGetStarted);
        menuHelp->addAction(actionAbout);
        menuSettings->addAction(menuStepTime->menuAction());
        menuSettings->addAction(menuPlayBackRate->menuAction());
        menuSettings->addAction(menuPlayBackMode->menuAction());
        menuStepTime->addAction(action1s);
        menuStepTime->addAction(action3s);
        menuStepTime->addAction(action5s);
        menuStepTime->addAction(action10s);
        menuStepTime->addAction(action30s);
        menuPlayBackRate->addAction(action0_5);
        menuPlayBackRate->addAction(action1_0);
        menuPlayBackRate->addAction(action1_5);
        menuPlayBackRate->addAction(action2_0);
        menuPlayBackMode->addAction(actionCurrentItemOnce);
        menuPlayBackMode->addAction(actionCurrentItemInLoop);
        menuPlayBackMode->addAction(actionSequential);
        menuPlayBackMode->addAction(actionLoop);
        menuPlayBackMode->addAction(actionRandom);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "AudioLabel", nullptr));
        actionOpenFile->setText(QCoreApplication::translate("MainWindow", "Open File...", nullptr));
#if QT_CONFIG(shortcut)
        actionOpenFile->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+O", nullptr));
#endif // QT_CONFIG(shortcut)
        actionOpenAudioFolder->setText(QCoreApplication::translate("MainWindow", "Open Audio Folder", nullptr));
#if QT_CONFIG(shortcut)
        actionOpenAudioFolder->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+O", nullptr));
#endif // QT_CONFIG(shortcut)
        action12->setText(QCoreApplication::translate("MainWindow", "12", nullptr));
        actionSave->setText(QCoreApplication::translate("MainWindow", "Save", nullptr));
#if QT_CONFIG(shortcut)
        actionSave->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+S", nullptr));
#endif // QT_CONFIG(shortcut)
        actionSaveAs->setText(QCoreApplication::translate("MainWindow", "Save As...", nullptr));
#if QT_CONFIG(shortcut)
        actionSaveAs->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+Shift+S", nullptr));
#endif // QT_CONFIG(shortcut)
        action0s->setText(QCoreApplication::translate("MainWindow", "0 s", nullptr));
        action60s->setText(QCoreApplication::translate("MainWindow", "60 s", nullptr));
        action120s->setText(QCoreApplication::translate("MainWindow", "120 s", nullptr));
        action180s->setText(QCoreApplication::translate("MainWindow", "180 s", nullptr));
        action300s->setText(QCoreApplication::translate("MainWindow", "300 s", nullptr));
        actionUserDefined->setText(QCoreApplication::translate("MainWindow", "User Defined", nullptr));
        actionGetStarted->setText(QCoreApplication::translate("MainWindow", "Get Started", nullptr));
        actionAbout->setText(QCoreApplication::translate("MainWindow", "About", nullptr));
        actionOpenAudioFiles->setText(QCoreApplication::translate("MainWindow", "Open Audio Files", nullptr));
#if QT_CONFIG(shortcut)
        actionOpenAudioFiles->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+O", nullptr));
#endif // QT_CONFIG(shortcut)
        actionOpenJsonFile->setText(QCoreApplication::translate("MainWindow", "Open Json File", nullptr));
#if QT_CONFIG(shortcut)
        actionOpenJsonFile->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+J", nullptr));
#endif // QT_CONFIG(shortcut)
        actionExit->setText(QCoreApplication::translate("MainWindow", "Exit", nullptr));
#if QT_CONFIG(shortcut)
        actionExit->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+Q", nullptr));
#endif // QT_CONFIG(shortcut)
        action0point25->setText(QCoreApplication::translate("MainWindow", "0.25", nullptr));
        action0point5->setText(QCoreApplication::translate("MainWindow", "0.5", nullptr));
        action0point75->setText(QCoreApplication::translate("MainWindow", "0.75", nullptr));
        action1point0->setText(QCoreApplication::translate("MainWindow", "1.0", nullptr));
        action1point25->setText(QCoreApplication::translate("MainWindow", "1.25", nullptr));
        action1point5->setText(QCoreApplication::translate("MainWindow", "1.5", nullptr));
        action1point75->setText(QCoreApplication::translate("MainWindow", "1.75", nullptr));
        action2point0->setText(QCoreApplication::translate("MainWindow", "2.0", nullptr));
        action2point5->setText(QCoreApplication::translate("MainWindow", "2.5", nullptr));
        action5s->setText(QCoreApplication::translate("MainWindow", "5 s", nullptr));
        action1s->setText(QCoreApplication::translate("MainWindow", "1 s", nullptr));
        action3s->setText(QCoreApplication::translate("MainWindow", "3 s", nullptr));
        action0_5->setText(QCoreApplication::translate("MainWindow", "0.5", nullptr));
        action0_75->setText(QCoreApplication::translate("MainWindow", "0.75", nullptr));
        action1_0->setText(QCoreApplication::translate("MainWindow", "1.0", nullptr));
        action1_25->setText(QCoreApplication::translate("MainWindow", "1.25", nullptr));
        action1_75->setText(QCoreApplication::translate("MainWindow", "1.75", nullptr));
        action1_5->setText(QCoreApplication::translate("MainWindow", "1.5", nullptr));
        action2_0->setText(QCoreApplication::translate("MainWindow", "2.0", nullptr));
        action2_5->setText(QCoreApplication::translate("MainWindow", "2.5", nullptr));
        action10s->setText(QCoreApplication::translate("MainWindow", "10 s", nullptr));
        action30s->setText(QCoreApplication::translate("MainWindow", "30 s", nullptr));
        actionCurrentItemOnce->setText(QCoreApplication::translate("MainWindow", "0 Current Item Once", nullptr));
        actionCurrentItemInLoop->setText(QCoreApplication::translate("MainWindow", "1 Current Item In Loop", nullptr));
        actionSequential->setText(QCoreApplication::translate("MainWindow", "2 Sequential", nullptr));
        actionLoop->setText(QCoreApplication::translate("MainWindow", "3 Loop", nullptr));
        actionRandom->setText(QCoreApplication::translate("MainWindow", "4 Random", nullptr));
        labelCurrentAudioName->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        labelTimeTips->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        toolButtonPlayBackMode->setText(QCoreApplication::translate("MainWindow", "...", nullptr));
        toolButtonStop->setText(QCoreApplication::translate("MainWindow", "...", nullptr));
        toolButtonPre->setText(QCoreApplication::translate("MainWindow", "...", nullptr));
#if QT_CONFIG(shortcut)
        toolButtonPre->setShortcut(QCoreApplication::translate("MainWindow", "Up", nullptr));
#endif // QT_CONFIG(shortcut)
        toolButtonBackward->setText(QCoreApplication::translate("MainWindow", "...", nullptr));
#if QT_CONFIG(shortcut)
        toolButtonBackward->setShortcut(QCoreApplication::translate("MainWindow", "Left", nullptr));
#endif // QT_CONFIG(shortcut)
        toolButtonPlayPause->setText(QCoreApplication::translate("MainWindow", "...", nullptr));
#if QT_CONFIG(shortcut)
        toolButtonPlayPause->setShortcut(QCoreApplication::translate("MainWindow", "Space", nullptr));
#endif // QT_CONFIG(shortcut)
        toolButtonForward->setText(QCoreApplication::translate("MainWindow", "...", nullptr));
#if QT_CONFIG(shortcut)
        toolButtonForward->setShortcut(QCoreApplication::translate("MainWindow", "Right", nullptr));
#endif // QT_CONFIG(shortcut)
        toolButtonNext->setText(QCoreApplication::translate("MainWindow", "...", nullptr));
#if QT_CONFIG(shortcut)
        toolButtonNext->setShortcut(QCoreApplication::translate("MainWindow", "Down", nullptr));
#endif // QT_CONFIG(shortcut)
        toolButtonVolume->setText(QCoreApplication::translate("MainWindow", "...", nullptr));
        labelVolume->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        menuFile->setTitle(QCoreApplication::translate("MainWindow", "File", nullptr));
        menuOpenRecently->setTitle(QCoreApplication::translate("MainWindow", "Open Recently", nullptr));
        menuAutoSave->setTitle(QCoreApplication::translate("MainWindow", "Auto Save", nullptr));
        menuHelp->setTitle(QCoreApplication::translate("MainWindow", "Help", nullptr));
        menuSettings->setTitle(QCoreApplication::translate("MainWindow", "Settings", nullptr));
        menuStepTime->setTitle(QCoreApplication::translate("MainWindow", "Step Time", nullptr));
        menuPlayBackRate->setTitle(QCoreApplication::translate("MainWindow", "Play Back Rate", nullptr));
        menuPlayBackMode->setTitle(QCoreApplication::translate("MainWindow", "Play Back Mode", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // AUDIOLABELMAINWINDOW_H
