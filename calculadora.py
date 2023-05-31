import sys
from PyQt5 import QtWidgets as Qtw

class App(Qtw.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        #window configuration
        self.setWindowTitle("Calculadora :D")
        self.setFixedSize(400, 400)
        
        self.cw = Qtw.QWidget()
        self.grid = Qtw.QGridLayout(self.cw)
        self.setCentralWidget(self.cw)
        
        # display configuration
        self.display = Qtw.QLineEdit()
        self.display.setSizePolicy(Qtw.QSizePolicy.Preferred, Qtw.QSizePolicy.Expanding)
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.setStyleSheet('* {background: #2B1A17; color: white; font-size: 30px; font-weight: sans;}')
        
        #btn configurations
        self.add_btn(Qtw.QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(Qtw.QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(Qtw.QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(Qtw.QPushButton('<-'), 1, 3, 1, 1, lambda: self.display.setText(self.display.text()[:-1]))
        self.add_btn(Qtw.QPushButton('C'), 1, 4, 1, 1, lambda: self.display.setText(''))
        
        self.add_btn(Qtw.QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(Qtw.QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(Qtw.QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(Qtw.QPushButton('**'), 2, 3, 1, 1)
        self.add_btn(Qtw.QPushButton('/'), 2, 4, 1, 1)
        
        self.add_btn(Qtw.QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(Qtw.QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(Qtw.QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(Qtw.QPushButton('-'), 3, 3, 1, 1)
        self.add_btn(Qtw.QPushButton('*'), 3, 4, 1, 1)
        
        self.add_btn(Qtw.QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(Qtw.QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(Qtw.QPushButton(','), 4, 2, 1, 1)
        self.add_btn(Qtw.QPushButton('+'), 4, 3, 1, 1)
        self.add_btn(Qtw.QPushButton('='), 4, 4, 1, 1, self.eval_igual)
        
    def add_btn(self, btn, rol, col, rowspan, cowspan, funcao=None):
        self.grid.addWidget(btn, rol, col, rowspan, cowspan)
        
        if not funcao:
            btn.clicked.connect(lambda: self.display.setText(self.display.text() + btn.text()))
        else:
            btn.clicked.connect(funcao)
            
    def eval_igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as error:
            self.display.setText("Conta inválida.")
    
    

if __name__=="__main__":
    qt = Qtw.QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec()