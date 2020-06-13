class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.children = {}

    def __repr__(self):
        return f"<Node {self.value}>"

    def add_branch(self, branch):
        names = branch.split(".")
        parent = self
        for name in names:
            if name not in parent.children:
                parent.add_child(Node(name))
            parent = parent.children[name]

    def add_child(self, node):
        node.parent = self
        self.children[node.value] = node


mammals = Node("mammals")
carnivora = Node("carnivora")
mammals.add_child(carnivora)
print(mammals.children)

mammals.add_branch("carnivora.felidae.panthera")
mammals.add_branch("carnivora.canidae.caninae")
mammals.add_branch("chiroptera.microchiroptera")

print(mammals.children)
print(mammals.children["carnivora"].children)
print(mammals.children["carnivora"].children["canidae"].children)
