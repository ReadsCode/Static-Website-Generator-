import unittest

from textnode import *


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a link", TextType.LINK, "www.google.com")
        self.assertNotEqual(node, node2)
    
    def test_url(self):
        node = TextNode("This has a url", TextType.LINK, "www.google.com")
        node2 = TextNode("This has a url", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_texttype_noteq(self):
        node = TextNode("This is a test", TextType.BOLD)
        node2 = TextNode("This is a test", TextType.TEXT)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()


class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("b", "bold text"))

    def test_italics(self):
        node = TextNode("italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("i", "italic text"))

    def test_code(self):
        node = TextNode("code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("code", "code text"))

    def test_image(self):
        node = TextNode("image", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("img", "", {"src": node.url, "alt": node.text}))

    def test_link(self):
        node = TextNode("test", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("a", "test", {"href": node.url}))