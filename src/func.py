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


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    text_nodes = []
    old_nodes = [TextNode(text, TextType.TEXT)]
    old_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
    old_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
    old_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
    old_nodes = split_nodes_image(old_nodes)
    old_nodes = split_nodes_link(old_nodes)
    return old_nodes


def markdown_to_blocks(markdown):
    pass


