import unittest


from blocks import *


class TestBlocks(unittest.TestCase):


    def test_block_to_blocktype_heading(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    

    def test_block_to_block_type_code(self):
        block = "```print(test)```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)


    def test_block_to_block_type_quote(self):
        block = "> Check out this quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)


    def test_block_to_block_type_unordered_list(self):
        block = """- test\n- this\n- list"""
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)


    def test_block_to_block_type_ordered_list(self):
        block = """1. Test
2. This
3. List"""
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)


    def test_block_to_block_type_paragraph(self):
        block = "test paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
