
class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False

        self_children = self.children or []
        other_children = other.children or []

        return (
                self.tag == other.tag and
                self.value == other.value and
                self_children == other_children and
                self.props == other.props
            )

    def __repr__(self):
        return f"tag: \"{self.tag}\", value = \"{self.value}\", children = \"{self.children}\", props = \"{self.props}\""

    def props_to_html(self):
        prop_string = ""
        if self.props == None or self.props == {}:
            return ""
        else:
            for key, value in self.props.items():
                prop_string += f" {key}=\"{value}\""

        return prop_string

    def to_html(self):
        raise NotImplementedError

    def text_node_to_html_node(text_node):
        print(text_node.text_type)


###################

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag = tag, value = value, props = props)

    def __repr__(self):
        return f"tag: \"{self.tag}\", value = \"{self.value}\", props = \"{self.props}\""

    def to_html(self):
        #print(f"Tag: {self.tag}")
        #print(f"Value: {self.value}")
        #print(f"Props: {self.props}")
        if self.value is None:
            raise ValueError('All leaf nodes must have a value')
        if self.tag is None:
            return self.value # as raw text
        else:
            if self.props == None:
                htmltag = f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                htmltag = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            return htmltag

#####################

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None): # no "value" argument; "props" optional
        super().__init__(tag = tag, children = children, props = props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('All parent nodes must have a tag')
        if self.children is None or self.children == []:
            raise ValueError('Children is missing value')
        else:
            htmltag = f"<{self.tag}"
            if self.props:
                htmltag += f"{self.props_to_html()}"
            htmltag += f">"

            for childNode in self.children:
                htmltag += childNode.to_html()
            htmltag += f"</{self.tag}>"
            return htmltag
