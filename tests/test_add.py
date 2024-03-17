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
        Add.__init__('book').exec(dom, [dom.xpath('/*').first])
        self.assertEqual(etree.tostring(dom), b'<books><book></books>')


if __name__ == '__main__':
    unittest.main()
