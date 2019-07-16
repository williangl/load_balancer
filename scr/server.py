"""Server."""


class Server:
    def __init__(self):
        self.task_pool = []
        # self.full = False

    def add_task(self):
        self.task_pool.append(None)

    def is_full(self):
        if len(self.task_pool) >= 2:
            return True
        return False
