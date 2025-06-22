from enum import Enum


class BlockType(Enum):

    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    newline_split_block = block.split("\n")
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    quote_check = True
    for newline in newline_split_block:
        if newline.startswith(">") is False:
            quote_check = False
            break
    if quote_check:
        return BlockType.QUOTE
    unordered_check = True
    for newline in newline_split_block:
        if newline.startswith("- ") is False:
            unordered_check = False
            break
    if unordered_check:
        return BlockType.UNORDERED_LIST
    ordered_check = True
    list_count = 0
    for newline in newline_split_block:
        list_count += 1
        if newline.startswith(f"{list_count}. ") is False:
            ordered_check = False
            break
    if ordered_check:
        return BlockType.ORDERED_LIST
    split_block = block.split(" ", 1)
    if len(split_block) == 1:
        return BlockType.PARAGRAPH
    if split_block[0] == ("#" * len(split_block[0])) and len(split_block[0]) < 7:
        if split_block[1] != "":
            return BlockType.HEADING
    return BlockType.PARAGRAPH

