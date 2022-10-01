import json

def get_storage(data):
    with open('A:/Python/Homeworke/dz_25.09.22/notebook.txt', 'a', encoding="utf-8") as file:
        file.write(f' {data} \n')

def get_base():
    with open('A:/Python/Homeworke/dz_25.09.22/notebook.txt', 'r', encoding="utf-8") as file:     
        return file.readlines()

def get_read():
    with open('A:/Python/Homeworke/dz_25.09.22/notebook.txt', 'r', encoding="utf-8") as file:     
        while True:
            line = file.readline()
            if not line:
                break
            print(line.strip())

def import_dick(surname, name, phone_number):
    new_dick = {'Surname': surname, 'Name': name, 'Phone': phone_number}
    return new_dick

def data_json(surname, name, phone_number):
    with open('A:/Python/Homeworke/dz_25.09.22/notebook.json', encoding="utf-8") as f:
        data = json.load(f)
        data.append(import_dick(surname, name, phone_number))
        with open('A:/Python/Homeworke/dz_25.09.22/notebook.json', 'w' ,encoding="utf-8") as outf:
            json.dump(data, outf, ensure_ascii=False, indent=2)

def read_json():
    with open('A:/Python/Homeworke/dz_25.09.22/notebook.json', 'r', encoding="utf-8") as f:
        data = json.load(f)
        for i in data:
            print(i)


        
