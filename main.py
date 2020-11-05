import tkinter as tk
from tkinter import ttk
from tkinter import *
import string
class Arrays:
    def get_array(self, code):
        if code == 0:
            return ()
        elif code == 1:
            return []
        elif code == 2:
            return {}
class TKinter:
    def get_window(self, name, geometry):
        temp = tk.Tk()
        temp.title(name)
        temp.geometry(geometry)
        return temp

    def grid(self, element, x, y):
        return element.grid(row = y, column = x)

    def bind(self, element, key, event):
        element.bind(key, event)

    def get_label(self, master, x, y, text, font = ''):
        temp = ttk.Label(master, text = text, font = font)
        self.grid(temp, x, y)
        return temp

    def config_label(self, line, text):
        line.config(text = text)

    def get_notebook(self, master, x, y, text):
        temp = ttk.Notebook(master)
        self.grid(temp, x, y)
        main_page = ttk.Frame(temp)
        temp.add(main_page, text = text)
        return temp

    def get_entry(self, master, x, y, width):
        temp = ttk.Entry(master, width = width)
        self.grid(temp, x, y)
        return temp

    def get_entry_text(self, element):
        return element.get()

    def clean_entry(self, element):
        element.delete(0, END)

    def get_button(self, master, x, y, text, action):
        temp = ttk.Button(master, text = text, command = action)
        self.grid(temp, x, y)
        return temp

    def get_radiobutton(self, master, x, y, text, var, value):
        temp = ttk.Radiobutton(master, text = text, variable = var, value = value)
        self.grid(temp, x, y)
        return temp

    def set_attributes(self, master, attributes = ()):
        for attribute, value in attributes.items():
            master.wm_attributes(attribute, value)
        return 1

    def set_mainloop(self, master):
        master.mainloop()
        return array

class Splitter:
    def num_pass(self, num):
        out = ''
        for elm in num:
            if elm in string.digits:
                out += elm
        return out
    def num_split(self, num):
        num = num.get()
        num = int(self.num_pass(num))
        out = []
        leight = len(str(num))-1
        for digit in range(len(str(num))):
            out.append(num // 10**leight % 10) # main formula
            leight -= 1
        return out

class Calculator:
    def calculate(self, nums, action):
        out = nums[0]
        for number in nums[1:]:
            if action == 'sum':
                out += number
            elif action == 'sub':
                out -= number
            elif action == 'mult':
                out *= number
            elif action == 'div':
                out /= number
        return out

class Reader:
    def read(self, file):
        with open(file, 'r') as file_read:
            return file_read.read()

class Scripts:

    def screen_init(self):
        windows_array = self.links[0]
        elements_array = self.links[1]
        windows_array['main'] = self.get_window('Калькькулятор арифметических действий', '500x300')

    def greeting_window(self):
        self.author = self.read('sources/text/author.sys')
        self.target = self.read('sources/text/target.sys')
        self.notes = self.read('sources/text/notes.sys')
        windows_array = self.links[0]
        elements_array = self.links[1]
        elements_array['greeting_line'] = self.get_label(windows_array['main'], 0, 0, 'Добро пожаловать!', 'Arial 22')
        elements_array['author'] = self.get_label(windows_array['main'], 0, 1, self.author, 'Segoe 12')
        elements_array['pass1'] = self.get_label(windows_array['main'], 0, 2, '-'*100, 'Segoe 12')
        elements_array['description1'] = self.get_label(windows_array['main'], 0, 3, self.target, 'Segoe 12')
        elements_array['pass2'] = self.get_label(windows_array['main'], 0, 4, '-'*100, 'Segoe 12')
        elements_array['notebook'] = self.get_notebook(windows_array['main'], 0, 5, self.notes)
        elements_array['begin_button'] = self.get_button(windows_array['main'], 0, 10, 'Продолжить', self.main_window)
        self.bind(elements_array['begin_button'], '<Return>', self.main_window)
        elements_array['begin_button'].focus()


    def main_window(self, event=None):
        windows_array = self.links[0]
        elements_array = self.links[1]
        for element in elements_array.values():
            element.destroy()
        windows_array['main'].update()
        elements_array['title'] = self.get_label(windows_array['main'], 0, 0, 'Калькулятор арифм. действий', 'Arial 16')
        elements_array['line'] = self.get_entry(windows_array['main'], 0, 1, 50)
        self.bind(elements_array['line'], '<Return>', self.main_counter)
        elements_array['line'].focus()
        elements_array['out'] = self.get_label(windows_array['main'], 0, 2, '', 'Times 16')
        self.radio_array['radiovar1'] = StringVar()
        self.radio_array['radiovar1'].set('sum')
        elements_array['radiobutton1'] = self.get_radiobutton(windows_array['main'], 1, 3, 'Сложение', self.radio_array['radiovar1'], 'sum')
        elements_array['radiobutton2'] = self.get_radiobutton(windows_array['main'], 2, 3, 'Вычитание', self.radio_array['radiovar1'], 'sub')
        elements_array['radiobutton3'] = self.get_radiobutton(windows_array['main'], 1, 4, 'Умножение', self.radio_array['radiovar1'], 'mult')
        elements_array['radiobutton4'] = self.get_radiobutton(windows_array['main'], 2, 4, 'Деление', self.radio_array['radiovar1'], 'div')
        elements_array['button'] = self.get_button(windows_array['main'], 2, 1, 'Считать', self.main_counter)

    def main_counter(self, event=None):
        try:
            out = self.num_split(self.names_dict['line'])
            out = self.calculate(out,self.radio_array['radiovar1'].get())
        except:
            out = 'Ошибка ввода!'
        self.names_dict['out'].config(text = 'Результат: ' + str(out))
        self.clean_entry(self.names_dict['line'])


class Main(TKinter, Arrays, Splitter, Calculator, Scripts, Reader):

    def __init__(self):
        self.links = self.get_array(1)
        self.windows = self.get_array(2)
        self.names_dict = self.get_array(2)
        self.radio_array = self.get_array(2)

        self.links.append(self.windows)
        self.links.append(self.names_dict)

        self.screen_init()
        self.greeting_window()

        self.set_attributes(self.windows['main'], {'-topmost': True})
        self.set_mainloop(self.windows['main'])




if __name__ == '__main__':
    main = Main()