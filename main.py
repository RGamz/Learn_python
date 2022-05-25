namespaces = {'global': None}
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


def get(namespace, arg):

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
    else:
        if get_var(namespace, arg) is None:
            namespace = namespaces[namespace]
            return get(namespace, arg)
        else:
            return get_var(namespace, arg)


for i in range(int(input())):
    cmd, namespace, arg = input().split()
    if cmd == "create":
        Create(namespace)
    elif cmd == "add":
        Add(cmd)
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
