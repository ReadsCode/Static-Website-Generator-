from textnode import *

from blocks import *

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
    block_list = []
    if markdown == "":
        return block_list
    blocks = markdown.split("\n\n")
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block != "":
            block_list.append(stripped_block)
    return block_list


def block_type_to_html(block_type, block_text):
    match block_type:
        case BlockType.PARAGRAPH:
            return "p"
        case BlockType.HEADING:
            split_text = block_text.split()
            return f"h{len(split_text[0])}"
        case BlockType.CODE:
            return "pre"
        case BlockType.QUOTE:
            return "blockquote"
        case BlockType.UNORDERED_LIST:
            return "ul"
        case BlockType.ORDERED_LIST:
            return "ol"



def text_to_children(block):
    child_list = []
    text_node_list = text_to_textnodes(block)
    for text_node in text_node_list:
        child_node = text_node_to_html_node(text_node)
        child_list.append(child_node)
    return child_list



print(text_to_children("this is a **bold** and _italic_ text"))


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    node_list = []
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.CODE:
            block_html_node = ParentNode("pre", children=[HTMLNode("code", value=block)])
            node_list.append(block_html_node)
        elif block_type in (BlockType.PARAGRAPH, BlockType.HEADING, BlockType.QUOTE):
            block_line = block.replace("\n", " ")
            html_tag = block_type_to_html(block_type, block)
            block_html_node = ParentNode(html_tag, children=text_to_children(block_line), props={})
            node_list.append(block_html_node)
        else:
            html_tag = block_type_to_html(block_type, block)
            block_html_node = ParentNode(html_tag, children=text_to_children(block), props={})
            node_list.append(block_html_node)
    return ParentNode("div", children=node_list)
    
