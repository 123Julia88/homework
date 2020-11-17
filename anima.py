class Animal():                                                         #описываю класс
    def __init__(self, kind, name, surname):                            
        self.kind = kind                                                #присваиваем тип животного
        self.name = name                                                # имя владельца
        self.surname = surname                                          # Фамилию владельца


    def getClient(self):                                                #геттер
        return self.name, self.surname, self.balance

    def setClient(self, balance):                                       #сеттер   
        if type(balance) == float:                                      #проверяем на то что это число
            self.balance = balance                                      # и приваиваем баланс

#описали класс переходим к программе
answer = 0                                                              #это переменная на выбор в меню
i = 0                                                                   #это итератор на список для сохранения клиентов
base = []                                                               # это массив, куда будем сохранять объекты
uchet = 1                                                               # это техническая переменная для проверки ввода

while answer < 2:                                                       # проверка на бесконечность
    print("--------Меню------------")
    uchet = input("Если Вы ходите ввести нового питомца - 1:\nЕсли хотите закончить работу - 2:\nЕсли хотите Вывести данные покупателя - 3:\nВыбор:  ")
    print("------------------------")

    if  uchet.isnumeric():                                              # проверяем ввод в меню на число (ясно что надо по идее сделать единую функцию на проверку чисел, но почему то долго писал это и не осталось времени)
        uchet = int(uchet)                                              # если число то делаем число
        if uchet == 2:                                                  # ну и поехали меню. 2 - то делаем 2 -это выход
            answer = 2

        elif uchet == 1:                                                # если 1 - то нулим новые переменны для нового объекта
            balance = "aa" 
            name = ""
            surname = ""
            kind = ""
            flag2 = False                                               # техническая переменная для проверки на число баланса


            kind = input("Какое животное: ")
            name = input("Имя клиента: ")
            surname = input("Фамилия клиента: ")
            
            while not flag2:
                balance = input("Баланс должен быть числом. Введите число: ")   # собственно так проверяю что баланс это число
            
                try:
                    balance = float(balance)
                    flag2 = True
                except:
                    flag2 = False                

            client = Animal(kind, name, surname)                            # все ок - создаем новый объект + через сеттер присваиваем баланс
            client.setClient(balance)

            base.append(client)                                             # добавляем это в наш список как новый член

            i += 1                                                          # после добавления счелкаем итератором

        elif uchet == 3:                                                               # вывод данных клиента в меню
            z = 0
            flag = False                                                    #техническая переменная. Если в базе нашлось имя - то выводим данные иначе фолс
            clientName = input("Введите имя клиента, по которому нужен баланс: ")

            for z in range(i):                                          # проверяем нашу базу. 
                checking = base[z]
                if checking.name == clientName:
                    print("Имя Клиента: ", checking.name, "Фамилия Клиента: ", checking.surname, "Баланс: ", checking.balance)   #находим = выводим данные
                    flag = True
                
            if flag == False:
                print("Данные по указанному клиенту отсутствуют ")


        else:
            print("Число должно быть 1, 2 или 3")  
    else:
        print("Выбор должен быть числом")
               

