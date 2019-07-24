"""Test load balance."""
from unittest import TestCase

from scr.load_balancer import LoadBalancer
from scr.server import Server


class TestCase(TestCase):
    def setUp(self):
        self.load_balancer = LoadBalancer()
        self.server = Server()

    def tearDown(self):
        ...

    def test_load_balancer_should__include_one_server_on_pool(self):
        self.load_balancer.add_user(1)

        self.assertEqual(1, len(self.load_balancer.pool))

    def test_load_balancer_should_include_server_object_on_pool(self):
        self.load_balancer.add_user(1)
        expected = Server
        self.assertIsInstance(self.load_balancer.pool[0], expected)

    def test_load_balancer_should__include_two_users_on_load_balancer_and_just_one_server_in_pool(self):
        self.load_balancer.add_user(1)
        self.load_balancer.add_user(1)

        self.assertEqual(1, len(self.load_balancer.pool))

    def test_load_balancer_should_include_three_users_on_load_balancer_and_two_servers_in_pool(self):
        self.load_balancer.add_user(1)
        self.load_balancer.add_user(1)
        self.load_balancer.add_user(1)

        self.assertEqual(2, len(self.load_balancer.pool))

    def test_load_balancer_shoud_include_ten_user_and_five_servers_in_pool(self):
        values_ = [
            (1, 1), (1, 1), (1, 2), (1, 2), (1, 3),
            (1, 3), (1, 4), (1, 4), (1, 5), (1, 5)
            ]

        for usr, svr in values_:
            with self.subTest(users=usr, servers=svr):
                self.load_balancer.add_user(usr)

                self.assertEqual(svr, len(self.load_balancer.pool))

    def test_load_balancer_shoud_inclue_more_than_one_user_at_once_and_create_the_equivalent_servers(self):
        self.load_balancer.add_user(5)

        self.assertEqual(3, len(self.load_balancer.pool))
