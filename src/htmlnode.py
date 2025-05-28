class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return_string = ""
        if self.props == None:
            return ""
        for key in self.props:
            return_string += f' {key}="{self.props[key]}"'
        return return_string

    def __repr__(self):
        return f"HTMLNODE(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})"



class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError ("must have a tag")
        elif self.children is None:
            raise ValueError ("parentnode must have children")
        elif self.children == []:
            raise ValueError ("list cannot be empty")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"



class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.props == other.props:
            return True
        else:
            return False
    
    def to_html(self):
        if self.value == None:
            raise ValueError ("All LeafNodes must have a value")
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
            



