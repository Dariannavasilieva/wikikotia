import re
import itertools 
import pandas as pd

carbohydrates = ["рис", "горох", "злаки", "пшеница", "кукуруза", "маис", "картофель", "овес", "ячмень", "сорго", "киноа", "спельта"]
antiacs = ["розмарин", "чай", "чая", "соль", "хлорид натрия", "антиоксидант"]
special = ["пробиоти"]
cellulose = ["яблок", "целлюл", "свек", "подорожн", "псиллиу", "волокн", "тыква"]
prebiotics = ["инулин", "дрож", "сахарид", "mos", "xos", "юкка" ]
meatList = ["сельдь", "утка", "куриц", "говяд", "телят", "индей", "треска", "мяс", "субпро", "гидролиз", "яйц", "креветк"]
marketing = ["дыня", "апельсин", "курку", "шпинат", "арбуз", "брусник", "алоэ", "гранат", "черник", "морко", "клюкв", "глюкозамин", "хондроитин"]
class ParsingComposition ():
    def __init__ (self, Ingridients, GA, Vitamins, id, brandName, lineName, spesialName, favorName, age, anymalType, kkal, note, granul):
        self.ga_dict = dict()
        self.ga_dict['ID'] = id
        self.ga_dict['животное'] = anymalType
        self.ga_dict['возраст'] = age
        self.ga_dict['бренд'] = brandName
        self.ga_dict['направление'] = spesialName
        self.ga_dict['линейка'] = lineName
        self.ga_dict['вкус'] = favorName
        
        self.ga_dict['белок'] =0
        self.ga_dict['жиры'] = 0
        self.ga_dict['клетчатка'] = 0
        self.ga_dict['зола'] = 0
        self.ga_dict['кальций'] = 0
        self.ga_dict['фосфор'] = 0
        self.ga_dict['коэфминерал'] = 0
        self.ga_dict['магний'] = 0
        self.ga_dict['натрий'] = 0
        self.ga_dict['калий'] = 0
        self.ga_dict['омега3'] = 0
        self.ga_dict['омега6'] = 0
        self.ga_dict['коэфомег'] = 0
        self.ga_dict['влажность'] = 0
        self.ga_dict['углеводы'] = 0
        self.ga_dict['энергия_упак'] = kkal
        self.ga_dict['энергия_гост'] =0
        self.ga_dict['epa'] = 0
        self.ga_dict['dha'] = 0

        self.compos_dict = dict()
        self.compos_dict['ID'] = id
        self.compos_dict['животное'] = anymalType
        self.compos_dict['возраст'] = age
        self.compos_dict['бренд'] = brandName
        self.compos_dict['направление'] = spesialName
        self.compos_dict['линейка'] = lineName
        self.compos_dict['вкус'] = favorName
        self.compos_dict['белки'] = []
        self.compos_dict['жиры'] = []
        self.compos_dict['углеводы'] = []
        self.compos_dict['клетчатка'] = []
        self.compos_dict['пребиотики'] = []
        self.compos_dict['специальное'] = []
        self.compos_dict['антиоксиданты'] = []
        self.compos_dict['маркетинг'] = []

        self.foodAbout = dict()
        self.foodAbout['ID'] = id
        self.foodAbout['животное'] = anymalType
        self.foodAbout['возраст'] = brandName
        self.foodAbout['бренд'] = brandName
        self.foodAbout['направление'] = spesialName
        self.foodAbout['линейка'] = lineName
        self.foodAbout['вкус'] = favorName
        self.foodAbout['ингридиенты'] = Ingridients
        self.foodAbout['га'] = GA
        self.foodAbout['добавка'] = Vitamins
        self.foodAbout['калории'] = kkal
        self.foodAbout['гранулы'] = granul
        self.foodAbout['примечание'] = note




        self.vit_dict = dict ()
        self.vit_dict['ID'] = id
        self.vit_dict['животное'] = anymalType
        self.vit_dict['возраст'] = brandName
        self.vit_dict['бренд'] = brandName
        self.vit_dict['направление'] = spesialName
        self.vit_dict['линейка'] = lineName
        self.vit_dict['вкус'] = favorName
        self.vit_dict['a'] = 0
        self.vit_dict['d'] = 0
        self.vit_dict['e'] = 0
        self.vit_dict['b1'] = 0
        self.vit_dict['b2'] = 0
        self.vit_dict['b3'] = 0
        self.vit_dict['b5'] = 0
        self.vit_dict['b6'] = 0
        self.vit_dict['b7'] = 0
        self.vit_dict['b9'] = 0
        self.vit_dict['b12'] = 0
        self.vit_dict['холин'] = 0
        self.vit_dict['цинк'] = 0
        self.vit_dict['марганец'] = 0
        self.vit_dict['железо'] = 0
        self.vit_dict['йод'] = 0
        self.vit_dict['медь'] = 0
        self.vit_dict['селен'] = 0
        self.vit_dict['таурин'] = 0
        self.vit_dict['метионин'] = 0
        self.vit_dict['k'] = 0
        

        self.Vitamins = list()
        

        self.parsingIngredients(Ingridients)
        self.parsingGA(GA)
        
        self.parsingVit(Vitamins)
        print('--------------Ингридиенты-----------------')
        print(self.compos_dict)
        print('--------------ГА-----------------')
        print(self.ga_dict)
        print('--------------Витамины-----------------')
        print(self.vit_dict)
        

        



    def parsingIngredients(self, ingredients):
        ingredients = ingredients.lower()


        ingredients = re.sub(r'(\d),(\d)', r'\1.\2', ingredients)       
        ingredients = re.split(r'[;,]', ingredients) # разделить ингредиенты в список, разделитель или , или ;
        #print ('список всех ингридиентов:', ingredients)
        
        newIngredients = []
        # приводим строки к приличному виду
        i = 0

        maxLen = len(ingredients)
        while i < maxLen:
            ingredients[i] = re.sub(r'^\s+', '', ingredients[i])
            #print(ingredients[i])
            # объединяем компоненты в скобках
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
         

        self.IngredientsDict(newIngredients)


# функция распределения ингридиентов на источники белков, жиров, углеводов и т.п
    def IngredientsDict(self, newIngredients):
        carboList = []
        protinList = []
        fatList = []
        anotherList = []
        antiacsList = []
        celluloseList = []
        prebioticList = []
        specList = []
        marketingList = []

        for ingredient in newIngredients:
                #ingredient = ingredient.lower()
                carboFlag = False
                antiacsFlag = False
                meatFlag = False
                celluloseFlag = False
                prebioticFlag = False
                specFlag = False
                marketingFlag = False
                for (i, j, k, n, m, l, r) in itertools.zip_longest(carbohydrates, antiacs, meatList, cellulose, prebiotics, special, marketing):
                    if n != None:
                        if n in ingredient:
                            celluloseFlag = True
                            
                    if i != None:
                        if (i in ingredient) and celluloseFlag == False:
                            carboFlag = True
                            
                    if j != None:
                        if j in ingredient:
                            antiacsFlag = True
                    if k != None:
                        if k in ingredient:
                            meatFlag = True

                    
                    if m != None:
                        if m in ingredient:
                            prebioticFlag = True
                    if l != None:
                        if l in ingredient:
                            specFlag = True
                    if r != None:
                        if r in ingredient:
                            marketingFlag = True
                            

                if celluloseFlag:
                    celluloseList.append(ingredient)
                elif carboFlag:
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
                elif marketingFlag:
                    marketingList.append(ingredient)
                elif prebioticFlag:
                    prebioticList.append(ingredient)
                elif specFlag:
                    specList.append(ingredient)
                else:
                    anotherList.append(ingredient)

        
        self.compos_dict['белки'] = protinList
        self.compos_dict['жиры'] = fatList
        self.compos_dict['углеводы'] = carboList
        self.compos_dict['антиоксиданты'] = antiacsList
        self.compos_dict['другое'] = anotherList
        self.compos_dict['клетчатка'] = celluloseList
        self.compos_dict['пребиотики'] = prebioticList
        self.compos_dict['специальное'] = specList
        self.compos_dict['маркетинг'] = marketingList
        

        


    def findNumber(self, GA, word):
    
        #pattern1 = r'\s{word}\w*[^A-Za-z]{,8}?\d+[,.]\d+'
        '''pattern1 = r'{}'.format(word)
        pattern1 += r'\w*[^A-Za-z]{,8}?\d+[,.]\d+'
        pattern2 = fr'{word}\w*[^A-Za-z]*?\d+'''
        number = []
        pattern1 = r'\d+[,.]\d+'
        #print("findNumber ",GA)
        if len(re.findall(pattern1, GA)) == 0:
            number = re.findall(r'\d+', GA)[0]
        else:
            number = re.findall(r'\d+[,.]\d+', GA)[0]
        if len(number) == 0:
            number = 0
        '''number = re.findall(r'\d+[,.]\d+', GA)[0]
        if len(number) == 0:
            number = re.findall(r'\d+', number)[0]
            if len(number) == 0:
                number = 0'''

        return number


        '''if GA.find(word) != -1: 
            if len(re.findall(pattern1, GA)) == 0: # искать подстроку бел... далее символы отличные от букв, не более 5, затем дробное число
                number = re.findall(pattern2, GA)[0]
                number = re.findall(r'\d+', number)[0]
                return number
            else:
                number = re.findall(pattern1, GA)[0]
                number = re.findall(r'\d+[,.]\d+', number)[0]
                number = number.replace(',', '.')
                return number
        else:
            print('Значение', word ,'не найдено в гарантированном анализе!')
            return number'''

    def kkalGOST_cats(self, protein, fat, fiber, water, ash):
        ugl = 100 - (protein + fat + fiber + water + ash)
        val_enrg = 5.7 * protein + 9.4 * fat + 4.1 * (ugl + fiber)
        usv_energ = 87.9 - (0.88 * fiber * 100) / (100 - water)
        perev_energ = val_enrg * usv_energ / 100
        obmen_energ = perev_energ - (0.77 * protein)
        return round(obmen_energ,2)



    def parsingGA(self, GA):
        GA = GA.lower()
        GA = re.sub(r'(\d),(\d)', r'\1.\2', GA)  
        

        protein, fat, fiber, ash= 0, 0, 0, 0
        calc, fosf, magn, natr, kal = 0, 0, 0, 0, 0
        koefMiner, koefOmeg = 0, 0
        water = 10
        omega3, omega6, epa, dha = 0, 0, 0, 0
        anotherList = list()
     
        GA = re.split(r'\.(?!\d)|(?<=\d)\.(?!\d)|[;,]', GA)

        
        for i in GA:
            findNutrientFlag = False
            if i.find('бел') != -1 or i.find('прот') != -1:
                protein = self.findNumber(i, 'бел')
                findNutrientFlag = True
            '''elif i.find('прот') != -1:
                protein = self.findNumber(i, 'прот')
                findNutrientFlag = True'''

    
            #----------жиры----------
            if i.find('масл') != -1 or i.find('жир') != -1: 
                fat = self.findNumber(i, 'масл')
                findNutrientFlag = True
            '''elif i.find('жир') != -1: 
                fat = self.findNumber(i, 'жир')
                findNutrientFlag = True'''
            

            #----------клетчатка----------
            if i.find('клетчат') != -1:
                fiber = self.findNumber(i, 'клетчат')
                findNutrientFlag = True
        
            #----------влажность----------
            if i.find('вла') != -1:
                water = self.findNumber(i, 'вла')
                findNutrientFlag = True
                
                

            #----------зольность----------
            if i.find('зол') != -1:                   
                ash = self.findNumber(i, 'зол')
                findNutrientFlag = True
        
            #----------кальций----------
            if i.find('каль') != -1: 
                calc = self.findNumber(i, 'каль')
                findNutrientFlag = True
        
            #----------фосфор----------
            if i.find('фосф') != -1: 
                fosf = self.findNumber(i, 'фосф')
                findNutrientFlag = True
        
            #----------магний----------
            if i.find('магн') != -1: 
                magn = self.findNumber(i, 'магн')
                findNutrientFlag = True
        
            #----------натрий----------
            if i.find('натр') != -1: 
                natr = self.findNumber(i, 'натр')
                findNutrientFlag = True
                    
            #----------калий----------
            if i.find('кали') != -1: 
                kal = self.findNumber(i, 'кали')
                findNutrientFlag = True

            if i.find('омега-3') != -1:     
                omega3 = self.findNumber(i, 'омега-3')
                findNutrientFlag = True
            if i.find('омега-6') != -1: 
                omega6 = self.findNumber(i, 'омега-6')
                findNutrientFlag = True
            
            if i.find('epa') != -1:   
                subi = i[i.find('epa'):len(i)-1]  # на случай, если это значение прописано внутри омег
                epa = self.findNumber(subi, 'epa')
                findNutrientFlag = True
            if i.find('dha') != -1:
                subi = i[i.find('dha'):len(i)-1] 
                dha = self.findNumber(subi, 'dha')
                findNutrientFlag = True

        
            if not findNutrientFlag:
                
                anotherList.append(i)
            

        if water == 0: #если не указана, берем среднее значение
            water = 8 

        if fosf != 0 and calc != 0:
            koefMiner = round(float(calc)/float(fosf),2)
        else:
            koefMiner = 0

        if omega6 != 0 and omega3 != 0:
            koefOmeg = round(float(omega6)/float(omega3),2)
        else:
            koefOmeg = 0
 
        self.compos_dict['специальное'] = self.compos_dict['специальное'] + anotherList
        self.ga_dict['белок'] = protein
        self.ga_dict['жиры'] = fat   
        self.ga_dict['клетчатка'] = fiber      
        self.ga_dict['зола'] = ash
        self.ga_dict['влажность'] = water
        self.ga_dict['кальций'] = calc
        self.ga_dict['фосфор'] = fosf
        self.ga_dict['коэфминерал'] = koefMiner
        self.ga_dict['магний'] = magn
        self.ga_dict['натрий'] = natr
        self.ga_dict['калий'] = kal
        self.ga_dict['омега3'] = omega3
        self.ga_dict['омега6'] = omega6
        self.ga_dict['коэфомег'] = koefOmeg
        self.ga_dict['углеводы'] = 100 - (float(protein) + float(fat) + float(fiber) + float(water) + float(ash)) 
        self.ga_dict['углеводы'] = round(self.ga_dict['углеводы'], 2 )
        self.ga_dict['энергия_гост'] = self.kkalGOST_cats(float(protein), float(fat), float(fiber), float(water), float(ash))
        self.ga_dict['epa'] = epa
        self.ga_dict['dha'] = dha


    def findAntioks(self, text):
        antiacsList = []
        for i in text:
            i = i.lower()
            for j in antiacs:
                if j in i:
                    antiacsList.append(i)
        self.compos_dict['антиоксиданты'] = self.compos_dict['антиоксиданты'] + antiacsList
        



    # функция обработки витаминной добавка
    def parsingVit(self, Vitamine):
        Vitamine = re.sub(r'(\d),(\d)', r'\1.\2', Vitamine)  
        Vitamine = re.split(r'[;]', Vitamine)
        
        subList = []
        anotherList = []
        antiacsList = []
        for i in Vitamine:
            subList = re.split(r'\.(?!\d)|(?<=\d)\.(?!\d)', i)
            #print(subList)
            if len(subList) > 1:
                self.Vitamins = self.Vitamins + subList
            else:
                self.Vitamins.append(i)
        

       
        a, d, e, c = 0, 0, 0, 0    
        b1, b2, b3, b5 = 0, 0, 0, 0
        b6, b7, b9, b12 = 0, 0, 0, 0
        holin = 0    
        zinc, copper, iod, iron = 0, 0, 0, 0
        manganese, selen = 0, 0 
        taurin, meteonin, k = 0, 0, 0
        for i in self.Vitamins:
            findNutrientFlag = False
            vit = i.lower()
            if i.find('Витамин A') != -1 or i.find('Витамин А') != -1:
                a = self.findNumber(i, 'a')
                findNutrientFlag = True

            if i.find('Витамин D3') != -1: 
                id = i.replace('D3', 'D')
                d = self.findNumber(id, 'д')
                findNutrientFlag = True
            if i.find('Витамин Д3') != -1: 
                id = i.replace('Д3', 'Д')
                d = self.findNumber(id, 'д')
                findNutrientFlag = True

            if i.find('Витамин C') != -1 or i.find('Витамин С') != -1: 
                anotherList.append(i)
                findNutrientFlag = True
        
            if i.find('Витамин E') != -1 or i.find('Витамин Е') != -1: 
                e = self.findNumber(i, 'e')
                findNutrientFlag = True
                
            if i.find('Витамин B1') != -1 or i.find('Витамин В1') != -1:                   
                b1 = self.findNumber(i, 'b1')
                findNutrientFlag = True

            if i.find('Витамин B2') != -1 or i.find('Витамин В2') != -1:
                b2 = self.findNumber(i, 'b2')
                findNutrientFlag = True

            if i.find('Витамин B3') != -1 or i.find('Витамин В3') != -1 : 
                b3 = self.findNumber(i, 'b3')
                findNutrientFlag = True
            if vit.find('ниацин') != -1:
                b3 = self.findNumber(i, 'b3')
                findNutrientFlag = True

            if i.find('Витамин B5') != -1 or i.find('Витамин В5') != -1 : 
                b5 = self.findNumber(i, 'b5')
                findNutrientFlag = True
            if vit.find('пантотен') != -1:
                b5 = self.findNumber(i, 'b5')
                findNutrientFlag = True

            if i.find('Витамин B6') != -1 or i.find('Витамин В6') != -1 : 
                b6 = self.findNumber(i, 'b6')
                findNutrientFlag = True

            if i.find('Витамин B7') != -1 or i.find('Витамин В7') != -1 : 
                b7 = self.findNumber(i, 'b7')
                findNutrientFlag = True
            if vit.find('биотин') != -1:
                b7 = self.findNumber(i, 'b7')
                findNutrientFlag = True
            
            if i.find('Витамин B9') != -1 or i.find('Витамин В9') != -1 : 
                b9 = self.findNumber(i, 'b9')
                findNutrientFlag = True
            if vit.find('фолие') != -1:
                b9 = self.findNumber(i, 'b9')
                findNutrientFlag = True

            if i.find('Витамин B12') != -1 or i.find('Витамин В12') != -1 :  
                b12 = self.findNumber(i, 'b12')
                findNutrientFlag = True
            
            if i.find('Витамин К') != -1 or i.find('Витамин K') != -1 : 
                k = self.findNumber(i, 'k')
                findNutrientFlag = True

            if vit.find('холин') != -1:  
                holin = self.findNumber(i, 'холин')
                findNutrientFlag = True

            if vit.find('цинк') != -1:  
                zinc = self.findNumber(i, 'цинк')
                findNutrientFlag = True
            
            if vit.find('марган') != -1:  
                manganese = self.findNumber(i, 'марган')
                findNutrientFlag = True

            if vit.find('желез') != -1:  
                iron = self.findNumber(i, 'желез')
                findNutrientFlag = True

            if vit.find('йод') != -1:  
                iod = self.findNumber(i, 'йод')
                findNutrientFlag = True

            if vit.find('медь') != -1:  
                copper = self.findNumber(i, 'медь')
                findNutrientFlag = True    

            if vit.find('селен') != -1:  
                selen = self.findNumber(i, 'селен')
                findNutrientFlag = True

            if vit.find('таурин') != -1:  
                taurin = self.findNumber(i, 'таурин')
                findNutrientFlag = True 

            if vit.find('метионин') != -1:  
                meteonin = self.findNumber(i, 'метионин')
                findNutrientFlag = True 
            
            if vit.find('карнитин') != -1:  
                
                findNutrientFlag = True
                anotherList.append(i)

            
            for j in antiacs:
                if j in vit:
                    antiacsList.append(i)
                    findNutrientFlag = True

            if not findNutrientFlag:
                anotherList.append(i)
            
        
        self.compos_dict['специальное'] = self.compos_dict['специальное'] + anotherList
        self.compos_dict['антиоксиданты'] = self.compos_dict['антиоксиданты'] + antiacsList
        
        self.vit_dict['a'] = a
        self.vit_dict['d'] = d
        self.vit_dict['e'] = e
        self.vit_dict['b1'] = b1
        self.vit_dict['b2'] = b2
        self.vit_dict['b3'] = b3
        self.vit_dict['b5'] = b5
        self.vit_dict['b6'] = b6
        self.vit_dict['b7'] = b7
        self.vit_dict['b9'] = b9
        self.vit_dict['b12'] = b12
        self.vit_dict['холин'] = holin
        self.vit_dict['цинк'] = zinc
        self.vit_dict['марганец'] = manganese
        self.vit_dict['железо'] = iron
        self.vit_dict['йод'] = iod
        self.vit_dict['медь'] = copper
        self.vit_dict['селен'] = selen
        self.vit_dict['таурин'] = taurin
        self.vit_dict['метионин'] = meteonin
        self.vit_dict['k'] = k
        
        



    def ListsToString (self):
        
        self.compos_dict['ID'] = id
        self.compos_dict['белки'] = ', '.join(self.compos_dict['белки'])
        self.compos_dict['жиры'] = ', '.join(self.compos_dict['жиры'])
        self.compos_dict['углеводы'] = ', '.join(self.compos_dict['углеводы'])
        self.compos_dict['клетчатка'] = ', '.join(self.compos_dict['клетчатка'])
        self.compos_dict['пребиотики'] = ', '.join(self.compos_dict['пребиотики'])
        self.compos_dict['специальное'] = ', '.join(self.compos_dict['специальное'])
        self.compos_dict['антиоксиданты'] = ', '.join(self.compos_dict['антиоксиданты'])
        self.compos_dict['маркетинг'] = ', '.join(self.compos_dict['маркетинг'])


    def createAllDataDict(self, id, brandName, lineName, spesialName, favorName, age, anymalType, kkal, note, ):
        self.allData_dict = dict()
        self.allData_dict['ID'] = id
        self.allData_dict['животное'] = anymalType
        self.allData_dict['возраст'] = age
        self.allData_dict['бренд'] = brandName
        self.allData_dict['направление'] = spesialName
        self.allData_dict['линейка'] = lineName
        self.allData_dict['вкус'] = favorName
        self.allData_dict['ингридиенты'] = self.foodAbout['ингридиенты']
        self.allData_dict['га'] = self.foodAbout['га']
        self.allData_dict['добавка'] = self.foodAbout['добавка']

        self.allData_dict['ист_белка'] = self.compos_dict['белки'] 
        self.allData_dict['ист_жиров'] = self.compos_dict['жиры'] 
        self.allData_dict['ист_углев'] = self.compos_dict['углеводы'] 
        self.allData_dict['ист_клетч'] = self.compos_dict['клетчатка'] 
        self.allData_dict['пребиотики'] = self.compos_dict['пребиотики']
        self.allData_dict['специальное'] = self.compos_dict['специальное'] 
        self.allData_dict['антиоксиданты'] = self.compos_dict['антиоксиданты'] 
        self.allData_dict['маркетинг'] = self.compos_dict['маркетинг'] 
        
         

        self.allData_dict['белок'] = self.ga_dict['белок'] 
        self.allData_dict['жиры'] = self.ga_dict['жиры'] 
        self.allData_dict['клетчатка'] = self.ga_dict['клетчатка'] 
        self.allData_dict['зола'] = self.ga_dict['зола'] 
        
        self.allData_dict['кальций'] = self.ga_dict['кальций'] 
        self.allData_dict['фосфор'] = self.ga_dict['фосфор'] 
        self.allData_dict['коэфминерал'] = self.ga_dict['коэфминерал'] 
        self.allData_dict['магний'] = self.ga_dict['магний']
        self.allData_dict['натрий'] = self.ga_dict['натрий'] 
        self.allData_dict['калий'] = self.ga_dict['калий'] 
        self.allData_dict['омега3'] = self.ga_dict['омега3'] 
        self.allData_dict['омега6'] = self.ga_dict['омега6'] 
        self.allData_dict['коэфомег'] = self.ga_dict['коэфомег'] 
        self.allData_dict['влажность'] = self.ga_dict['влажность'] 
        self.allData_dict['углеводы'] = self.ga_dict['углеводы'] 
        self.allData_dict['энергия_упак'] = kkal          
        self.allData_dict['энергия_гост'] = self.ga_dict['энергия_гост'] 
        self.allData_dict['epa'] = self.ga_dict['epa'] 
        self.allData_dict['dha'] = self.ga_dict['dha'] 
        
        self.allData_dict['витамины'] = ', '.join(self.Vitamins)
        self.allData_dict['примечание'] = note
        self.allData_dict['гранулы'] = self.foodAbout['гранулы']

    
        

        
