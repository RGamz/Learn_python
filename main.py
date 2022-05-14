namespaces = {}

def Create():
    """
    Create <namespace> <parent>
    создать новое пространство имен с именем <namespace> внутри пространства <parent>
    """
    local_namespace = {}
    local_namespace[namespace] = []
    namespaces[arg] = local_namespace

def Add():
    """
    add <namespace> <var>
    добавить в пространство <namespace> переменную <var>
    """
    if namespace in namespaces:
        namespaces[namespace] = arg
    else:
        return "Error"

def Get():
    """
    get <namespace> <var>
    получить имя пространства, из которого будет взята переменная <var>
    при запросе из пространства <namespace>, или None, если такого пространства не существует
    """
    pass

for i in range(int(input())):
    cmd, namespace, arg = input().split()
    if cmd == "create":
        Create()
    elif cmd == "add":
        Add()
    elif cmd == "get":
        Get()


print(namespaces)







