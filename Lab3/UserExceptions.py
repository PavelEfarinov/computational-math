class SameFunctionException(Exception):
    def __init__(self, message="You should pick different functions"):
        super().__init__(message)


class LimitSignException(Exception):
    def __init__(self, message="The signs of function in two border points must differ"):
        super().__init__(message)


class NoRootsException(Exception):
    def __init__(self, message="This method would not converge!\nYou should try some other points"):
        super().__init__(message)
