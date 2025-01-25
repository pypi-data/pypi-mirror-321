"""
>>> _| [2, 4, 1] | max | _()-1 | divmod(9, _()) |_
(3, 0)
>>> _ >> [2, 4, 1] >> max >> _()-1 >> divmod(9, _()) >> _
(3, 0)
>>> _ >> [2, 4, 1] >> max >> _._ -1 >> divmod(9, _._) >> _
(3, 0)
>>> __ >> [2, 4, 1] >> max >> __._ - 1 >> divmod(11, __._) >> __._[1] >> __
2
>>> [2, 4, 1] >> __ >> max >> __._ - 1 >> divmod(11, __._) >> __._[1] >> __
2
"""

class Pipe:
    """
    >>> p = Pipe()
    >>> p | 3
    Pipe(3)
    >>> p.value
    3

    >>> import math
    >>> Pipe() | [2, 4, 1] | max | math.sqrt
    Pipe(2.0)
 
    >>> p = Pipe()
    >>> p | [2, 4, 1] | max | (p._-1) | divmod(9, p._)
    Pipe((3, 0))
    """

    @property
    def _(self):
        return self.value

    def __or__(self, next):
        return self.process(next)

    def __rshift__(self, next):
        return self.process(next)

    def __rrshift__(self, next):
        return self.process(next)

    def process(self, next):
        if next == self:
            return self.value
        value = next
        if callable(next):
            value = next(self.value)
        self.value = value
        return self

    def __call__(self):
        return self.value

    def __repr__(self):
        return f'Pipe({repr(self.value)})'
    
_ = __ = Pipe()
