from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout,
                             QLabel, QTextEdit, QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView,
                             QGroupBox, QRadioButton, QButtonGroup)
import sys
import re
import itertools 

carbohydrates = ["рис", "горох", "злаки", "пшеница", "кукуруза", "маис", "картофель", "овес", "ячмень", "сорго", "киноа", "спельта"]
antiacs = ["апельсин", "клюква", "розмарин", "брусника", "курку", "алоэ"]
meatList = ["сельд", "утка", "куриц", "говяд", "телят", "индей"]

# Создаём виджет Qt — окно.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cats Food")

        self.brendNameLbl = QLabel("Введите название бренда:")
        self.lineNameLbl = QLabel("Название линейки и вкуса:")
        self.classLbl = QLabel("Класс корма:")
        self.ingrediensLbl = QLabel("Введите ингредиенты корма:")
        self.analisLbl = QLabel("Введите гарантированные показатели корма:")
        self.reportLbl = QLabel("Отчет:")
        self.sizeLbl = QLabel("Введите размер гранул:")
        self.noteLbl = QLabel("Введите примечание:")
        self.brendNameLine = QLineEdit()
        self.lineNameLine = QLineEdit()
        self.classLine = QLineEdit()
        self.sizeLine = QLineEdit()
        self.noteLine = QLineEdit()
        self.ingredText = QTextEdit()
        self.analisText = QTextEdit()
        self.reportText = QTextEdit()
        self.TypeRadioGroupBox = QGroupBox("Вид корма:") # группа на экране для переключателей с ответами
        self.ClassRadioGroupBox = QGroupBox("Класс корма:") # группа на экране для переключателей с ответами

        self.TypeRadioGroup = QButtonGroup() # это для группировки переключателей, чтобы управлять их поведением
        self.ClassRadioGroup = QButtonGroup() # это для группировки переключателей, чтобы управлять их поведением

        self.rbtn_1 = QRadioButton('Для взрослых')
        self.rbtn_2 = QRadioButton('Для котят')
        self.rbtn_3 = QRadioButton('Стерилизованные,\nUrinary,\nLight')
        self.rbtn_4 = QRadioButton('Sansitive,\nHypoallergenic,\nSkin&Coat')
        self.TypeRadioGroup.addButton(self.rbtn_1)
        self.TypeRadioGroup.addButton(self.rbtn_2)
        self.TypeRadioGroup.addButton(self.rbtn_3)
        self.TypeRadioGroup.addButton(self.rbtn_4)
        self.layout_group = QHBoxLayout()
        self.layout_group.addWidget(self.rbtn_1) 
        self.layout_group.addWidget(self.rbtn_2)
        self.layout_group.addWidget(self.rbtn_3) 
        self.layout_group.addWidget(self.rbtn_4)
        self.TypeRadioGroupBox.setLayout(self.layout_group)


        self.rbtn_5 = QRadioButton('Эконом')
        self.rbtn_6 = QRadioButton('Премиум')
        self.rbtn_7 = QRadioButton('Супер\nпремиум')
        self.rbtn_8 = QRadioButton('Холистик')
        self.ClassRadioGroup.addButton(self.rbtn_5)
        self.ClassRadioGroup.addButton(self.rbtn_6)
        self.ClassRadioGroup.addButton(self.rbtn_7)
        self.ClassRadioGroup.addButton(self.rbtn_8)
        self.layout_group2 = QHBoxLayout()
        self.layout_group2.addWidget(self.rbtn_5) 
        self.layout_group2.addWidget(self.rbtn_6)
        self.layout_group2.addWidget(self.rbtn_7) 
        self.layout_group2.addWidget(self.rbtn_8)
        self.ClassRadioGroupBox.setLayout(self.layout_group2)




        self.v1Line = QVBoxLayout() # левая вертикальная
        self.v2Line = QVBoxLayout() #правая вертикальная
        self.h1Line = QHBoxLayout() # выравнивает две предыдущие
        self.mainLine = QVBoxLayout()# главная 
        self.btnLoad = QPushButton("Загрузить")
        self.btnLoad.setMinimumHeight(70)
        self.btnLoad.setStyleSheet("QPushButton" 
                              "{"
                                "font : 20px Arial;"
                                "background-color : lightblue;"
                                "}"
                              )
      
        self.table = QTableWidget(self)  # Create a table
        self.table.setMaximumHeight(250)
        ColumNum = 26
        self.table.setColumnCount(ColumNum)     #Set three columns
        self.table.setRowCount(2) 
        
        self.table.setRowHeight(0,130)
        for i in range(ColumNum):
            self.table.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeMode.ResizeToContents)
     
        
        self.table.setHorizontalHeaderLabels(["Бренд/направление", "Линейка/вкус", "класс", "Источник белка",
                                         "Источник жиров", "Источник углеводов", "доп.компоненты", "белки %", "жиры %",
                                         "клетчатка %", "зола %", "Ca %", "P %", "Ca/P", "Mg %", "Na %", 
                                         "калий %", "Омега-3", "Омега-6", "влажность %", "углеводы %", "калорийность", 
                                         "размер гранул", "витаминная добавка", "консер-т антиокс-д", "примечания"])

        self.v1Line.addWidget(self.brendNameLbl)  
        self.v1Line.addWidget(self.brendNameLine)
        self.v1Line.addWidget(self.lineNameLbl)  
        self.v1Line.addWidget(self.lineNameLine)
        self.v1Line.addWidget(self.TypeRadioGroupBox)
        self.v1Line.addWidget(self.ClassRadioGroupBox)
        #self.v1Line.addWidget(self.classLbl)  
        #self.v1Line.addWidget(self.classLine)
        self.v1Line.addWidget(self.analisLbl)  
        self.v1Line.addWidget(self.analisText)

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
        self.mainLine.addWidget(self.btnLoad)
        self.mainLine.addWidget(self.table)
        

        self.mainwidget = QWidget()
        self.mainwidget.setLayout(self.mainLine)
        #self.setFixedSize(QSize(400, 300))

        # Set the central widget of the Window.
        self.setCentralWidget(self.mainwidget)
        self.setMinimumSize(1200,700)

        self.btnLoad.clicked.connect(self.btnClick)

    def btnClick(self):



        name = self.brendNameLine.text()    
        if name:
            self.table.setItem(0, 0, QTableWidgetItem(name))
        line = self.lineNameLine.text()
        if line:
            self.table.setItem(0, 1, QTableWidgetItem(line))
                    

        ingredients = self.ingredText.toPlainText()
        if ingredients:
            self.parsingIngredients(ingredients)
        else:
            print('Вы не ввели список ингредиентов')
        
        GA = self.analisText.toPlainText()
        if GA:
            self.parsingGA(GA)
        else:
            print('Вы не ввели гарантированный анализ')


    def parsingIngredients(self, ingredients):
        ingredients = ingredients.lower()
  
        ingredients = re.split(r'[;,]', ingredients) # разделить ингредиенты в список, разделитель или , или ;
        #print ('список всех ингридиентов:', ingredients)
        carboList = []
        protinList = []
        fatList = []
        anotherList = []
        antiacsList = []
        newIngredients = []
        # приводим строки к приличному виду
        i = 0

        maxLen = len(ingredients)
        while i < maxLen:
            ingredients[i] = re.sub(r'^\s+', '', ingredients[i])
            #print(ingredients[i])
            
            if '(' in ingredients[i]:
                newIngrid = ''
                while not (')' in ingredients[i]):
                    newIngrid += ingredients[i] 
                  
                    i +=1
                    
                newIngrid += ingredients[i]
                newIngredients.append(newIngrid)  
            else:
                newIngredients.append(ingredients[i] )  
            i+=1
            maxLen = len(ingredients)
        print(newIngredients)   
         

        for ingredient in newIngredients:
            #ingredient = ingredient.lower()
            carboFlag = False
            antiacsFlag = False
            meatFlag = False
            for (i, j, k) in itertools.zip_longest(carbohydrates, antiacs, meatList):
                if i != None:
                    if i in ingredient:
                        if ingredient.find("волокн") == -1:
                            carboFlag = True
                        else:
                            anotherList.append(ingredient)
                if j != None:
                    if j in ingredient:
                        antiacsFlag = True
                if k != None:
                    if k in ingredient:
                        meatFlag = True
 
            if carboFlag:
                carboList.append(ingredient)
            elif antiacsFlag:
                antiacsList.append(ingredient)
            elif ingredient.find("жир") != -1 or ingredient.find("масл") != -1:
                fatList.append(ingredient)
            elif ( ingredient.find("мясо") != -1 or ingredient.find("дегидр") != -1  or ingredient.find("белк") != -1 or
                    ingredient.find("глютен") != -1 or ingredient.find("яйц") != -1 or 
                    ingredient.find("обезвож") != -1 or ingredient.find("белок") != -1 ):
                protinList.append(ingredient)
            elif meatFlag:
                protinList.append(ingredient)
            else:
                anotherList.append(ingredient)

        #----------------------------------------------------------------------------------------------
        #добавление в таблицу
        self.addToTable(protinList, 3)
        self.addToTable(fatList, 4)
        self.addToTable(carboList, 5)
        self.addToTable(anotherList, 6)
        self.addToTable(antiacsList, 24)


        
        
    def addToTable(self, content, rowNum):
        helpSt = ""
        n = 0
        for i in content:
            if n%2 == 0:
                helpSt += '\n'
            helpSt = helpSt + i + ', '
            n+=1
            
        helpSt=helpSt[:-2]
        self.table.setItem(0, rowNum, QTableWidgetItem(helpSt))
        

    def findNumber(self, GA, word):
        
        #pattern1 = r'\s{word}\w*[^A-Za-z]{,8}?\d+[,.]\d+'
        pattern1 = r'{}'.format(word)
        pattern1 += r'\w*[^A-Za-z]{,8}?\d+[,.]\d+'
        pattern2 = fr'{word}\w*[^A-Za-z]*?\d+'
        number = 0
        if GA.find(word) != -1: 
            if len(re.findall(pattern1, GA)) == 0: # искать подстроку бел... далее символы отличные от букв, не более 5, затем дробное число
                number = re.findall(pattern2, GA)[0]
                number = re.findall(r'\d+', number)[0]
                #print(number)
            else:
                number = re.findall(pattern1, GA)[0]
                number = re.findall(r'\d+[,.]\d+', number)[0]
                number = number.replace(',', '.')
                #print(number)
        else:
            print('Значение', word ,'не найдено в гарантированном анализе!')
        return number


   

    def parsingGA(self, GA):
        #GA = GA.replace(';',',')
        #print(GA)
        GA = GA.lower()
        protein, fat, fiber, ash= [], [], [], []
        calc, fosf, magn, natr, kal = 0, 0, 0, 0, 0
        koefMiner = 0
        water = 10

        GA = re.sub(r'\d,\d', r'\d.\d', GA)
        print(GA)
        print ('парс ГА')

        #----------белок----------
        GA = GA.lower()
        if GA.find('бел') != -1:
            protein = self.findNumber(GA, 'бел')
        elif GA.find('прот') != -1:
            protein = self.findNumber(GA, 'прот')
        else:
            print('Значение белка не найдено в гарантированном анализе!')
            protein = 0

   
        #----------жиры----------
        if GA.find('масл') != -1: 
            fat = self.findNumber(GA, 'масл')
        elif GA.find('жир') != -1: 
            fat = self.findNumber(GA, 'жир')
        else:
            print('Значение жирности не найдено в гарантированном анализе!')
            fat = 0

        #----------клетчатка----------
        fiber = self.findNumber(GA, 'клетчат')
        

        #----------влажность----------
        water = self.findNumber(GA, 'вла')


        #----------зольность----------
        ash = self.findNumber(GA, 'зол')
        
        #----------кальций----------
        calc = self.findNumber(GA, 'каль')
        
        #----------фосфор----------
        fosf = self.findNumber(GA, 'фосф')
        
        
        if fosf != 0 and calc != 0:
            koefMiner = round(float(calc)/float(fosf),2)

        #----------магний----------
        magn = self.findNumber(GA, 'магн')
        
        #----------натрий----------
        natr = self.findNumber(GA, 'натр')
                
        #----------калий----------
        kal = self.findNumber(GA, 'кали')
                

        #----------------------------------------------------------------------------------------------
        #добавление в таблицу
        ugl = 100 - float(protein) - float(fat) - float(fiber) - float(ash)

        self.table.setItem(0, 7, QTableWidgetItem(str(protein)))
        self.table.setItem(0, 8, QTableWidgetItem(str(fat)))
        self.table.setItem(0, 9, QTableWidgetItem(str(fiber)))
        self.table.setItem(0, 10, QTableWidgetItem(str(ash)))
        self.table.setItem(0, 11, QTableWidgetItem(str(calc)))
        self.table.setItem(0, 12, QTableWidgetItem(str(fosf)))
        self.table.setItem(0, 13, QTableWidgetItem(str(koefMiner)))
        self.table.setItem(0, 14, QTableWidgetItem(str(magn)))
        self.table.setItem(0, 15, QTableWidgetItem(str(natr)))
        self.table.setItem(0, 16, QTableWidgetItem(str(kal)))
        self.table.setItem(0, 19, QTableWidgetItem(str(water)))
        self.table.setItem(0, 20, QTableWidgetItem(str(ugl)))
 
        
        
        
        '''self.addToTable(protein, 7)
        self.addToTable(fat, 8)
        self.addToTable(fiber, 9)
        self.addToTable(ash, 10)

        self.addToTable(calc, 11)
        self.addToTable(fosf, 12)
        self.addToTable(koefMiner, 12)
        self.addToTable(magn, 13)
        self.addToTable(natr, 14)

        self.addToTable(kal, 15)'''
       
        
        
        
        
        
        
        
        
    






app = QApplication(sys.argv)
window = MainWindow()
window.show()  # Важно: окно по умолчанию скрыто.

app.exec()