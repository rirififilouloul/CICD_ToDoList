import datetime
import requests

class Item:

    def __init__(self, name, content , dateCreation):
        self.name : str = name
        self.content : str = content
        self.date : datetime = dateCreation


class TodoList:


    def __init__(self):
        self.tasks : list[Item,...] = []
        self.maxTask = 10
        self.endpointApi = "https://dummyjson.com/todos"

    def addTask(self, newItem : Item) -> bool:

        if len(self.tasks) < self.maxTask:
            self.tasks.append(newItem)
            return True

        print("Vous avez atteint le nombre maximum de tâches")
        return False

    def save(self) -> NotImplementedError:
        raise NotImplementedError("Pas implémenté")


    def loadFromApi(self):

        response = requests.get(self.endpointApi + "?limit=10")
        data = response.json()
        if response.status_code != 200:

            return False

        allTodos = data['todos']
        for todo in allTodos:

            newItem : Item = Item(f"task : {todo['id']}", todo['todo'], datetime.datetime.now())
            self.addTask(newItem)

        return True

    def __print__(self):
        for task in self.tasks:
            print(task.name + " : " + task.content)

