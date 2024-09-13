

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()

'''
inner_function() 

Вызов данной функции вне функции test_function приводит к ошибке:
NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
имя 'inner_function' не определено, т.к. она находится только в пределах видимости функции test_function
т.е. локально и не может быть выполнена в глобальном пространстве.
'''