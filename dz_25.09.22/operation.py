def new_data(surname, name, phone_number):
    new_str = [surname, name, phone_number]    
    return ' '.join(new_str)

def find(surname, notebook):
    surname_list = [notebook[i] for i in range(len(notebook)) if surname in notebook[i]]
    return str(surname_list) 

def hello():
    print( '''Возможные действия со справочником:
            1. Добавить запись
            2. Посмотреть телефон по фамилии
            3. Посомтреть все записи справочника в TXT
            4. Посомтреть все записи справочника в JSON
            0. Выход''')

def import_dick(surname, name, phone_number):
    new_str = (name, phone_number)
    new_dick = {surname: new_str}
    return new_dick


