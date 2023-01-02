import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Anasayfa import *
from backend import *
from PyQt5.QtCore import Qt
import openpyxl


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.comboBox.addItem("Star")
        self.ui.comboBox.addItem("Director")
        self.ui.comboBox.addItem("Rating")
        self.ui.comboBox.addItem("Genre")
        self.ui.comboBox.addItem("Metascore")
        self.ui.comboBox.addItem("Watchtime")
        self.ui.comboBox.addItem("All Data")
         
        self.ui.pushButton.clicked.connect(self.show_results)
        
        
    def show_results(self):
        selectedData = self.ui.comboBox.currentText()
        if selectedData == "Star" : 
             self.ui.tableWidget.clear()
             row=0
             for mov in range(0,249):
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(movie_DF["Name of movie"][mov])))
                self.ui.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(movie_DF["Star"][mov])))
                row=row+1
        elif selectedData == "Director":
              self.ui.tableWidget.clear()
              row=0
              for mov in range(0,249):
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(movie_DF["Name of movie"][mov])))
                self.ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(movie_DF["Director"][mov])))
                row=row+1
        elif selectedData == "Rating"  : 
             self.ui.tableWidget.clear()
             row=0
             for mov in range(0,249):
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(movie_DF["Name of movie"][mov])))
                self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(movie_DF["Movie Rating"][mov])))
                row=row+1
        elif selectedData == "Genre" : 
              self.ui.tableWidget.clear()
              row=0
              for mov in range(0,249):
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(movie_DF["Name of movie"][mov])))
                self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(movie_DF["Genre"][mov])))
                row=row+1
        elif selectedData == "Metascore" : 
             self.ui.tableWidget.clear()
             row=0
             for mov in range(0,249):
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(movie_DF["Name of movie"][mov])))
                self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(movie_DF["Metascore"][mov])))
                row=row+1
        elif selectedData == "Watchtime" : 
             self.ui.tableWidget.clear()
             row=0
             for mov in range(0,249):
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(movie_DF["Name of movie"][mov])))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(movie_DF["Watchtime"][mov])))
                row=row+1
        elif selectedData == "All Data" : 
            self.ui.tableWidget.clear()
            row=0
            for mov in range(0,249):
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(movie_DF["Name of movie"][mov])))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(movie_DF["Watchtime"][mov])))
                self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(movie_DF["Movie Rating"][mov])))
                self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(movie_DF["Metascore"][mov])))
                self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(movie_DF["Genre"][mov])))
                self.ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(movie_DF["Director"][mov])))
                self.ui.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(movie_DF["Star"][mov])))
                row=row+1
           

        


Uygulama=QApplication(sys.argv)
'''penAna=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()
sys.exit(Uygulama.exec_())'''

pencere=main()
pencere.show()
Uygulama.exec()


