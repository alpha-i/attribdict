class AttribDict(dict):
    """A dictionary with attribute-style access. It maps attribute access to
    the real dictionary.  """
    def __init__(self, init={}):
        dict.__init__(self, init)

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, items):
        for key, val in items:
            self.__dict__[key] = val

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, dict.__repr__(self))

    def __setitem__(self, key, value):
        return super().__setitem__(key, value)

    def __getitem__(self, name):
        try:
            return super().__getitem__(name)
        except KeyError:
            return None

    def __delitem__(self, name):
        return super().__delitem__(name)

    def __hash__(self):
        return hash(repr(dict(self)))

    __getattr__ = __getitem__
    __setattr__ = __setitem__
