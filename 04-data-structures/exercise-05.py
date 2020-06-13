"""
1. Implement a Node class with 3 fields:
    name
    is_directory (file if False; directory if True)
    Size (int) – file size in bytes (filled for files only)
2. Create a tree matching representation in exercise-5.png
3. Write a function which calculates a size of any given Node, whether 
   it is a file or a directory. You might want to read about 
   tree traversal algorithms.
4. Calculate the size of /home/jakub directory
"""


class Node:
    def __init__(self, name, is_directory, size=0):
        self.name = name
        self.is_directory = is_directory
        self.size = size if not is_directory else 0
        self.children = {}
        self.parent = None

    def __repr__(self):
        type_ = "Dir" if self.is_directory else "File"
        return f"<{type_} {self.name}>"

    def __getitem__(self, key):
        return self.children[key]

    def add_child(self, name, is_directory, size=0):
        if not self.is_directory:
            raise ValueError("Cannot create a child of a file!")
        node = Node(name, is_directory, size)
        node.parent = self
        self.children[name] = node

    def calculate_size(self):
        if not self.is_directory:
            return self.size
        return sum(ch.calculate_size() for ch in self.children.values())


filesystem = Node("/", True)
filesystem.add_child("home", True)
filesystem["home"].add_child("jakub", True)
filesystem["home"]["jakub"].add_child(".bashrc", False, 50)
filesystem["home"]["jakub"].add_child(".vimrc", False, 100)
filesystem["home"]["jakub"].add_child("blob", False, 1023)
filesystem.add_child("var", True)
filesystem["var"].add_child("log", True)
filesystem["var"]["log"].add_child("sys.log", False, 10)

print("Size of /home/jakub: ", filesystem["home"]["jakub"].calculate_size())
