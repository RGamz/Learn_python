namespaces = {'global': None}
variables = {'global': []}
temp_namespace = []

def Create(namespace):
    """
    Create <namespace> <parent>
    создать новое пространство имен с именем <namespace> внутри пространства <parent>
    Примеры:
        create foo global
        create bar foo
    """
    if namespace in namespaces:
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


def Get(namespace, arg):
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

    def variables_func(namespace, arg):
        for key, value in variables.items():
            for x in value:
                if arg == x:
                    if key == namespace:
                        return key
                    else:
                        continue
                else:
                    continue

    def namespaces_func(namespace):
        for key, value in namespaces.items():
            if namespace == key:
                temp_namespace.clear()
                temp_namespace.append(value)
                return value
            else:
                pass

    if variables_func(namespace, arg) is None:
        if namespaces_func(namespace) is None:
            print("None")
            exit()
        else:
            for key, value in variables.items():
                if temp_namespace[0] == key:
                    if arg == value[0]:
                        return key
    else:
        return variables_func(namespace, arg)


for i in range(int(input())):
    cmd, namespace, arg = input().split()
    if cmd == "create":
        Create(namespace)
    elif cmd == "add":
        Add(cmd)
    elif cmd == "get":
        print(Get(namespace, arg))


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
