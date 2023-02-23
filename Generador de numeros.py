"""
Horacio Lopez 
Carne: 1290-21-3372
Clase: Programacion III
Fecha: 23/02/2023
Tarea 1 : Generador de Números (optimizar código)
"""

import random

class RandomNumbersGenerator:

    def __init__(self, min_value, max_value, num_values, output_filename):
        self.min_value = min_value
        self.max_value = max_value
        self.num_values = num_values
        self.output_filename = output_filename

    def generate(self):
        with open(self.output_filename, 'w') as f:
            for i in range(self.num_values):
                f.write(str(random.randint(self.min_value, self.max_value)) + '\n')

class ShellSort:

    def sort(self, arr):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

class NumbersSorter:

    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename

    def sort(self):
        with open(self.input_filename, 'r') as f_in, open(self.output_filename, 'w') as f_out:
            numbers = [int(line) for line in f_in]
            shell_sort = ShellSort()
            shell_sort.sort(numbers)
            for number in numbers:
                f_out.write(str(number) + '\n')

class Program:

    def run(self):
        while True:
            print('-----------Bienvenido--------------')
            print('1. Generar números aleatorios')
            print('2. Ordenar números')
            print('3. Salir')
            print('-----------------------------------')
            option = input('Ingrese una opción: ')

            if option == '1':
                num_values = 1000000
                output_filename = 'Numeros.txt'
                generator = RandomNumbersGenerator(-10000000, 10000000, num_values, output_filename)
                generator.generate()
                print(f'Se generaron {num_values} números aleatorios y se guardaron en el archivo "{output_filename}"')

            elif option == '2':
                input_filename = input('Ingrese el nombre del archivo con los números a ordenar: ')
                output_filename = input('Ingrese el nombre del archivo para guardar los números ordenados: ')
                sorter = NumbersSorter(input_filename, output_filename)
                sorter.sort()
                print(f'Se ordenaron los números del archivo "{input_filename}" y se guardaron en el archivo "{output_filename}"')

            elif option == '3':
                break

            else:
                print('Opción inválida')

if __name__ == '__main__':
    program = Program()
    program.run()