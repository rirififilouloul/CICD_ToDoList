import ToDoListClass as tdl
from EmailClass import Email
import re
import datetime

class User:

    def __init__(self, firstname : str, lastname : str, email : str,password : str , date_naissance : datetime):
        self.firstname : str = firstname
        self.lastname : str = lastname
        self.email : str = email
        self.password : str = password
        self.date_naissance : datetime = date_naissance
        self.todoList : tdl.TodoList = None
        self.lastItemAddDate : datetime = datetime.datetime(1970, 1, 1)
        self.period = 1800

    def isValid(self) -> bool:

        if self.firstname == "" or not self.firstname.isalpha():
            return False

        if self.lastname == "" or not self.lastname.isalpha():
            return False

        if (not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.email)):
            return False

        try:
            date_naissance = datetime.datetime.strptime(self.date_naissance, '%d/%m/%Y')
            date_actuelle = datetime.datetime.now()

            if (date_actuelle.year - date_naissance.year < 13):
                return False

            if (date_actuelle.year + 1 < date_naissance.year):
                return False

        except ValueError:
            print("Le format correct est JJ/MM/AAAA")

            return False


        if not (len(self.password) >= 8  and len(self.password) <= 40):

            return False

        if not re.search("[a-z]", self.password):
            return False

        if not re.search("[A-Z]", self.password):
            return False

        if not re.search("[0-9]", self.password):
            return False

        return True

    def createTodoList(self) -> bool:

        if self.isValid():
            self.todoList = tdl.TodoList()
            return True
        else:
            print("Vous n'avez pas de compte utilisateur valide")
            return False

    def checkIfTaskExist(self, name) -> bool:

        if self.todoList == None:
            print("Vous n'avez pas de liste de tâches")
            return False

        for task in self.todoList.tasks:
            if task != None and task.name == name:
                return True

        return False


    def addTaskInTodoList(self, name, content) -> bool:

        if self.todoList == None:
            print("Vous n'avez pas de liste de tâches")
            return False

        if(name == "" or content == ""):
            print("Vous devez renseigner un nom et un contenu pour la tâche")
            return False

        if(len(content) > 1000):
            print("Le contenu de la tâche ne doit pas dépasser 1000 caractères")
            return False

        if(self.checkIfTaskExist(name)):
            print("Une tâche avec ce nom existe déjà")
            return False

        if (datetime.datetime.now() - self.lastItemAddDate).seconds >= self.period:

            self.lastItemAddDate = datetime.datetime.now()
            newItem: Item = tdl.Item(name, content, self.lastItemAddDate)

            if self.todoList.addTask(newItem):


                if len(self.todoList.tasks)==8:

                    newEmail : Email =  Email()
                    newEmail.send(self.email, "Vous avez bientôt atteint le nombre maximum de tâches")

                return True

            else:

                return False
        else:

            print(f"Vous ne pouvez pas ajouter de tâche pour le moment . Veuillez attendre : {(datetime.datetime.now() - self.lastItemAddDate).seconds} secondes")
            return False





