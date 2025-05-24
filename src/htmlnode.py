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
            



