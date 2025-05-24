from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, props, children=None)
    
    def to_html(self):
        if self.value == None:
            raise ValueError ("All LeafNodes must have a value")
        if self.tag == None:
            return f"{self.value}"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
