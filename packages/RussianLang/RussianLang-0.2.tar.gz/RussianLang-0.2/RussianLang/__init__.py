#SlavicPy language library
import sys
import os
import time
import math
import random

class Основа:
    #Ввод вывод данных
    def Писать(self, data=None):
        if data is None:
            return print("")
        else:
            return print(data)

    def Молвить(self, data=None):
        if data is None:
            return input()
        else:
            return input(data)
    
    #Проверка
    def Проверить(self, condition=None, do_first=None, do_second=None):
        if condition is None:
            self.Ошибка("Условие не указано")
        else:
            # если условие не пустое, то делать первое действие, иначе второе
            # Если верно, то возвращать True, иначе False
            if do_first is None and do_second is None:
                if condition:
                    return True
                else:
                    return False
            # тк не пустое условие, делать первое действие, иначе второе
            elif do_second is None:
                if condition:
                    return do_first()  # вызываем функцию
                else:
                    return False
            elif do_first is None:
                if condition:
                    return True
                else:
                    return do_second()  # вызываем функцию
            else:
                if condition:
                    return do_first()  # вызываем функцию
                else:
                    return do_second()  # вызываем функцию
                
    #Математика
    def КвадратныйКорень(self, число):
        if число < 0:
            self.Ошибка("Невозможно вычислить квадратный корень для отрицательного числа")
        else:
            результат = число ** 0.5
            return результат
        
    def Синус(self, угол):
        # угол должен быть в радианах
        результат = 0
        шаг = угол
        знак = -1
        факториал = 1
        степень = 1
        
        # Разложение в ряд Тейлора для синуса
        for i in range(10):
            результат += шаг / факториал
            шаг *= угол * угол
            факториал *= (2*i + 2) * (2*i + 1)
            знак *= -1
        return результат
    
    def Косинус(self, угол):
        # угол должен быть в радианах
        результат = 0
        степень = 1
        факториал = 1
        шаг = 1
        
        # Разложение в ряд Тейлора для косинуса
        for i in range(10):
            результат += шаг / факториал
            шаг *= угол * угол
            факториал *= (2*i + 2) * (2*i + 1)
            степень *= -1
        return результат
    
    def ВозвестиВСтепень(self, основание, степень):
        результат = 1
        for _ in range(степень):
            результат *= основание
        return результат
    
    def Логарифм(self, число, основание=10):
        # Простой логарифм через деление
        результат = 0
        шаг = число - 1  # Отсчет от 1
        while число >= основание:
            число /= основание
            результат += 1
        return результат
    
    def Модуль(self, число):
        if число < 0:
            return -число
        return число
    
    def НайтиКорни(self, a, b, c):
        # Проверка на дискриминант
        дискриминант = b ** 2 - 4 * a * c
        
        if дискриминант > 0:
            # Два корня
            корень1 = (-b + дискриминант ** 0.5) / (2 * a)
            корень2 = (-b - дискриминант ** 0.5) / (2 * a)
            return корень1, корень2
        elif дискриминант == 0:
            # Один корень
            корень = -b / (2 * a)
            return корень,
        else:
            # Нет реальных корней
            return print("Нет реальных корней")
            #self.Ошибка("Нет реальных корней")
            #return None
    

    #Рандом
    def СлучЦел(self, мин, макс):
        return random.randint(мин, макс)

    def СлучДроб(self):
        return random.random()
    
    def СлучВыбор(self, список):
        return random.choice(список)

    #Выход и в будущем ченибудь докину
    def Ошибка(self, data=None):
        if data is None:
            return print("Ошибка")
        else:
            return print(f"Ошибка: {data}")
        
    def Информация(self):
        return print("SlavicPy - библиотека для python на русском языке\nВерсия 0.1\nАвтор: Dron3915\nДата создания: 16.01.2025")

    def Завершить(self):
        sys.exit()



Система = Основа()