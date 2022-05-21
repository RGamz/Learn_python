namespaces = {'global': None}
variables = {'global': []}

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
                return value
            else:
                pass

    if variables_func(namespace, arg) is None:
        if namespaces_func(namespace) is None:
            print("None_nam")
        else:
            return namespaces_func(namespace)
    else:
        return variables_func(namespace, arg)


r = int(input()) - 1

for i in range(r):
    cmd, namespace, arg = input().split()
    if cmd == "create":
        Create(cmd)
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
#
# namespaces = {'global': None, 'foo': 'global', 'bar': 'foo'}
# variables = {'global': ['a'], 'foo': ['b'], 'bar': ['a']}
#
# def Get(arg):
#     for key1, value1 in variables.items():
#         for x in value1:
#             if arg == x:
#                 return key1
#             else:
#                 for key2, value2 in namespaces.items():
#                     for y in value2:
#                         if arg == y:
#                             return key2
#                         else:
#                             print("Error")
#
# arg = input()
#
# print(Get(arg))