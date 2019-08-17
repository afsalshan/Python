from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
# class MyWindow(MainWindow):
    # def __init(self):
    #     super(MyWindow,self).__init()
print("hai")
def clicked():
    print('clicked')
def window():

    app = QApplication(sys.argv)
    print(type(app))
    win = QMainWindow()
    win.setGeometry(0, 0, 300, 300)
    win.setWindowTitle("hello ")
    label = QtWidgets.QLabel(win)
    b1 = QtWidgets.QPushButton(win)
    b1.setText("click")
    b1.clicked.connect(clicked)
    
    # QtWidgets.QMessageBox()
    label.setText("my first label")
    label.move(0, 150)
    win.show()
    sys.exit(app.exec_())


window()
