"""
ᲡᲐᲑᲐᲖᲝ ᲡᲘᲜᲢᲐᲥᲡᲘ
"""
import typing


# ᲫᲘᲠᲘᲗᲐᲓᲘ ᲢᲘᲞᲔᲑᲘ ᲓᲐ ᲡᲢᲠᲣᲥᲢᲣᲠᲔᲑᲘ
types = [
    ...,
    None,
    True, False, bool,
    1, int,
    1.1, float,
    ' ', " ", """ """, f'', r'', str,
    b'', bytes,
    [], list,
    (), tuple,
    {1, }, set,
    {}, dict
]


# ᲫᲘᲠᲘᲗᲐᲓᲘ ᲝᲞᲔᲠᲐᲢᲝᲠᲔᲑᲘ
_ = 1 + 2
_ = 1 - 2
_ = 1 * 2
_ = 1 ** 2
_ = 1 / 2
_ = 1 // 2
_ = 1 % 2
_ = 1 and 2
_ = 1 or 2
_ = 1 > 2 | 1 >= 2 | 1 < 2 | 1 <= 2


# ᲪᲘᲙᲚᲘ for
for _ in types:
    pass

for _ in types:
    break
else:
    pass


# Comprehensions კომპაქტური ფორმები - კომპრეჰენზია
a = [i for i in types]
b = (i for i in types)
c = {i for i in types if isinstance(i, typing.Hashable)}
d = {str(i): i for i in types}


# მინიჭება, გამოშლა, კვეთები  
e, *f, g = types
h = [*f]
_ = [1, 2, 3][:]
_ = {**{}}


# განაცხადი assert
assert h, 'test'


# ციკლი while
while a:
    a.pop()

while a:
    break
else:
    pass


# ფუნქციები
def func(text: str, space: str, action: typing.Callable) -> None:
    if not text:
        return

    print(space + action(text))
    func(text[1:], space + ' ', action)
    print(space + action(text))


# lambda ფუნქციები
func('*' * 11, '', lambda text: ' '.join(i for i in text))


# დეკორატორები
def decorator(multiplier: int):

    def dec(func: typing.Callable):
        # Области видимости функции
        global a, b, c, d
        nonlocal multiplier

        if multiplier % 2 == 0:
            multiplier += 1

        def wrap(*args, **kwargs):
            for _ in range(multiplier):

                # Генераторы
                yield func(*args, **kwargs)

        return wrap

    return dec


@decorator(10)
def f(num: int) -> int:
    return num


qwe = [*f(1)]


# პირობები
if i := d.get(''):
    pass
elif not (q := d.get(1)):
    pass
else:
    ...


# match qwe:
#     case "1":
#         pass
#     case _:
#         pass


# გამონაკლისები და მისი დამუშავება
try:
    1 / 0
except ZeroDivisionError as exc:
    pass
else:
    pass
finally:
    ...


# კლასები
class A:

    class_attrs = None

    def __init__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        self.__test_arg = None

    def main(self) -> None:
        ...

    @property
    def test_arg(self) -> typing.Any:
        return self.__test_arg

    @test_arg.setter
    def test_arg(self, value: typing.Any):
        self.__test_arg = value


class B(A):

    def main(self) -> None:
        super().main()
        print(self.test_arg)

    @classmethod
    def create(cls, *args, **kwargs) -> 'B':
        return cls(*args, **kwargs)

    @staticmethod
    def get_test() -> str:
        return 'test'
