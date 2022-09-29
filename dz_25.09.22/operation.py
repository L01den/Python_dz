def new_data(id, surname, name, phone_number):
    new_str = [id, surname, name, phone_number]    
    return '**'.join(new_str)

def new_id(notebook):
    id_temp = [notebook[i][1] for i in range(len(notebook))]
    id_list = tuple(map(int, id_temp))
    return str(max(id_list) + 1)

def read_base(notebook):
    notebook = [notebook[i][:-1] for i in range(len(notebook))]
    notebook = [notebook[i].split('**') for i in range(len(notebook))]
    # handbook = [handbook[i].remove('') for i in range(len(handbook))]
    return notebook

def find(surname, notebook):
    surname_list = [notebook[i] for i in range(len(notebook)) if notebook[i][2] == surname]
    return surname_list