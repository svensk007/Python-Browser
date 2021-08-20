import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

print("ERR LOG:")

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__()
		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl('http://google.com'))
		self.setCentralWidget(self.browser)
		self.showMaximized()

# NAVBAR
navbar = QToolBar()
self.addToolBar(navbar)

back_btn = QAction('Back',self)
back_btn.triggered.connect(self.browser.back)

app = QApplication(sys.argv)
QApplication.setApplicationName('Browser')
window = MainWindow()
app.exec_()
