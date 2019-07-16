"""Test load balance."""
from unittest import TestCase

from scr.load_balancer import LoadBalancer
from scr.server import Server

class TestCase(TestCase):
    def setUp(self):
        self.load_balancer = LoadBalancer()

    def tearDown(self):
        ...

    def test_load_balancer_should__include_one_server_on_pool(self):
        self.load_balancer.add_user(1)
        expected = 1
        self.assertEqual(expected, len(self.load_balancer.pool))

    def test_load_balancer_should_include_server_object_on_pool(self):
        self.load_balancer.add_user(1)
        expected = Server
        self.assertIsInstance(self.load_balancer.pool[0], expected)

    def test_load_balancer_should__include_two_users_on_load_balancer_and_just_one_server_in_pool(self):
        self.load_balancer.add_user(1)
        self.load_balancer.add_user(1)

        expected = 1
        self.assertEqual(expected, len(self.load_balancer.pool))

    def test_load_balancer_should__include_three_users_on_load_balancer_and_two_servers_in_pool(self):
        self.load_balancer.add_user(1)
        self.load_balancer.add_user(1)
        self.load_balancer.add_user(1)

        expected = 2
        self.assertEqual(expected, len(self.load_balancer.pool))
