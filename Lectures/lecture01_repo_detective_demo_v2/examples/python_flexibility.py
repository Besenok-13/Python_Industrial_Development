def predict(x):
    return x * 2

def everything_is_an_object() -> None:
    objects = [42, "hello", [1, 2, 3], len, list, predict]
    for obj in objects:
        print(f"{obj!r:>24} -> type={type(obj)}, object?={isinstance(obj, object)}")
    print("type(list) =", type(list))
    print("type(type) =", type(type))

class DangerousList(list):
    def __hash__(self):
        return hash(tuple(self))



def dangerous_hash_demo() -> None:

    # делаем имя list локальной переменной всей функции.
    # items = list([1, 2, 3])

    items = [1,2,3]
    try:
        hash(items)
    except TypeError as exc:
        print("normal list:", type(exc).__name__, exc)

    list = DangerousList

    items = [1, 2, 3]
    try:
        hash(items)
    except TypeError as exc:
        print("normal list v2:", type(exc).__name__, exc)


    items = list(items)
    try:
        hash(items)
        print("А теперь это работает. Более того, не посмотрев наверх мы не узнаем что что-то пошло не так")
    except TypeError as exc:
        print("normal list v2:", type(exc).__name__, exc)
    
    key = list([0])
    before = hash(key)
    key.append(3)
    after = hash(key)
    print("DangerousList hash before:", before)
    print("DangerousList hash after: ", after)
    print("hash changed:", before != after)

if __name__ == "__main__":
    everything_is_an_object()
    print("-" * 60)
    dangerous_hash_demo()
