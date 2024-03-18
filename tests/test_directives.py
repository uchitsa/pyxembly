from unittest import TestCase


class TestDirectives(TestCase):
    def test_parse_text(self):
        self.fail()

    def test_map(self):
        self.fail("ADD 'orders'; ADD 'order'; ATTR 'id', '553'; SET '$140.00';")
