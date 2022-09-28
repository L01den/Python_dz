import hb_functions as f
import handbook_base as hb
import gui as g

def button_click():
    print( '''Возможные действия со справочником:
        1. Добавить запись
        2. Посмотреть телефон по фамилии''')
    
    notebook_temp = hb.get_base()

    match g.action():
        case '1':
            hb.get_storage(f.new_data(f.new_id(f.read_base(notebook_temp)), g.get_surname(), g.get_name(), g.get_phone_num()))
        case '2':
            print(f.find(g.get_surname(), f.read_base(notebook_temp)))