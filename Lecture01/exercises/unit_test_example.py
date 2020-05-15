class A():
    def __init__(self):
        self.value = "Some Value"

    def return_true(self):
        return True

    def raise_exception(self, val):
        raise KeyError(val)