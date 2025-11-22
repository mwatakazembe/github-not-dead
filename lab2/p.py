#создать структуру в которой будет храниться, фамилия, балл по математике, по физике, по языку,специальность, статус пост или нет. должна быть возможносьт добавить, удалить студента, поменять балл, статус. и вывод в файл

students = {}

def add_stu():
    s_name = input("input secondname: ")
    m_mark = input("input mathematics mark: ")
    ph_mark = input("input physics mark: ")
    l_mark = input("input language mark: ")
    spec = input("input specialty: ")
    status = input("input status: ")
    student_char = {s_name: {"mathmark": m_mark, "physmark": ph_mark, "langmark": l_mark, "spec": spec, "status": status}}
    students.update(student_char)
    print("student added")
    return students
    
while True:
    choice = input("input:\n 1. add student\n 2. delete student\n 3. change mathematics mark\n 4. change physics mark\n 5. change language mark\n 6. change status\n 7. create file\n")
    if(choice == "1"):
        add_stu()
    elif(choice == "2"):
        i = input("input secondname")
        del(students[i])
    elif(choice == "3"):  
        i = input("input secondname")
        students[i]["mathmark"] = input("input new mathematics mark")    
    elif(choice == "4"):  
        i = input("input secondname")
        students[i]["physmark"] = input("input new physics mark")
    elif(choice == "5"):  
        i = input("input secondname")
        students[i]["langmark"] = input("input new language mark")
    elif(choice == "6"):  
        i = input("input secondname")
        students[i]["status"] = input("input new status")  
    elif(choice == "7"):
         with open("students.txt", 'w') as f:
            f.write(str(students))              
