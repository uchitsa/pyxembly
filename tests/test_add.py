import unittest
from unittest import TestCase
from lxml import etree

from add import Add


class TestAdd(TestCase):
    def test_exec(self):
        self.fail()

    def test_add(self):
        dom = etree.fromstring('<books/>')
        new_node = etree.Element('book')
        dom.append(new_node)
        add = Add.__init__(self, name='book')
        add.exec(dom, [dom.xpath('/*').first])
        self.assertEqual(etree.tostring(dom), b'<books><book></books>')

    class TestStringMethods(unittest.TestCase):

        def test_upper(self):
            self.assertEqual('foo'.upper(), 'FOO')

        def test_isupper(self):
            self.assertTrue('FOO'.isupper())
            self.assertFalse('Foo'.isupper())

    if __name__ == '__main__':
        unittest.main()
