import datetime

class Item:

    def __init__(self, name, content , dateCreation):
        self.name : str = name
        self.content : str = content
        self.date : datetime = dateCreation


class TodoList:

    def __init__(self):
        self.tasks : list[Item,...] = []
        self.maxTask = 10

    def addTask(self, newItem : Item) -> bool:

        if len(self.tasks) < self.maxTask:
            self.tasks.append(newItem)
            return True

        print("Vous avez atteint le nombre maximum de tâches")
        return False

    def save(self) -> NotImplementedError:
        raise NotImplementedError("Pas implémenté")




