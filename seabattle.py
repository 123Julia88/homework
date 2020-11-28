import random


class Ship():                                                         #описываю класс корябля
    def __init__(self, dimension, y_Point, x_Point):                            
        self.dim = dimension                                            # есть размер
        self.y_Point = y_Point                                          # координаты начала
        self.x_Point = x_Point

    def shipCoordinates(self, dimension, y_Point, x_Point):             # у класса корабль есть метод получения  координат корябля
        i = 0                               
        position = []                                                   # фактически по начальной координате и размеру моделируем остальное корабль
        for i in range(dimension):
            position.append(["-"]*2)

        i = 0
        while i < dimension:
            j = 0
            position[i][j] = y_Point
            j= 1
            while j < 2:
                position[i][j] = x_Point+i
                j += 1
            i += 1


        return position                                             # и возвращем координаты корабля
        
        
        
class Battlefield():                    # класс поля игрового
    def __init__(self): 
        
        i = 0                                        #присваиваем 
        x_matrix = 7    #задаем размер матрицы кол-во стобцов
        y_matrix = 7    #задаем размер матрицы кол-во строк
        
        self.numberOfShips = 11


        self.matrix = []                                #Создаем матрину поля. 
        for i in range(x_matrix):
            self.matrix.append(["."]*y_matrix)
            self.matrix[0][i] = i  # и заполняем номера строк и столбцов
            self.matrix[i][0] = i   

    def matrixPrint1(self):                                            #метод класса печати (нашей доски)
        x = 0
        y = 0
        for x in range(len(self.matrix)):                                    # столбцы
            for y in range(len(self.matrix[x])):                             #строки
        
                print(self.matrix[x][y], end=' ')                            # печатаем через пробел

            print()                                                     #след. строка

    def positionChecking(self, dimension, y_Point, x_Point, matrix, yPosOffset, yNegOffset, xPosOffset, xNegOffsetm, aiFlag):    #  метод проврки положения на поля корабля
        i = 0
        flagPlace = False


        if (x_Point+dimension-1) > 6 and dimension > 1 :                # сначала проверяеям прпалаем ли мы в поле числом
            return flagPlace


        yPosOffset = 1                               # устанавлиеваем смещения для проверки координаты корабля на одну клетку.               
        yNegOffset = -1             
        xPosOffset = 1
        xNegOffset = -1
        if y_Point == 6:                             #  проверяем, если значение координаты предельное то нулим в нужную сторону смещение, чтобы не вылететь за поле на проверке
            yPosOffset = 0
        if y_Point == 1:
            yNegOffset = 0
        if (x_Point+dimension) > 6:
            xPosOffset = 0
        if x_Point == 1:
            xNegOffset = 0

        while i < dimension:                        # ну и дальше идем по длинне корябля и проверяем на наличие других кораблей в ближайшей клетке

            if self.matrix[y_Point+yNegOffset][x_Point+i] != "." or self.matrix[y_Point][x_Point+i] != "." or self.matrix[y_Point+yPosOffset][x_Point+i] != "." or self.matrix[y_Point][x_Point+xNegOffset+i] != "." or self.matrix[y_Point][x_Point+xPosOffset+i] != ".":
                flagPlace = False
                if aiFlag == False:                 # Если ход человека то пишем ниже фразу. если комп то нет, чтобы не спамить
                    print("Нельзя располагать корабли рядом. Осуществите ввод еще раз")
                return flagPlace

            i +=1

        flagPlace = True            # если не нашли рядом кораблей то возвращаем тру.
        return flagPlace

    def shipKill(self):                 # медод класса убийство корябля. в случае попадания отнимает от общего числа живых палуб одну
        self.numberOfShips -= 1
        print(self.numberOfShips)

    def getAliveShip(self):
        return self.numberOfShips       # геттер поля. возвращаем кол-во живых кораблей на поле.
        

    def moveCheck(self, y_move, x_move, moveLog, aiFlag, matrix3):      # метод проверки возможности хода на поле
        move = [0]                                                      # делаем список

        if 1 <= y_move <= 6 and 1 <= x_move <= 6:                       # проверяем, что ходом попали в поле
            move = [y_move, x_move]                                     # нашему локальному списку присваиваем координаты поля
   
            if move not in moveLog:                                     # т.к. все ходы записываем в общий лог ходов
                moveLog.append([y_move, x_move])                        # то проверяем на наличие нашего хода в общем логе ходов
            else:
                if not aiFlag:                                          # ниже сообщение выводим только если ходит игрок
                    print("Такой ход уже был. Попробуйте ввести заново") 
                
                flag = False                                            # если условие не соблюли то возвращаем фолс.
                return flag, moveLog, matrix3                           # матрица три это не объект а просто "картинка" для изобращения ходов игрока,
                                                                        # чтобы не палить где корабли компа
        else:
            if not aiFlag:
                print("Координаты должны быть от 1 до 6. Попробуйте ввести заново")
            flag = False
            return flag, moveLog, matrix3 
         
        if self.matrix[y_move][x_move] == ".":                          # соответственно, если  в месте удара была пустотам то
            if not aiFlag:                                              # для хода игрока
                self.matrix[y_move][x_move] = "T"                       # ставим промах в поле кораблей компа
                matrix3[y_move][x_move] = "T"                           # и промах в поле изображения ходов
            else:
                self.matrix[y_move][x_move] = "T"                       # а для компа игроку рисуем промах в поле игрока

            if not aiFlag:                                                 # и для игрока печатаем результат
                print("____________Поле ИИ___________") 
            else:
                print("_____________Поле ИГРОКА_______________")
            print("Мимо!")


            if not aiFlag:

                x = 0                                                   # т.к. игроку нельзя палить поле компа. 
                y = 0                                                   # то печатаем матрикс 3 которая только изображаем ходы
                for x in range(len(matrix3)):                                    # столбцы
                    for y in range(len(matrix3[x])):                             #строки
                        print(matrix3[x][y], end=' ')                            # печатаем через пробел
                    print()   
                print("______________________________")
            else:
                self.matrixPrint1()  
                      

            flag = True
            return flag, moveLog, matrix3

        else:                                                           # все аналогично, если при ходе попали в корабль
            if not aiFlag:
                self.matrix[y_move][x_move] = "X"
                matrix3[y_move][x_move] = "X"
            else:
                self.matrix[y_move][x_move] = "X"                


            if not aiFlag:

                print("____________Поле ИИ___________") 
            else:

                print("_____________Поле ИГРОКА_______________")
            print("Попал!")

            if not aiFlag:

                x = 0
                y = 0
                for x in range(len(matrix3)):                                    # столбцы
                    for y in range(len(matrix3[x])):                             #строки
                        print(matrix3[x][y], end=' ')                            # печатаем через пробел
                    print() 
                print("______________________________")
  
            else:
                self.matrixPrint1()   

            
            self.shipKill()                                                     # при попадании также используем свойство поля уменьшить кол-во живых палуб на поле
            flag = True  
            return flag, moveLog, matrix3

        
        
    def setShip(self, coordinates, matrix, dimension):                          # еще один метод поля. берем координаты корабля и по ним ставим корабль

        i = 0 
        while i < dimension:
            j = 0
            y_Point = coordinates[i][j] 
            j= 1
            while j < 2:
                x_Point = coordinates[i][j]

                self.matrix[y_Point][x_Point] = "■"
                j += 1
            i += 1

        
    

def numberEnter(number, flag):                              # наша проверка, что все числа, которые вводятся челочисленные. и от 1 до 6 (в поле)

    try:
        number = int(number)

        if number > 6 or number < 1:                          # проверка что координата от 1 до 6
            print("Координаты должны быть цифра от 1 до 6")
            flag = False
            return number, flag 

        flag = True
        return int(number), flag

    except:
        return number, flag    
    


#def matrixPrint(matrix):                                            #функция печати матрицы (нашей доски)
#     
#    for x in range(len(matrix)):                                    # столбцы
#        for y in range(len(matrix[x])):                             #строки
#        
#            print(matrix[x][y], end=' ')                            # печатаем через пробел#

#        print()                                                     #след. строка


def enterData(dim3ship, dim2ship, dim1ship, aiFlag):                #функция ввода данных (в игру) для установке кораблей
                                                         #
    flagGlobal = False                                          # метка №1 если она не ок, то делаем вводы
    while not flagGlobal:

        flag = False                                            # метка №2 - пока она не тру вводим размер корабля
        while not flag:
            if aiFlag == False:                                    # если ходит игрок
                dimension = input("Введите размер корабля №")
                dimension, flag = numberEnter(dimension, flag)      # закидываем проверку возвращаем либо фолс либо тру (если все ок)

            elif dim3ship !=0 and aiFlag:                           # а вот тут интересно. Очень часто комп не мог расставить корабли на поле
                dimension = 3                                       # если рандомно генерировать размер
                flag = True                                         # потом пришлось сначала ставить большой. потом средние и потом мелочь. Тогда получается всегда.

            elif dim2ship !=0 and dim3ship == 0 and aiFlag: 
                dimension = 2
                flag = True

            
            else:
                
                dimension = 1

                flag = True

            if flag:
                if dimension == 3 and dim3ship > 0 :             # проверяем что корабли у нас 1 2 или 3 и уменьшаем количество
                    dim3ship -= 1

                elif dimension == 2 and dim2ship >0  :
                    dim2ship -= 1

                elif dimension == 1 and dim1ship > 0  :
                    dim1ship -= 1

                elif dimension != 1 or dimension != 2 or dimension != 3 :
                    if aiFlag == False:
                        print("Размер корабля введен не правильно. должно быть 1, 2 или 3")   # иначе просим ввести правильный размер корабля
                        flag = False 
                    else:
                        flag = False                                                           # и ставим метку №2 фолс чтобы повторить ввод

                else:
                    if aiFlag == False:
                        print("Такие корабли закончились. Введите другой размер корабля ")
                        flag = False        
                    else:
                        flag = False                                                                                              # если все проверки прошли, значит номер корабля это правильная цифра
                

        flag = False                                                    # опять ставим метку №2 на фолс и пока она не тру делаем ввод и проверку координат
        while not flag:
            if aiFlag == False:
                y_Point = input("укажите координату по Y")
                y_Point, flag = numberEnter(y_Point, flag)                  # стандартной функцией проверяем что у нас цифра.
            else:
                y_Point = random.randint(1, 6)

                flag = True 

            if flag:
                if y_Point > 6 or y_Point < 1:                          # проверка что координата от 1 до 6
                    print("Координаты должны быть цифра от 1 до 6")
                    flag = False                                        # и запускаем этот цикл по новой

        flag = False                                                    #  аналогично для х
        while not flag:
            if aiFlag == False:
                x_Point = input("укажите координату по X")
                x_Point, flag = numberEnter(x_Point, flag)
            else:
                x_Point = random.randint(1, 6-dimension+1)

                flag = True 


            if flag:
                if x_Point > 6 or x_Point < 1:
                    print("Координаты должны быть цифра от 1 до 6")
                    flag = False
        
                flagGlobal = True
                return x_Point, y_Point, dimension, dim3ship, dim2ship, dim1ship


x_matrix = 7    #задаем размер матрицы кол-во стобцов
y_matrix = 7    #задаем размер матрицы кол-во строк
shipsPlayer = [0]*7   # хранилище кораблей игроков
shipsAI = [0]*7        # хранилище кораблей компа
aiFlag = False          # ходить будет сначала игрок
            
matrix1 = Battlefield()         # создаем поле человека
matrix2 = Battlefield()         # и поле компа
matrix3 = []                    # и поле изображения ходов человека
for i in range(x_matrix):
    matrix3.append(["."]*y_matrix)
    matrix3[0][i] = i  # и заполняем номера строк и столбцов
    matrix3[i][0] = i


#печатаем поля 

matrix1.matrixPrint1()
print("Электрический разум: ")
print("________________")
matrix2.matrixPrint1()

#shipBasePlayer = [0]*7
#shipBaseAI = [0]*7


#Делаем расстановку кораблей
dim3ship = 1            #кол-во доступных кораблей
dim2ship = 2
dim1ship = 4

i = 0

#aiFlag = True           #переключатель на AI, чтобы игра начиналась с расстановки кораблей компа. плеей прокускается. для отладки.
#i = 7
while i < 14:                                                    # Начинаем расставлять 6 кораблей
    
    if aiFlag == False:                                                            #
        print("Кораблей доступно для установки: ")                  # выдаем сколько и каких кораблей можно расставить еще. только человеку.
        print("3х палубных кораблей для установки: ", dim3ship)
        print("2х палубных кораблей для установки: ", dim2ship)
        print("1х палубных кораблей для установки: ", dim1ship)
       
    flagGlobal = False                                          # метка №1 если она не ок, то делаем вводы
    while not flagGlobal:
        x_Point, y_Point, dimension, dim3ship, dim2ship, dim1ship = enterData(dim3ship, dim2ship, dim1ship, aiFlag)  # через функцию ввода данных расставляем корабли

        flag = False
        flagPlace = False
        yPosOffset = 1
        yNegOffset = -1
        xPosOffset = 1
        xNegOffset = -1
        if y_Point == 6:
            yPosOffset = 0
        if y_Point == 1:
            yNegOffset = 0
        if (x_Point+dimension) > 6:
            xPosOffset = 0
        if x_Point == 1:
            xNegOffset = 0

        while not flagPlace:              #значит идея какая надо сделать 4 проверки. слева. права. снизу. сверху. 

            if aiFlag == False:  #используем разные поля для установки для компа и для человека
                flagPlace = matrix1.positionChecking(dimension, y_Point, x_Point, matrix1, yPosOffset, yNegOffset, xPosOffset, xNegOffset, aiFlag)
            else:
                flagPlace = matrix2.positionChecking(dimension, y_Point, x_Point, matrix2, yPosOffset, yNegOffset, xPosOffset, xNegOffset, aiFlag)

            if flagPlace == False:
                if dimension == 3:             # проверяем что корабли у нас 1 2 или 3 и увеличиваем обратно количество
                    dim3ship += 1               # потому что в проверке мы уже уменьшили. Но видимо чтото пошло не так и надо откатить уменьшение.

                elif dimension == 2:
                    dim2ship += 1

                elif dimension == 1:
                    dim1ship += 1


                x_Point, y_Point, dimension, dim3ship, dim2ship, dim1ship = enterData(dim3ship, dim2ship, dim1ship, aiFlag)

            else:
                flagPlace = True
                flagGlobal = True


        if aiFlag == False:
            shipsPlayer[i] = Ship(dimension, y_Point, x_Point)                                  # добавляем наш новый корабль в хранилище кораблей
            coordinates = shipsPlayer[i].shipCoordinates(dimension, y_Point, x_Point)           # получаем координаты его из метода класса кораблей
        else:
            shipsAI[i-7] = Ship(dimension, y_Point, x_Point)                                    # тоже, но для компа
            coordinates = shipsAI[i-7].shipCoordinates(dimension, y_Point, x_Point)

    
        if aiFlag == False:
            matrix1.setShip(coordinates, matrix1, dimension)
            print("Кораблей доступно для установки: ")                  # выдаем сколько и каких кораблей можно расставить еще для челоека
            print("3х палубных кораблей для установки: ", dim3ship)
            print("2х палубных кораблей для установки: ", dim2ship)
            print("1х палубных кораблей для установки: ", dim1ship)
            matrix1.matrixPrint1()
        else:
            matrix2.setShip(coordinates, matrix2, dimension) 


    if i == 6:                      # первые семь кораблей ставил человек. Вторые шеть ставит комп.
        dim3ship = 1                # тут переключатель устаноки кораблей человек / комп
        dim2ship = 2
        dim1ship = 4
        aiFlag = True
    if i < 6:
        aiFlag = False        

        
    i += 1



print("!!!!!!!!Игра начинается!!!!!!")
print("________________")


moveLog1 = [0]                  # это лог ходов для человека
moveLog2 = [0]                  # и для компа
gameFlagGlobal = False
aiFlag = False
i = 0
while not gameFlagGlobal:
    flagMove = False
    while not flagMove:

        if i % 2 == 0:     # ходы икрок / ПК
            aiFlag = False
        else: 
            aiFlag = True 

        flag = False
        while not flag:
            if not aiFlag:
                y_move = input("Введите Y для хода: ")      # вводим координаты. прогоняем обычной функцие проверки
                y_move, flag = numberEnter(y_move, flag)
            else:
                y_move = random.randint(1, 6)               # а комп просто генерирует число от 1 до 6 и проверка не нужна
                flag = True

        flag = False
        while not flag:
            if not aiFlag:
                x_move = input("Введите X для хода: ")          # тоже самое вторая координата
                x_move, flag = numberEnter(x_move, flag)
            else:
                y_move = random.randint(1, 6)
                flag = True


        if not aiFlag:
            flag, moveLog2, matrix3 = matrix2.moveCheck(y_move, x_move, moveLog2, aiFlag, matrix3)   # проверяем результат хода методом класса поля
        else:
            flag, moveLog1, matrix3 = matrix1.moveCheck(y_move, x_move, moveLog1, aiFlag, matrix3)             

        if flag:                    # если попали - считаем
            i += 1


            
        if not aiFlag:                                      # тут методом класса считаем кол-во живых кораблей. если ноль - значит победа.
            numberOfShips = matrix2.getAliveShip()
            if numberOfShips == 0:
                print("Игра закончена. Победил Игрок")
                gameFlagGlobal = True
                flagMove = True

        else:
            numberOfShips = matrix1.getAliveShip()
            if numberOfShips == 0:
                print("Игра закончена. Победил Искуственный РазумЪ")
                gameFlagGlobal = True
                flagMove = True




        



