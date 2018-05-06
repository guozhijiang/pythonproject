#-*- coding:utf-8 -*-
__author__ = 'GuoZhiqiang'
import json
import sys
from PyQt5.QtGui import  QPixmap
from PyQt5.QtGui import  QIntValidator
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QHBoxLayout,  QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.index=0
        self.configDict=self.loadConfig()
        self.initUi()
        self.btn_next.clicked.connect(self.switchImage)
        self.btn_sub.clicked.connect(self.subPriceInfo)

    def closeEvent(self, QCloseEvent):
        self.export()

    def export(self):
        with open('./record.json','w') as record_file:
            record_file.write(json.dumps(self.configDict))

    def loadConfig(self):
        with open("./config.json",'r') as load_f:
            load_dict = json.load(load_f)
            return load_dict

    def switchImage(self):
        if self.guess_info.text!='':
            self.guess_info.clear()
        if self.produce_price!='':
            self.produce_price.clear()
        self.index=(self.index+1)%len(self.configDict)
        self.imgeLabel.setPixmap(QPixmap(self.configDict[str(self.index)]['imagepath']))
        self.price_info.setText(str(self.configDict[str(self.index)]['priceRange'][0]))
        self.price_info2.setText(str(self.configDict[str(self.index)]['priceRange'][1]))

    def subPriceInfo(self):
        if self.produce_price.text()=='':
            return
        try:
            price=self.produce_price.text()
            self.configDict[str(self.index)]['record'].append(int(price))
            if int(price)==self.configDict[str(self.index)]['price']:
                self.guess_info.setText('恭喜您猜对了！')
                print(self.index)
                print(self.configDict[str(self.index)]['record'])
            elif int(price)>self.configDict[str(self.index)]['price']:
                self.guess_info.setText('您猜的价格太高了！')
                if int(price)<int(self.price_info2.text()):
                    self.price_info2.setText(price)
            else:
                self.guess_info.setText('您猜的价格太低了！')
                if int(price)>int(self.price_info.text()):
                    self.price_info.setText(price)
        except Exception as e:
            print('erro happen')

    def initUi(self):
        self.createGridGroupBox()
        self.creatFormGroupBox()
        self.creatFormGroupBox2()
        mainLayout = QVBoxLayout()
        hboxLayout = QHBoxLayout()
        hboxLayout2 = QHBoxLayout()
        hboxLayout.addStretch()
        hboxLayout.addWidget(self.gridGroupBox)
        mainLayout.addLayout(hboxLayout)
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addLayout(hboxLayout2)
        mainLayout.addWidget(self.formGroupBox2)
        self.setLayout(mainLayout)

    def createGridGroupBox(self):
        self.gridGroupBox = QGroupBox("物品：")
        layout = QGridLayout()
        self.imgeLabel = QLabel()
        self.pixMap = QPixmap(QPixmap(self.configDict[str(self.index)]['imagepath']))
        self.imgeLabel.setPixmap(self.pixMap)
        self.btn_next=QPushButton('下一个')
        layout.setSpacing(10)
        layout.addWidget(self.imgeLabel,0,0,0,1)
        layout.addWidget(self.btn_next,0,1,0,10)
        layout.setColumnStretch(1, 10)
        self.gridGroupBox.setLayout(layout)
        self.setWindowTitle('猜猜物品的价格')

    def creatFormGroupBox(self):
        self.formGroupBox = QGroupBox("价格信息：")
        layout = QGridLayout()
        price_range_label = QLabel("价格区间（元）：")
        self.label1 = QLabel('[')
        self.price_info = QLabel()
        self.label2 = QLabel('-')
        self.price_info2 = QLabel()
        self.label3 = QLabel(']')
        self.price_info.setText(str(self.configDict[str(self.index)]['priceRange'][0]))
        self.price_info2.setText(str(self.configDict[str(self.index)]['priceRange'][1]))
        self.guess_info = QLabel()
        self.input_price = QLineEdit("")
        layout.setSpacing(10)
        layout.addWidget(price_range_label,0,0,0,1)
        layout.addWidget(self.label1,0,1,0,1)
        layout.addWidget(self.price_info,0,2,0,1)
        layout.addWidget(self.label2,0,3,0,1)
        layout.addWidget(self.price_info2,0,4,0,1)
        layout.addWidget(self.label3,0,5,0,1)
        layout.addWidget(self.guess_info,0,20,0,10)
        self.formGroupBox.setLayout(layout)

    def creatFormGroupBox2(self):
        self.formGroupBox2 = QGroupBox("输入价格(请输入整数)：")
        layout = QGridLayout()
        self.produce_price = QLineEdit("")
        pIntValidator=QIntValidator(self)
        self.produce_price.setValidator(pIntValidator)
        self.btn_sub=QPushButton('提交价格')
        layout.addWidget(self.produce_price, 0, 0, 0, 1)
        layout.addWidget(self.btn_sub,0,1,0,1)
        self.formGroupBox2.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())