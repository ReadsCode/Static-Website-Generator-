from enum import Enum

from htmlnode import *

class TextType(Enum):

    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    

class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.TEXT:
                html_node = LeafNode(None, text_node.text)
            case TextType.BOLD:
                html_node = LeafNode("b", text_node.text)
            case TextType.ITALIC:
                html_node = LeafNode("i", text_node.text)
            case TextType.CODE:
                html_node = LeafNode("code", text_node.text)
            case TextType.LINK:
                html_node = LeafNode("a", text_node.text, {"href": text_node.url})
            case TextType.IMAGE:
                html_node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
            case _:
                raise Exception ("Text node must have TextType (TEXT, BOLD, ITALIC, CODE, LINK, OR IMAGE")
        return html_node
