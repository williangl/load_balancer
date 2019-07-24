"""Load balancer."""

from scr.server import Server


class LoadBalancer:
    """Class Load Balancer."""

    def __init__(self):
        """Atribute definition."""
        self.pool = []

    def add_user(self, user):
        for usr in range(user):
            if not self.pool:
                self.pool.append(Server())

            elif self.pool[-1].is_full:
                self.pool.append(Server())

            self.pool[-1].add_task()
