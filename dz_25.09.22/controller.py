import operation as o
import db 
import gui as g

def button_click():
    o.hello()
    click = g.action()
    while click != 0:
        notebook_temp = db.get_base()
        match click:
            case 1:
                surname = g.get_surname()
                name = g.get_name()
                phone = g.get_phone_num()
                db.get_storage(o.new_data(surname, name, phone))
                db.data_json(surname, name, phone)
            case 2:
                temp = o.find(g.get_surname(), notebook_temp)
                print(temp[5:-5])
            case 3:
                db.get_read()
            case 4:
                db.read_json()
        
        o.hello()  
        click = g.action()



                