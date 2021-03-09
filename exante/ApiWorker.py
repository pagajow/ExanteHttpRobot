import threading
from threading import Thread


class ApiWorker(Thread):
    def __init__(self, function, *args, **kwargs):
        Thread.__init__(self)
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.name = self.function.__name__

    def run(self) -> None:
        print("START: %{0}".format(threading.current_thread().name))
        self.function(*self.args, **self.kwargs)
        print("END: %{0}".format(threading.current_thread().name))
