import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):

    def test_to_html(self):
        props_dict = {
    "href": "https://www.google.com",
    "target": "_blank",
    }
        node = HTMLNode(tag="p", value="text", children=None, props=props_dict)
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')

    def test_props_none(self):
        node = HTMLNode(tag="p", value="text", children=None, props=None)
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_empty_dict(self):
         node = HTMLNode(tag="p", value="text", children=None, props={})
         result = node.props_to_html()
         self.assertEqual(result, "")

