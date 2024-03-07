from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout,
                             QLabel, QTextEdit, QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView,
                             QGroupBox, QRadioButton, QButtonGroup)
import sys
import re
from composition_analysis import *



# Создаём виджет Qt — окно.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cats Food")

        self.brendNameLbl = QLabel("Введите название бренда:")
        self.brendNameLbl.setStyleSheet("QLabel" 
                              "{"
                                "font : 20px Arial;"
                                "background-color : lightgreen;"
                                "}"
                              )
        self.brendNameLine = QLineEdit()
        self.brendNameLine.setStyleSheet("QLineEdit" 
                              "{"
                                "font : 20px Arial;"
                                "}"
                              )
        self.lineNameLbl = QLabel("Название линейки")
        self.lineNameLbl.setStyleSheet("QLabel" 
                              "{"
                                "font : 20px Arial;"
                                "background-color : lightgreen;"
                                "}"
                              )
        self.linevkusLbl = QLabel("Название вкуса:")
        self.linevkusLbl.setStyleSheet("QLabel" 
                              "{"
                                "font : 20px Arial;"
                                "background-color : lightgreen;"
                                "}"
                              )

        self.lineNameLine = QLineEdit()
        self.lineNameLine.setStyleSheet("QLineEdit" 
                              "{"
                                "font : 20px Arial;"
                                "}"
                              )
        self.linevkus = QLineEdit()
        self.linevkus.setStyleSheet("QLineEdit" 
                              "{"
                                "font : 20px Arial;"
                                "}"
                              )
        self.Vline1 = QVBoxLayout()
        self.Vline1.addWidget(self.lineNameLbl)
        self.Vline1.addWidget(self.lineNameLine)

        self.Vline2 = QVBoxLayout()
        self.Vline2.addWidget(self.linevkusLbl)
        self.Vline2.addWidget(self.linevkus)
        self.layout3 = QHBoxLayout()
        self.layout3.addLayout(self.Vline1)
        self.layout3.addLayout(self.Vline2)

        self.ClassRadioGroupBox = QGroupBox("Вид животного:") # группа на экране для переключателей с ответами
        self.ClassRadioGroupBox.setStyleSheet("QGroupBox" 
                              "{"
                                "font : 25px Arial;"
                                "background-color : lightyellow"
                                "}"
                              )
        
        self.ClassRadioGroup = QButtonGroup() # это для группировки переключателей, чтобы управлять их поведением
        self.cat_rbtn = QRadioButton('кошки')
        self.cat_rbtn.setChecked(True)
        self.cat_rbtn.setStyleSheet("QRadioButton" 
                              "{"
                                "font : 20px Arial;"
                                "}"
                              )
        self.dog_rbtn = QRadioButton('собаки')
        self.dog_rbtn.setStyleSheet("QRadioButton" 
                              "{"
                                "font : 20px Arial;"
                                "}"
                              )
        self.ClassRadioGroup.addButton(self.cat_rbtn)
        self.ClassRadioGroup.addButton(self.dog_rbtn)
        self.Cl_layout_group = QHBoxLayout()
        self.Cl_layout_group.addWidget(self.cat_rbtn) 
        self.Cl_layout_group.addWidget(self.dog_rbtn)
        self.ClassRadioGroupBox.setLayout(self.Cl_layout_group)

        self.Vline0 = QVBoxLayout()
        self.Vline0.addWidget(self.brendNameLbl)
        self.Vline0.addWidget(self.brendNameLine)
        self.layout0 = QHBoxLayout()
        self.layout0.addLayout(self.Vline0)
        self.layout0.addWidget(self.ClassRadioGroupBox)



        self.ingrediensLbl = QLabel("Введите ингредиенты корма:")
        self.ingrediensLbl.setStyleSheet("QLabel" 
                              "{"
                                "font : 20px Arial;"
                                "background-color : lightgreen;"
                                "}"
                              )
        self.analisLbl = QLabel("Введите гарантированные показатели корма:")
        self.analisLbl.setStyleSheet("QLabel" 
                              "{"
                                "font : 20px Arial;"
                                "background-color : lightgreen;"
                                "}"
                              )
        self.reportLbl = QLabel("Отчет:")

        self.sizeLbl = QLabel("Введите витаминную добавку:")
        self.sizeLbl.setStyleSheet("QLabel" 
                              "{"
                                "font : 20px Arial;"
                                "background-color : lightgreen;"
                                "}"
                              )
        self.noteLbl = QLabel("Введите примечание:")
        self.noteLbl.setStyleSheet("QLabel" 
                              "{"
                                "font : 20px Arial;"
                                "background-color : lightgreen;"
                                "}"
                              )
        self.kalorLbl = QLabel("Введите калорийность:")
        self.kalorLbl.setStyleSheet("QLabel" 
                              "{"
                                "font : 20px Arial;"
                                "background-color : lightgreen;"
                                "}"
                              )
        
        self.granulLbl = QLabel("Введите размер гранул:")
        self.granulLbl.setStyleSheet("QLabel" 
                              "{"
                                "font : 20px Arial;"
                                "background-color : lightgreen;"
                                "}"
                              )

        
     
        self.sizeLine = QTextEdit()
        self.noteLine = QLineEdit()
        self.noteLine.setStyleSheet("QLineEdit" 
                              "{"
                                "font : 20px Arial;"
                                "}"
                              )
        self.kalorLine = QLineEdit()
        self.kalorLine.setStyleSheet("QLineEdit" 
                              "{"
                                "font : 20px Arial;"
                                "}"
                              )
        
        self.granulLine = QLineEdit()
        self.granulLine.setStyleSheet("QLineEdit" 
                              "{"
                                "font : 20px Arial;"
                                "}"
                              )
        self.ingredText = QTextEdit()
        self.analisText = QTextEdit()
        self.reportText = QTextEdit()
        self.TypeRadioGroupBox = QGroupBox("Возрастная группа:") # группа на экране для переключателей с ответами
        self.TypeRadioGroupBox.setStyleSheet("QGroupBox" 
                              "{"
                                "font : 25px Arial;"
                                "background-color : lightyellow"
                                "}"
                              )
        self.TypeRadioGroup = QButtonGroup() # это для группировки переключателей, чтобы управлять их поведением
        
        self.adult_rbtn = QRadioButton('Для взрослых')
        self.adult_rbtn.setChecked(True)
        self.adult_rbtn.setStyleSheet("QRadioButton" 
                              "{"
                                "font : 20px Arial;"
                                "}"
                              )
        self.little_rbtn = QRadioButton('Для маленьких')
        self.little_rbtn.setStyleSheet("QRadioButton" 
                              "{"
                                "font : 20px Arial;"
                                "}"
                              )
        self.old_rbtn = QRadioButton('Для пожилых')
        self.old_rbtn.setStyleSheet("QRadioButton" 
                              "{"
                                "font : 20px Arial;"
                                "}"
                              )

        self.TypeRadioGroup.addButton(self.adult_rbtn)
        self.TypeRadioGroup.addButton(self.little_rbtn)
        self.TypeRadioGroup.addButton(self.old_rbtn)
        
        self.layout_group = QHBoxLayout()
        self.layout_group.addWidget(self.adult_rbtn) 
        self.layout_group.addWidget(self.little_rbtn)
        self.layout_group.addWidget(self.old_rbtn) 
        
        self.TypeRadioGroupBox.setLayout(self.layout_group)


        self.layout1 = QHBoxLayout()
        self.SpesialLine = QLineEdit()
        self.SpesialLine.setStyleSheet("QLineEdit" 
                              "{"
                                "font : 20px Arial;"
                                "}"
                              )
        self.SpesialLineName = QLabel("Введите направление:")
        self.SpesialLineName.setStyleSheet("QLabel" 
                              "{"
                                "font : 20px Arial;"
                                "background-color : lightgreen;"
                                "}"
                              )
        self.layout1.addWidget(self.TypeRadioGroupBox)
        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.SpesialLineName)
        self.layout2.addWidget(self.SpesialLine)

        self.layout1.addLayout (self.layout2)

    



        self.v1Line = QVBoxLayout() # левая вертикальная
        self.v2Line = QVBoxLayout() #правая вертикальная
        self.h1Line = QHBoxLayout() # выравнивает две предыдущие
        self.mainLine = QVBoxLayout()# главная 
        self.btnLoadTable = QPushButton("Внести в таблицу")
        self.btnLoadTable.setMinimumHeight(70)
        self.btnLoadTable.setStyleSheet("QPushButton" 
                              "{"
                                "font : 20px Arial;"
                                "background-color : lightblue;"
                                "}"
                              )
      
        self.table = QTableWidget(self)  # Create a table
        self.table.setMaximumHeight(250)
        ColumNum = 35
        self.table.setColumnCount(ColumNum)     #Set three columns
        self.table.setRowCount(2) 
        
        self.table.setRowHeight(0,130)
        for i in range(ColumNum):
            self.table.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeMode.ResizeToContents)
     
        
        self.table.setHorizontalHeaderLabels(["id", "животное", "возраст", "Бренд", "направление", #0 1 2 3 4 
                                           "Линейка", "вкус", "Источник белка", "Источник жиров",  # 5 6 7 8 
                                           "Источник углеводов", "источники клетчатки", "пребиотики", # 9 10 11 
                                            "спец.добавки", "консер-т/антиокс-д",  "маркетинг", # 12 13 14
                                           "белки %", "жиры %", # 15 16
                                         "клетчатка %", "зола %", "Ca %", "P %", # 17 18 19 20
                                         "Ca/P", "Mg %", "Na %", "калий %", # 21 22 23 24
                                          "Омега-3%", "Омега-6%", "Ом6/Ом3" , "влажность %", #  25 26 27 28
                                         "углеводы %", "калорийность упак", "калорийность ГОСТ", # 29 30 31 
                                          "витаминная добавка", "примечания"])# 32 33
                                      

        self.btnLoadInFile = QPushButton("Загрузить в файл")
        self.btnLoadInFile.setMinimumHeight(70)
        self.btnLoadInFile.setStyleSheet("QPushButton" 
                              "{"
                                "font : 20px Arial;"
                                "background-color : lightblue;"
                                "}"
                              )


        self.v1Line.addLayout(self.layout0)
        self.v1Line.addLayout(self.layout3)

        self.v1Line.addLayout(self.layout1)
        #self.v1Line.addWidget(self.ClassRadioGroupBox)
        #self.v1Line.addWidget(self.classLbl)  
       
        self.v1Line.addWidget(self.analisLbl)  
        self.v1Line.addWidget(self.analisText)


        self.subv1 = QVBoxLayout()
        self.subv2 = QVBoxLayout()
        self.h2Line = QHBoxLayout()


        self.subv1.addWidget(self.kalorLbl)  
        self.subv1.addWidget(self.kalorLine)

        self.subv2.addWidget(self.granulLbl)  
        self.subv2.addWidget(self.granulLine)
        self.h2Line.addLayout(self.subv1)
        self.h2Line.addLayout(self.subv2)

        self.v1Line.addLayout(self.h2Line)

       # self.v1Line.setSpacing(0)
        self.v1Line.addStretch()
        self.v2Line.addWidget(self.ingrediensLbl)
        self.v2Line.addWidget(self.ingredText)
        self.v2Line.addWidget(self.sizeLbl)
        self.v2Line.addWidget(self.sizeLine)
        self.v2Line.addWidget(self.noteLbl)
        self.v2Line.addWidget(self.noteLine)


        self.h1Line.addLayout(self.v1Line)
        self.h1Line.addLayout(self.v2Line)
        self.mainLine.addLayout(self.h1Line)
        self.mainLine.addWidget(self.btnLoadTable)
        self.mainLine.addWidget(self.table)
        self.mainLine.addWidget(self.btnLoadInFile)
        

        self.mainwidget = QWidget()
        self.mainwidget.setLayout(self.mainLine)
        #self.setFixedSize(QSize(400, 300))

        # Set the central widget of the Window.
        self.setCentralWidget(self.mainwidget)
        self.setMinimumSize(1920,700)

        self.btnLoadTable.clicked.connect(self.btnClick)

        self.btnLoadInFile.setEnabled(False)
        self.btnLoadInFile.clicked.connect(self.LoadClick)

    def btnClick(self):

        brandName = self.brendNameLine.text()    
        if brandName:
            self.table.setItem(0, 3, QTableWidgetItem(brandName))
        else:
            print('Вы не ввели название бренда')

        lineName = self.lineNameLine.text()
        if lineName:
            self.table.setItem(0, 5, QTableWidgetItem(lineName))
        else:
            print('Вы не ввели название линейки')

        spesialName = self.SpesialLine.text()
        if spesialName:
            self.table.setItem(0, 4, QTableWidgetItem(spesialName))
        else:
            print('Вы не ввели название направления')

        favorName = self.linevkus.text()
        if favorName:
            self.table.setItem(0, 6, QTableWidgetItem(favorName))
        else:
            print('Вы не ввели название вкуса')


        kkal = self.kalorLine.text()
        if kkal:
            self.table.setItem(0, 30, QTableWidgetItem(kkal))
        else:
            self.table.setItem(0, 30, QTableWidgetItem(str(0)))
            kkal = 0
            print('Вы не ввели калорийность')

        line = self.noteLine.text()
        if line:
            self.table.setItem(0, 33, QTableWidgetItem(line))
        else:
            print('Вы не ввели примечание')


        granul = self.granulLine.text()
        if line:
            granul = '0'
        else:
            print('Вы не ввели размер гранул')
                    
        
        age = ""
        if self.adult_rbtn.isChecked():
            age = "взрослые"
        elif self.little_rbtn.isChecked():
            age = "малыши"
        elif self.old_rbtn.isChecked():
            age = "пожилые"

        self.table.setItem(0, 2, QTableWidgetItem(age))

        anymalType = ""
        if self.cat_rbtn.isChecked():
            anymalType = "кошки"
        else:
            anymalType = "собаки"
            
        self.table.setItem(0, 1, QTableWidgetItem(anymalType))


        ingredients = self.ingredText.toPlainText()
        if not ingredients:
            print('Вы не ввели список ингредиентов')
            ingredients = "Ингридиентов нет"
       

        GA = self.analisText.toPlainText()
        if not GA:
            GA = "нет ГА"
            print('Вы не ввели гарантированный анализ')
       
            

        Vitamine = self.sizeLine.toPlainText()

          
        if not Vitamine:
            print('Вы не ввели добавку')

            self.addStringToTable(Vitamine, 32)
        else:
            print('Вы не ввели добавку')
        

        df = pd.read_csv('all_food_data.csv')
        print(df)
        id = df['ID'].max()+1
        #id = 1



        self.composition = ParsingComposition(ingredients, GA, Vitamine, id, brandName, lineName, spesialName, favorName, age, anymalType, kkal, line, granul )
        self.addDataToTable()
        self.btnLoadInFile.setEnabled(True)
        self.composition.ListsToString()
        self.composition.createAllDataDict(id, brandName, lineName, spesialName, favorName, age, anymalType, kkal, line)
        

    def LoadClick(self):
      df_gaData = pd.DataFrame.from_dict([self.composition.ga_dict])
      df_gaData.to_csv('ga_data.csv', mode='a', index= False , header= False )

      df_vitData = pd.DataFrame.from_dict([self.composition.vit_dict])
      df_vitData.to_csv('vitamin_data.csv', mode='a', index= False , header= False )

      df_foodData = pd.DataFrame.from_dict([self.composition.foodAbout])
      df_foodData.to_csv('food_about_data.csv', mode='a', index= False , header= False )


      df_allData = pd.DataFrame.from_dict([self.composition.allData_dict])
      df_allData.to_csv('all_food_data.csv', mode='a', index= False , header= False )

      df_composData = pd.DataFrame.from_dict([self.composition.compos_dict])
      df_composData.to_csv('composition_data.csv', mode='a', index= False , header= False )

      print("Данные загружены в файлы")

      



        
        
    def addStringToTable(self, content, rowNum):
        helpSt = ""
        n = 0
        for i in content:
            if n%2 == 0:
                helpSt += '\n'
            helpSt = helpSt + i + ', '
            n+=1
            
        helpSt=helpSt[:-2]
        self.table.setItem(0, rowNum, QTableWidgetItem(helpSt))
        

        #----------------------------------------------------------------------------------------------
        #добавление в таблицу
    
    def addDataToTable (self):

        self.addStringToTable(self.composition.compos_dict['белки'], 7)
        self.addStringToTable(self.composition.compos_dict['жиры'], 8)
        self.addStringToTable(self.composition.compos_dict['углеводы'], 9)
        self.addStringToTable(self.composition.compos_dict['клетчатка'], 10)
        self.addStringToTable(self.composition.compos_dict['пребиотики'], 11)
        self.addStringToTable(self.composition.compos_dict['специальное'], 12)
        self.addStringToTable(self.composition.Vitamins, 32)
        self.addStringToTable(self.composition.compos_dict['маркетинг'], 14)
        self.addStringToTable(self.composition.compos_dict['антиоксиданты'], 13)

        self.table.setItem(0, 15, QTableWidgetItem(str(self.composition.ga_dict['белок'])))
        self.table.setItem(0, 16, QTableWidgetItem(str(self.composition.ga_dict['жиры'])))
        self.table.setItem(0, 17, QTableWidgetItem(str(self.composition.ga_dict['клетчатка'])))
        self.table.setItem(0, 18, QTableWidgetItem(str(self.composition.ga_dict['зола'])))
        self.table.setItem(0, 19, QTableWidgetItem(str(self.composition.ga_dict['кальций'])))
        self.table.setItem(0, 20, QTableWidgetItem(str(self.composition.ga_dict['фосфор'])))
        self.table.setItem(0, 21, QTableWidgetItem(str(self.composition.ga_dict['коэфминерал'])))
        self.table.setItem(0, 22, QTableWidgetItem(str(self.composition.ga_dict['магний'])))
        self.table.setItem(0, 23, QTableWidgetItem(str(self.composition.ga_dict['натрий'])))
        self.table.setItem(0, 24, QTableWidgetItem(str(self.composition.ga_dict['калий'])))
        self.table.setItem(0, 25, QTableWidgetItem(str(self.composition.ga_dict['омега3'])))
        self.table.setItem(0, 26, QTableWidgetItem(str(self.composition.ga_dict['омега6'])))
        self.table.setItem(0, 27, QTableWidgetItem(str(self.composition.ga_dict['коэфомег'])))
        self.table.setItem(0, 28, QTableWidgetItem(str(self.composition.ga_dict['влажность'])))
        self.table.setItem(0, 29, QTableWidgetItem(str(self.composition.ga_dict['углеводы'])))
        self.table.setItem(0, 31, QTableWidgetItem(str(self.composition.ga_dict['энергия_гост'])))

        
        self.table.setItem(0, 0, QTableWidgetItem(str(self.composition.compos_dict['ID'])))



app = QApplication(sys.argv)
window = MainWindow()
window.show()  # Важно: окно по умолчанию скрыто.

app.exec()