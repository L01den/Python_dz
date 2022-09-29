def get_storage(data):
    with open('A:/Python/Homeworke/dz_25.09.22/notebook.txt', 'a', encoding="utf-8") as file:
        file.write(f'**{data}**\n')

def get_base():
    with open('A:/Python/Homeworke/dz_25.09.22/notebook.txt', 'r', encoding="utf-8") as file:     
        return file.readlines()

        
def del_data(id, notebook):    
    notebook = [notebook[i] for i in range(len(notebook)) if notebook[i][1] != id]
    '**'.join(notebook)
    with open('A:/Python/Homeworke/dz_25.09.22/notebook.txt', 'w', encoding="utf-8") as file:
        file.write(f'**{notebook}**\n')