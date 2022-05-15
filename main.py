namespaces = {'global': None}
variables = {}

def Create(x):
    """
    Create <namespace> <parent>
    создать новое пространство имен с именем <namespace> внутри пространства <parent>
    Примеры:
        create foo global
        create bar foo
    """
    if cmd in namespaces:
        pass
    else:
        namespaces[namespace] = arg

def Add(x):
    """
    add <namespace> <var>
    добавить в пространство <namespace> переменную <var>
    Примеры:
        add global a
        add foo b
        add bar a
    """
    variables[namespace] = []
    a = variables[namespace]
    a.append(arg)


def Get(x):
    """
    get <namespace> <var>
    получить имя пространства, из которого будет взята переменная <var>
    при запросе из пространства <namespace>, или None, если такого пространства не существует
    Примеры:
        get foo a
        get foo с
        get bar a
        get bar b
    """
    for key, value in namespaces.items():
        if value == arg:
            print("ok")
        else:
            return None

for i in range(int(input())):
    cmd, namespace, arg = input().split()
    if cmd == "create":
        Create(cmd)
    elif cmd == "add":
        Add(cmd)
    elif cmd == "get":
        Get(cmd)


print(namespaces)
print(variables)

"""

9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b

"""



