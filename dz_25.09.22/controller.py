import operation as a
import db 
import gui as g

def button_click():
    print( '''Возможные действия со справочником:
        1. Добавить запись
        2. Посмотреть телефон по фамилии''')
    
    notebook_temp = db.get_base()

    match g.action():
        case '1':
            db.get_storage(a.new_data(a.new_id(a.read_base(notebook_temp)), g.get_surname(), g.get_name(), g.get_phone_num()))
        case '2':
            print(a.find(g.get_surname(), a.read_base(notebook_temp)))