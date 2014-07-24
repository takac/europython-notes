Magic Access Attributes
=======================
Petr Viktorin
[@encukou](https://twitter.com/encukou)
[encukou.cz](https://encukou.cz)
[https://ep2014.europython.eu/en/schedule/sessions/123/](https://ep2014.europython.eu/en/schedule/sessions/123/)
[https://www.youtube.com/watch?v=y420yZMRdLw](https://www.youtube.com/watch?v=y420yZMRdLw)

Order an attribute is looked up:
- Check `__dict__`
- Check `__type__`
- Check `__getattr__`
- Raise `AttrError`

Can use `__getattribute__` to overwrite all attribute access.
Also overwrite `__setattr__`

Object also have `__doc__`, methods, subclasses etc.

### [Descriptors](https://docs.python.org/2/howto/descriptor.html)

    class MyDescriptor
    def __get__(...)
    def __set__(...)

    class MyClass()
        my = MyDescriptor()

If has set -> data descriptor
Can use property decorator -> @property

Functions are descriptors.

    class Point:
        def align(self):
            return ..

    >>> p = Point()
    >>> p.align
    bound method
    >>> Point.align
    functon descritpor

## Slots

Help save memory
Removes `__dict__`
Creates a descriptor for the attributes in `__slots__`

0. `__getattribute__`
1. Data descriptor
2. `__dict__`
3. non-data descriptor
4. simple value from class
5. `__getattr__` on class
6. raise `AttrError`

(Don't forget about MRO, [Child, Parent, object])

Data descriptor and non data descriptor in different place

Allows reify (lazy property)
First get will call function, second call will go to the dict value.
