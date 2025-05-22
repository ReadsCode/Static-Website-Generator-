import unittest

from textnode import TextNode, TextType


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
