class BoxError(Exception): ...
class BoxKeyError(BoxError, KeyError, AttributeError): ...
class BoxTypeError(BoxError, TypeError): ...
class BoxValueError(BoxError, ValueError): ...
class BoxWarning(UserWarning): ...
