FILEPATH = "Todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return a list
    of to-do items.
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file:
        todos_local = file.read().splitlines()
    return todos_local


def write_todos(todos_to_write, filepath=FILEPATH):
    """ Write the to-do items list in the text file """
    todos_to_write = [item + "\n" for item in todos_to_write]
    with open(filepath, 'w') as file:
        file.writelines(todos_to_write)

