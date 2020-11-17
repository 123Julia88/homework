

x_matrix = 4    #задаем размер матрицы кол-во стобцов
y_matrix = 4    #задаем размер матрицы кол-во строк
point_X = 0     #эти 2 переменные это координаты нашей будущей точки нолик и икрестик
point_Y = 0
count = 0       # счетчик на выигрыш
playersOrder = 0 # счетчик ходов


def matrixPrint(matrix):                                            #функция печати матрицы (нашей доски)
     
    for x in range(len(matrix)):                                    # столбцы
        for y in range(len(matrix[x])):                             #строки
        
            print(matrix[x][y], end=' ')                            # печатаем через пробел

        print()                                                     #след. строка

def checkPoint(point):                                              #функиця проверки правильности введенных координат

    while True:
        if not point.isnumeric():                                                   #проверяем что координата число
            point = input("Вы ввели не число. Попробуйте снова: ")                  # или предлагаем ввести повторно
        elif 1 < int(point) > 3:                                                    #проверяем что координата число из нужного нам диапазона от 1 до 3
            point = input("Ваше число не диапазоне от 1 до 3. Попробуйте снова: ")  # или предлагаем ввести снова
        else:
            return int(point)                                                       # если условия прошли возращаем координату ввиде числа.
        
        



def enterPoint():                                                                   #функция ввода координатов точки 
    point_X = 0
    point_Y = 0
    
    
    
    point_Xin = (input("Введите координаты точки в формате столбик (число) "))       #вводим точку (х или у)
    point_X = checkPoint(point_Xin)                                                  #и вызываем сразу фукцию проверки



    point_Yin = (input("Введите координаты точки в формате строка (число) ")) 
    point_Y = checkPoint(point_Yin)




    if matrix[point_Y][point_X] == "-" :                                            #и проверяем сразу, чтобы когда ставили крестик или нолик, то точку на пустое место
        return point_X, point_Y
    else:  
        print("По указанным координатам уже есть метка. введите новые координаты")  # или предлагаем ввести новые координаты
        enterPoint()                                                                # и запускаем запрос новых координат

def moveKross(point_X, point_Y, matrix):                                         
    count = 0                                                                       #функция хода крестиком

    matrix[point_Y][point_X] = "x"

    if matrix[1][point_X] == matrix[2][point_X]  == matrix[3][point_X] or matrix[point_Y][1] == matrix[point_Y][2]  == matrix[point_Y][3] or matrix[1][3] == matrix[2][2] == matrix[3][1] == "x" or matrix[1][1] == matrix[2][2] == matrix[3][3] == "x":  
        print("Победил игрок КРЕСТИК")            #функция хода крестиком проверяем по кооринатам горизонатль вертикаль и обе диагоноли, не крестики ли после того как сделали ход

        count = 4

        

    return matrix, count    

def moveZerro(point_X, point_Y, matrix):    #функция хода ноликом
    count = 0 
    matrix[point_Y][point_X] = "o"   

    if matrix[1][point_X] == matrix[2][point_X]  == matrix[3][point_X] or matrix[point_Y][1] == matrix[point_Y][2]  == matrix[point_Y][3] or matrix[1][3] == matrix[2][2] == matrix[3][1] == "o" or matrix[1][1] == matrix[2][2] == matrix[3][3] == "o":  
        print("Победил игрок НОЛИК")    #функция хода ноликом проверяем по кооринатам горизонатль вертикаль и обе диагоноли, не крестики ли после того как сделали ход
        count = 4        # если да ставим счетчик на поебду

    return matrix, count    


#создаем матрицу 4 на 4 
matrix = []
for i in range(x_matrix):
    matrix.append(["-"]*y_matrix)
    matrix[0][i] = i  # и заполняем номера строк и столбцов
    matrix[i][0] = i


#печатаем ее
matrixPrint(matrix)



while count<2 :             # условие счетчика. пока не победа продолжаем ходить
    playersOrder +=1        # считаем ходы
    print("Ход №",playersOrder)
    if playersOrder % 2 == 0:  #условие на чет нечет
        print("Игрок Нолик Введите координаты")
        point_X, point_Y = enterPoint() # ставим точку
        matrix, count = moveZerro(point_X, point_Y, matrix) #возвращаем матрицу с поставленной точкой
    else:
        print("Игрок Крестик Введите координаты") #аналогично
        point_X, point_Y = enterPoint()
        matrix, count = moveKross(point_X, point_Y, matrix)

    if playersOrder >8:                     #если все клетки заполнены то объявляем ничью и сзаканчиваем партию
        print("Ничья!!!")
        count = 4
    matrixPrint(matrix)  # не забываем печатать матрицу


