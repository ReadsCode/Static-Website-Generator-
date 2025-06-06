from textnode import *

import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            new_node_text = node.text.split(delimiter)
            if len(new_node_text) % 2 == 0:
                raise Exception ("invalid markdown syntax, must have closing delimiter")
            for i in range((len(new_node_text))):
                if new_node_text[i] == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(new_node_text[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(new_node_text[i], text_type))
        else:
            new_nodes.append(node)
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)" , text)
    return matches