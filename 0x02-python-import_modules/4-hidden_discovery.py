#!/usr/bin/python3
import imp
my_module = imp.load_compiled("my_module", "/home/one/Documents/Disk Education/Python/alx-higher_level_programming/0x02-python-import_modules/hidden_4.pyc")

if __name__ == '__main__':
    #my_module.main()
    #print(len(my_module))
    '''
    for i in range(len(my_module)):
        if my_module[i][:2] != '__':
            print(my_module[i])
            '''