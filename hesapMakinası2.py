from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

uyg=QApplication([])

class hesapMakinasi2(QWidget):
    def __init__(self,ebeveyn=None):
        super(hesapMakinasi2,self).__init__(ebeveyn)

        self.setWindowTitle("Hesap Makinası 2")
        self.resize(100,300)

        baslik=QLabel("<center><font color='blue' size='20'>HESAP MAKİNASI</center></font>")
        birinciDegerLabel=QLabel("Birinci Değer: ")
        self.birinciDeger=QLineEdit()
        ikinciDegerLabel=QLabel("İkinci Değer: ")
        self.ikinciDeger=QLineEdit()
        sonucLabel=QLabel("Sonuç: ")
        self.sonucLabel2=QLabel("")
        self.toplaButton=QPushButton("TOPLA")
        self.cikarButton=QPushButton("ÇIKAR")
        self.carpButton=QPushButton("ÇARP")
        self.bolButton=QPushButton("BÖL")
        self.temizleButton=QPushButton("Temizle")

        grid=QGridLayout()
        self.setLayout(grid)
        grid.addWidget(baslik,0,0,1,3)
        grid.addWidget(birinciDegerLabel,1,0)
        grid.addWidget(self.birinciDeger,1,1)
        grid.addWidget(ikinciDegerLabel,2,0)
        grid.addWidget(self.ikinciDeger,2,1)
        grid.addWidget(sonucLabel,3,0)
        grid.addWidget(self.sonucLabel2,3,1)
        grid.addWidget(self.temizleButton,4,0)
        grid.addWidget(self.toplaButton,5,0)
        grid.addWidget(self.cikarButton,5,1)
        grid.addWidget(self.carpButton,6,0)
        grid.addWidget(self.bolButton,6,1)

        self.temizleButton.clicked.connect(self.temizle)
        self.toplaButton.clicked.connect(self.topla)
        self.cikarButton.clicked.connect(self.cikar)
        self.carpButton.clicked.connect(self.carp)
        self.bolButton.clicked.connect(self.bol)
        
    def temizle(self):
        self.birinciDeger.setText("")
        self.ikinciDeger.setText("")
        self.sonucLabel2.setText("")

    def topla(self):
        result1=int(self.birinciDeger.text())+int(self.ikinciDeger.text())
        self.sonucLabel2.setText(str(result1))
        
    def cikar(self):
        result2=int(self.birinciDeger.text())-int(self.ikinciDeger.text())
        self.sonucLabel2.setText(str(result2))

    def carp(self):
        result3=int(self.birinciDeger.text())*int(self.ikinciDeger.text())
        self.sonucLabel2.setText(str(result3))

    def bol(self):
        gecici=int(self.birinciDeger.text())/int(self.ikinciDeger.text())
        result4=float(gecici)
        self.sonucLabel2.setText(str(result4))

pencere=hesapMakinasi2()
pencere.show()
uyg.exec_()