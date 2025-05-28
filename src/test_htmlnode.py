import unittest

from htmlnode import *


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



class TestParentNode(unittest.TestCase):


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_missing_tag(self):
        child_node = LeafNode("b", "bold")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_missing_children(self):
        parent_node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_node_with_props(self):
        child_node = LeafNode("b", "test")
        parent_node = ParentNode("p", [child_node], {"href": "https://www.example.com", "class": "my-link"})
        self.assertEqual(parent_node.to_html(), '<p href="https://www.example.com" class="my-link"><b>test</b></p>')

    def test_children_with_tags(self):
        child_node_1 = LeafNode("b", "test")
        child_node_2 = LeafNode("li", "apples, bananas")
        parent_node = ParentNode("p", [child_node_1, child_node_2])
        self.assertEqual(parent_node.to_html(), "<p><b>test</b><li>apples, bananas</li></p>")

    def test_children_without_tags(self):
        child_node_1 = LeafNode(None, "test")
        child_node_2 = LeafNode(None, "apples, bananas")
        parent_node = ParentNode("p", [child_node_1, child_node_2])
        self.assertEqual(parent_node.to_html(), "<p>testapples, bananas</p>")

    def test_empty_children_list(self):
        parent_node = ParentNode("p", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()



class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hellow, world!")
        self.assertEqual(node.to_html(), "<b>Hellow, world!</b>")

    def test_leaf_to_html_li(self):
        node = LeafNode("li", "banana, apple, strawberry")
        self.assertEqual(node.to_html(), "<li>banana, apple, strawberry</li>")
