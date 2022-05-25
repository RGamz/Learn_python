namespaces = {'global': "None"}
variables = {'global': []}

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

def Add(namespace, arg):
    """
    add <namespace> <var>
    добавить в пространство <namespace> переменную <var>
    Примеры:
        add global a
        add foo b
        add bar a
    """
    if namespace in variables.keys():
        pass
    else:
        variables[namespace] = []

    a = variables[namespace]
    a.append(arg)


def get(namespace, arg):

    def check_fun(namespace):
        for key in namespaces.keys():
            if namespace == key:
                return "True"
            else:
                continue


    def check_var(arg):
        for key, value in variables.items():
            for x in value:
                if arg == x:
                    return "True"
                else:
                    continue
            else:
                continue

    def get_var(namespace, arg):
        for key, value in variables.items():
            for x in value:
                if arg == x:
                    if key == namespace:
                        return key
                    else:
                        continue
                else:
                    continue

    if check_var(arg) is None:
        return None
    elif check_fun(namespace) is None:
        return None
    else:
        if get_var(namespace, arg) is None:
            namespace = namespaces[namespace]
            if namespace == "None":
                return "None"
            else:
                return get(namespace, arg)
        else:
            return get_var(namespace, arg)


for i in range(int(input())):
    cmd, namespace, arg = input().split()
    if cmd == "create":
        Create(namespace)
    elif cmd == "add":
        Add(namespace, arg)
    elif cmd == "get":
        print(get(namespace, arg))


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
