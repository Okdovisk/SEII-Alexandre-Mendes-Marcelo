/********************************************************************************
** Form generated from reading UI file 'calculadora.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CALCULADORA_H
#define UI_CALCULADORA_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Calculadora
{
public:
    QWidget *centralwidget;
    QGridLayout *gridLayout;
    QPushButton *MemoriaSbt;
    QPushButton *Adicao;
    QPushButton *Botao5;
    QPushButton *Botao3;
    QPushButton *Divisao;
    QPushButton *Botao9;
    QPushButton *Botao7;
    QPushButton *Botao8;
    QPushButton *Botao6;
    QPushButton *Botao1;
    QPushButton *MemoriaAdc;
    QPushButton *Multiplicacao;
    QPushButton *Botao2;
    QPushButton *Memoria;
    QPushButton *Botao4;
    QPushButton *Limpar;
    QPushButton *Botao0;
    QPushButton *TrocarSinal;
    QPushButton *Subtracao;
    QPushButton *Igual;
    QLineEdit *Display;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *Calculadora)
    {
        if (Calculadora->objectName().isEmpty())
            Calculadora->setObjectName(QString::fromUtf8("Calculadora"));
        Calculadora->resize(512, 288);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(Calculadora->sizePolicy().hasHeightForWidth());
        Calculadora->setSizePolicy(sizePolicy);
        centralwidget = new QWidget(Calculadora);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayout = new QGridLayout(centralwidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        MemoriaSbt = new QPushButton(centralwidget);
        MemoriaSbt->setObjectName(QString::fromUtf8("MemoriaSbt"));
        sizePolicy.setHeightForWidth(MemoriaSbt->sizePolicy().hasHeightForWidth());
        MemoriaSbt->setSizePolicy(sizePolicy);
        MemoriaSbt->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #FFBC00;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(MemoriaSbt, 2, 4, 1, 1);

        Adicao = new QPushButton(centralwidget);
        Adicao->setObjectName(QString::fromUtf8("Adicao"));
        sizePolicy.setHeightForWidth(Adicao->sizePolicy().hasHeightForWidth());
        Adicao->setSizePolicy(sizePolicy);
        Adicao->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #FFBC00;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Adicao, 3, 3, 1, 1);

        Botao5 = new QPushButton(centralwidget);
        Botao5->setObjectName(QString::fromUtf8("Botao5"));
        sizePolicy.setHeightForWidth(Botao5->sizePolicy().hasHeightForWidth());
        Botao5->setSizePolicy(sizePolicy);
        Botao5->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #C0C0C0;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Botao5, 2, 1, 1, 1);

        Botao3 = new QPushButton(centralwidget);
        Botao3->setObjectName(QString::fromUtf8("Botao3"));
        sizePolicy.setHeightForWidth(Botao3->sizePolicy().hasHeightForWidth());
        Botao3->setSizePolicy(sizePolicy);
        Botao3->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #C0C0C0;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Botao3, 3, 2, 1, 1);

        Divisao = new QPushButton(centralwidget);
        Divisao->setObjectName(QString::fromUtf8("Divisao"));
        sizePolicy.setHeightForWidth(Divisao->sizePolicy().hasHeightForWidth());
        Divisao->setSizePolicy(sizePolicy);
        Divisao->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #FFBC00;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Divisao, 1, 3, 1, 1);

        Botao9 = new QPushButton(centralwidget);
        Botao9->setObjectName(QString::fromUtf8("Botao9"));
        sizePolicy.setHeightForWidth(Botao9->sizePolicy().hasHeightForWidth());
        Botao9->setSizePolicy(sizePolicy);
        Botao9->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #C0C0C0;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Botao9, 1, 2, 1, 1);

        Botao7 = new QPushButton(centralwidget);
        Botao7->setObjectName(QString::fromUtf8("Botao7"));
        sizePolicy.setHeightForWidth(Botao7->sizePolicy().hasHeightForWidth());
        Botao7->setSizePolicy(sizePolicy);
        Botao7->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #C0C0C0;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Botao7, 1, 0, 1, 1);

        Botao8 = new QPushButton(centralwidget);
        Botao8->setObjectName(QString::fromUtf8("Botao8"));
        sizePolicy.setHeightForWidth(Botao8->sizePolicy().hasHeightForWidth());
        Botao8->setSizePolicy(sizePolicy);
        Botao8->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #C0C0C0;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Botao8, 1, 1, 1, 1);

        Botao6 = new QPushButton(centralwidget);
        Botao6->setObjectName(QString::fromUtf8("Botao6"));
        sizePolicy.setHeightForWidth(Botao6->sizePolicy().hasHeightForWidth());
        Botao6->setSizePolicy(sizePolicy);
        Botao6->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #C0C0C0;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Botao6, 2, 2, 1, 1);

        Botao1 = new QPushButton(centralwidget);
        Botao1->setObjectName(QString::fromUtf8("Botao1"));
        sizePolicy.setHeightForWidth(Botao1->sizePolicy().hasHeightForWidth());
        Botao1->setSizePolicy(sizePolicy);
        Botao1->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #C0C0C0;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Botao1, 3, 0, 1, 1);

        MemoriaAdc = new QPushButton(centralwidget);
        MemoriaAdc->setObjectName(QString::fromUtf8("MemoriaAdc"));
        sizePolicy.setHeightForWidth(MemoriaAdc->sizePolicy().hasHeightForWidth());
        MemoriaAdc->setSizePolicy(sizePolicy);
        MemoriaAdc->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #FFBC00;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(MemoriaAdc, 1, 4, 1, 1);

        Multiplicacao = new QPushButton(centralwidget);
        Multiplicacao->setObjectName(QString::fromUtf8("Multiplicacao"));
        sizePolicy.setHeightForWidth(Multiplicacao->sizePolicy().hasHeightForWidth());
        Multiplicacao->setSizePolicy(sizePolicy);
        Multiplicacao->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #FFBC00;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Multiplicacao, 2, 3, 1, 1);

        Botao2 = new QPushButton(centralwidget);
        Botao2->setObjectName(QString::fromUtf8("Botao2"));
        sizePolicy.setHeightForWidth(Botao2->sizePolicy().hasHeightForWidth());
        Botao2->setSizePolicy(sizePolicy);
        Botao2->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #C0C0C0;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Botao2, 3, 1, 1, 1);

        Memoria = new QPushButton(centralwidget);
        Memoria->setObjectName(QString::fromUtf8("Memoria"));
        sizePolicy.setHeightForWidth(Memoria->sizePolicy().hasHeightForWidth());
        Memoria->setSizePolicy(sizePolicy);
        Memoria->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #FFBC00;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Memoria, 3, 4, 1, 1);

        Botao4 = new QPushButton(centralwidget);
        Botao4->setObjectName(QString::fromUtf8("Botao4"));
        sizePolicy.setHeightForWidth(Botao4->sizePolicy().hasHeightForWidth());
        Botao4->setSizePolicy(sizePolicy);
        Botao4->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #C0C0C0;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Botao4, 2, 0, 1, 1);

        Limpar = new QPushButton(centralwidget);
        Limpar->setObjectName(QString::fromUtf8("Limpar"));
        sizePolicy.setHeightForWidth(Limpar->sizePolicy().hasHeightForWidth());
        Limpar->setSizePolicy(sizePolicy);
        Limpar->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #FF0000;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Limpar, 4, 0, 1, 1);

        Botao0 = new QPushButton(centralwidget);
        Botao0->setObjectName(QString::fromUtf8("Botao0"));
        sizePolicy.setHeightForWidth(Botao0->sizePolicy().hasHeightForWidth());
        Botao0->setSizePolicy(sizePolicy);
        Botao0->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #C0C0C0;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Botao0, 4, 1, 1, 1);

        TrocarSinal = new QPushButton(centralwidget);
        TrocarSinal->setObjectName(QString::fromUtf8("TrocarSinal"));
        sizePolicy.setHeightForWidth(TrocarSinal->sizePolicy().hasHeightForWidth());
        TrocarSinal->setSizePolicy(sizePolicy);
        TrocarSinal->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #FF5500;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(TrocarSinal, 4, 2, 1, 1);

        Subtracao = new QPushButton(centralwidget);
        Subtracao->setObjectName(QString::fromUtf8("Subtracao"));
        sizePolicy.setHeightForWidth(Subtracao->sizePolicy().hasHeightForWidth());
        Subtracao->setSizePolicy(sizePolicy);
        Subtracao->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #FFBC00;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Subtracao, 4, 3, 1, 1);

        Igual = new QPushButton(centralwidget);
        Igual->setObjectName(QString::fromUtf8("Igual"));
        sizePolicy.setHeightForWidth(Igual->sizePolicy().hasHeightForWidth());
        Igual->setSizePolicy(sizePolicy);
        Igual->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	background-color: #FFBC00;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"	background-color: #A9A9A9;\n"
"	border:  1px solid gray;\n"
"	padding: 5px;\n"
"}"));

        gridLayout->addWidget(Igual, 4, 4, 1, 1);

        Display = new QLineEdit(centralwidget);
        Display->setObjectName(QString::fromUtf8("Display"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(Display->sizePolicy().hasHeightForWidth());
        Display->setSizePolicy(sizePolicy1);
        QFont font;
        font.setFamily(QString::fromUtf8("Yrsa"));
        font.setPointSize(24);
        font.setBold(true);
        font.setItalic(true);
        font.setWeight(75);
        Display->setFont(font);
        Display->setStyleSheet(QString::fromUtf8("QLineEdit{\n"
"	background-color: gray;\n"
"	border:  1px solid gray;\n"
"	color: #ffffff\n"
"}"));
        Display->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(Display, 0, 0, 1, 5);

        Calculadora->setCentralWidget(centralwidget);
        menubar = new QMenuBar(Calculadora);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 512, 22));
        Calculadora->setMenuBar(menubar);
        statusbar = new QStatusBar(Calculadora);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        Calculadora->setStatusBar(statusbar);

        retranslateUi(Calculadora);

        QMetaObject::connectSlotsByName(Calculadora);
    } // setupUi

    void retranslateUi(QMainWindow *Calculadora)
    {
        Calculadora->setWindowTitle(QCoreApplication::translate("Calculadora", "Calculadora", nullptr));
        MemoriaSbt->setText(QCoreApplication::translate("Calculadora", "M-", nullptr));
        Adicao->setText(QCoreApplication::translate("Calculadora", "+", nullptr));
        Botao5->setText(QCoreApplication::translate("Calculadora", "5", nullptr));
        Botao3->setText(QCoreApplication::translate("Calculadora", "3", nullptr));
        Divisao->setText(QCoreApplication::translate("Calculadora", "/", nullptr));
        Botao9->setText(QCoreApplication::translate("Calculadora", "9", nullptr));
        Botao7->setText(QCoreApplication::translate("Calculadora", "7", nullptr));
        Botao8->setText(QCoreApplication::translate("Calculadora", "8", nullptr));
        Botao6->setText(QCoreApplication::translate("Calculadora", "6", nullptr));
        Botao1->setText(QCoreApplication::translate("Calculadora", "1", nullptr));
        MemoriaAdc->setText(QCoreApplication::translate("Calculadora", "M+", nullptr));
        Multiplicacao->setText(QCoreApplication::translate("Calculadora", "*", nullptr));
        Botao2->setText(QCoreApplication::translate("Calculadora", "2", nullptr));
        Memoria->setText(QCoreApplication::translate("Calculadora", "M", nullptr));
        Botao4->setText(QCoreApplication::translate("Calculadora", "4", nullptr));
        Limpar->setText(QCoreApplication::translate("Calculadora", "AC", nullptr));
        Botao0->setText(QCoreApplication::translate("Calculadora", "0", nullptr));
        TrocarSinal->setText(QCoreApplication::translate("Calculadora", "+/-", nullptr));
        Subtracao->setText(QCoreApplication::translate("Calculadora", "-", nullptr));
        Igual->setText(QCoreApplication::translate("Calculadora", "=", nullptr));
        Display->setText(QCoreApplication::translate("Calculadora", "0.0", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Calculadora: public Ui_Calculadora {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CALCULADORA_H
