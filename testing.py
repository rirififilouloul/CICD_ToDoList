import pytest

from UserClass import User
from EmailClass import Email

def initValidUser() -> User:
    return User("Jean", "Dupont", "jean@dupont.com", "JeanDupont123", "15/12/2000")

def initInvalidUser() -> User:
    return User("Jean", "Dupont", "jean@dupont.com,", "jeandupont123", "15/12/2000")

#######################################################

def test_User_isValid():
    user = initValidUser()
    assert user.isValid() == True

def test_User_PwdNotValid():
    user = initValidUser()
    user.password = "123"
    assert user.isValid() == False

def test_User_AgeNotValid():
    user = initValidUser()
    user.date_naissance = "15/12/2020"
    assert user.isValid() == False

def test_User_EmailNotValid():
    user = initValidUser()
    user.email = "jean@dupont"
    assert user.isValid() == False

#######################################################

def test_createTodoList():
    user = initValidUser()
    assert user.createTodoList() == True

def test_createTodoListNotValid():
    user = initInvalidUser()
    assert user.createTodoList() == False


#######################################################

def test_createTask():
    user = initValidUser()
    user.createTodoList()
    assert user.addTaskInTodoList("Test", "Test") == True

def test_createTaskWithoutTodoList():
    user = initValidUser()
    assert user.addTaskInTodoList("Test", "Test") == False

def test_createTaskWithoutName():
    user = initValidUser()
    user.createTodoList()
    assert user.addTaskInTodoList("", "Test") == False

def test_createTaskWithoutContent():
    user = initValidUser()
    user.createTodoList()
    assert user.addTaskInTodoList("Test", "") == False

def test_createTaskWithOverflow():
    user = initValidUser()
    user.createTodoList()
    assert user.addTaskInTodoList("Test", "Test"*999) == False

def test_createTaskWithTaskExist():
    user = initValidUser()
    user.createTodoList()
    user.addTaskInTodoList("Test", "Test")
    assert user.checkIfTaskExist("Test") == True

def test_createTaskWithTaskNotExist():
    user = initValidUser()
    user.createTodoList()
    user.addTaskInTodoList("Test", "Test")
    assert user.checkIfTaskExist("Test2") == False

#######################################################


def test_addMaxNumTaskInTodoList(mocker):
    user = initValidUser()
    user.createTodoList()
    user.period = 0

    mocker.patch('EmailClass.Email.send', return_value=True)

    for i in range(10):
        user.addTaskInTodoList("Test" + str(i), "Test" + str(i))

    assert user.addTaskInTodoList("Test", "Test") == False
    assert len(user.todoList.tasks) == 10

def test_EmailSend(mocker):
    user = initValidUser()
    user.createTodoList()
    user.period = 0

    mocker.patch('EmailClass.Email.send', return_value=True)

    for i in range(8):
        user.addTaskInTodoList("Test" + str(i), "Test" + str(i))

    assert len(user.todoList.tasks) == 8

def test_SaveTodoList(mocker):
    user = initValidUser()
    user.createTodoList()
    user.period = 0

    mocker.patch('ToDoListClass.TodoList.save', return_value=True)

    for i in range(2):
        user.addTaskInTodoList("Test" + str(i), "Test" + str(i))

    assert user.todoList.save() == True

def test_SaveTodoListAndEmail(mocker):
    user = initValidUser()
    user.createTodoList()
    user.period = 0

    mocker.patch('ToDoListClass.TodoList.save', return_value=True)
    mocker.patch('EmailClass.Email.send', return_value=True)

    for i in range(10):
        user.addTaskInTodoList("Test" + str(i), "Test" + str(i))

    assert user.todoList.save() == True

def test_SaveTodoListAndEmailNotValid(mocker):
    user = initValidUser()
    user.createTodoList()
    user.period = 0

    mocker.patch('ToDoListClass.TodoList.save', return_value=False)
    mocker.patch('EmailClass.Email.send', return_value=False)

    for i in range(10):
        user.addTaskInTodoList("Test" + str(i), "Test" + str(i))

    assert user.todoList.save() == False

