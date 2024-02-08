# Комплексный калькулятор
# Проверен на Python 3.6
# Также работает с онлайн-интерпретатором
#  www.online-python.com  или  http://pythonide.online
# SOLID-принципы:
#   Single Responsibility Principle (SRP);
#   Dependency Inversion Principle (DIP).
#----------------------------------------------
import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] [%(levelname)s] [%(module)s] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def get_logger(name):
    return logging.getLogger(name)

#----------------------------------------------

from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def operate(self, num1, num2):
        pass

    @abstractmethod
    def __str__(self):
        pass

#----------------------------------------------
class ComplexAdd(Operation):
    def operate(self, num1, num2):
        real_sum = num1.real + num2.real
        imag_sum = num1.imag + num2.imag
        return complex(real_sum, imag_sum)

    def __str__(self):
        return "Addition"

#----------------------------------------------
class ComplexSub(Operation):
    def operate(self, num1, num2):
        real_sum = num1.real - num2.real
        imag_sum = num1.imag - num2.imag
        return complex(real_sum, imag_sum)

    def __str__(self):
        return "Substraction"

#----------------------------------------------
class ComplexMul(Operation):
    def operate(self, num1, num2):
        real_mul = num1.real * num2.real - num1.imag * num2.imag
        imag_mul = num1.real * num2.imag + num1.imag * num2.real
        return complex(real_mul, imag_mul)

    def __str__(self):
        return "Multiplication"

#----------------------------------------------
class ComplexDiv(Operation):
    def operate(self, num1, num2):
        try:
            denominator = num2.real ** 2 + num2.imag ** 2
            real_div = (num1.real * num2.real + num1.imag * num2.imag) / denominator
            imag_div = (num1.imag * num2.real - num1.real * num2.imag) / denominator
            return complex(real_div, imag_div)
        except ZeroDivisionError:
            return None

    def __str__(self):
        return "Division"

#----------------------------------------------
class ComplexCalculator:
    def __init__(self, operation):
        self.operation = operation

    def calculate(self, num1, num2):
        return self.operation.operate(num1, num2)

    def __str__(self):
        return str(self.operation)

#----------------------------------------------

def input_complex_number():
    real = float(input("Введите Re = "))
    imag = float(input("Введите Im = "))
    return complex(real, imag)

def input_operation():
    op = input("Введите знак операции +, -, *, / : ")
    return op

#----------------------------------------------

def main():
    setup_logger()
    logger = get_logger("complex_calculator")
    logger.info("Калькулятор комплексных чисел запущен.")
    logger.info("Введите 1-е компл.число:")
    num1 = input_complex_number()
    logger.info("Введите 2-е компл.число:")
    num2 = input_complex_number()
    logger.info("Введите знак операции:")
    op = input_operation()
    if op == '+':
        operation = ComplexAdd()
    elif op == '-':
        operation = ComplexSub()
    elif op == '*':
        operation = ComplexMul()
    elif op == '/':
        operation = ComplexDiv()
    else:
        logger.info("Неверный знак операции!")
        exit(-1)
    
    calculator = ComplexCalculator(operation)
    result = calculator.calculate(num1, num2)
    logger.info(f"Результат {calculator}: {result}")

#----------------------------------------------
    
if __name__ == "__main__":
    main()
