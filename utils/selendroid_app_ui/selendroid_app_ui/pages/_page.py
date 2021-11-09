class BasePage:
    def __str__(self):
        return self.__class__.__name__  # TODO: move it to baseclass

    def wait(self, timeout=10):
        raise NotImplemented
