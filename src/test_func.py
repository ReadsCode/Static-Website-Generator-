import unittest

from func import *

from textnode import *

class FuncTest(unittest.TestCase):


    def test_code_text(self):
        old_node_list = [TextNode("code", TextType.CODE), TextNode("This `is` text ", TextType.TEXT), TextNode(" this is more text", TextType.TEXT)]
        delimiter = "`"
        text_type = TextType.CODE
        self.assertEqual(split_nodes_delimiter(old_node_list, delimiter, text_type), [TextNode("code", TextType.CODE), TextNode("This ", TextType.TEXT), TextNode("is", TextType.CODE), TextNode(" text ", TextType.TEXT), TextNode(" this is more text", TextType.TEXT)])


    def test_bold_text(self):
        old_node = [TextNode("This is **bold** text", TextType.TEXT)]
        delimiter = "**"
        text_type = TextType.BOLD
        self.assertEqual(split_nodes_delimiter(old_node, delimiter, text_type), [TextNode("This is ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" text", TextType.TEXT)])


    def test_italic_text(self):
        old_node = [TextNode("This is _italic_ text", TextType.TEXT)]
        delimiter = "_"
        text_type = TextType.ITALIC
        self.assertEqual(split_nodes_delimiter(old_node, delimiter, text_type), [TextNode("This is ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" text", TextType.TEXT)])




    def test_image_and_text_extract_image(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])


    def test_image_and_text_extract_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev")])


    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


    def test_extract_markdown_images_only_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        self.assertNotEqual(extract_markdown_images(text), [("to boot dev", "https://www.boot.dev")])

    
    def test_extract_markdown_links_only_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        self.assertNotEqual(extract_markdown_links(text), [("image", "https://i.imgur.com/zjjcJKZ.png")])