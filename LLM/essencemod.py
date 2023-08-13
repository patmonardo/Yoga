class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

class TriadTree:
    def __init__(self, triad_structure):
        self.root = self._build_tree(triad_structure)

    def _build_tree(self, node_structure):
        node = TreeNode(node_structure["name"])
        if "children" in node_structure:
            for child_name in node_structure["children"]:
                child_node = self._build_tree(child_name)
                node.add_child(child_node)
        return node

    def traverse(self, node=None, depth=0):
        if node is None:
            node = self.root
        print("  " * depth + node.name)
        for child in node.children:
            self.traverse(child, depth + 1)

essence = {
"Essence": {
  "children": [
    "Essence as Reflection Within",
    "Appearance",
    "Actuality"
  ]
}
}

reflection = {
"Essence as Reflection Within": {
  "children": [
    "Shine",
    "The essentialities or the determinations of reflection",
    "Ground"
  ]
},
"Shine": {
  "children": [
    "THE ESSENTIAL AND THE UNESSENTIAL",
    "SHINE",
    "REFLECTION"
  ]
},
"REFLECTION": {
  "children": [
    "Positing reflection",
    "External reflection",
    "Determining reflection"
  ]
},
"The essentialities or the determinations of reflection": {
  "children": [
    "IDENTITY",
    "DIFFERENCE",
    "CONTRADICTION"
  ]
},
"DIFFERENCE": {
  "children": [
    "Absolute difference",
    "Diversity",
    "Opposition"
  ]
},
"Ground": {
  "children": [
    "ABSOLUTE GROUND",
    "DETERMINATE GROUND",
    "CONDITION"
  ]
},
"ABSOLUTE GROUND": {
  "children": [
    "Form and essence",
    "Form and matter",
    "Form and content"
  ]
},
"DETERMINATE GROUND": {
  "children": [
    "Formal ground",
    "Real ground",
    "Complete ground"
  ]
},
"CONDITION": {
  "children": [
    "The relatively unconditioned",
    "The absolutely unconditioned",
    "Procession of the fact into concrete existence"
  ]
}
}

appearance = {
"Appearance": {
  "children": [
    "Concrete existence",
    "Appearance",
    "The essential relation"
  ]
},
"Concrete existence": {
  "children": [
    "THE THING AND ITS PROPERTIES",
    "THE CONSTITUTION OF THE THING OUT OF MATTERS",
    "DISSOLUTION OF THE THING"
  ]
},
"THE THING AND ITS PROPERTIES": {
  "children": [
    "The thing in itself and concrete existence",
    "Property",
    "The reciprocal action of things"
  ]
},
"Appearance": {
  "children": [
    "THE LAW OF APPEARANCE",
    "THE WORLD OF APPEARANCE AND THE WORLD-IN-ITSELF",
    "THE DISSOLUTION OF APPEARANCE"
  ]
},
"The essential relation": {
  "children": [
    "THE RELATION OF WHOLE AND PARTS",
    "THE RELATION OF FORCE AND ITS EXPRESSION",
    "RELATION OF OUTER AND INNER"
  ]
},
"THE RELATION OF FORCE AND ITS EXPRESSION": {
    "children": [
    "The conditionedness of force"
    "The solicitation of force"
    "The infinity of force"
  ]
}
}

actuality = {
"Actuality": {
  "children": [
    "The absolute",
    "Actuality",
    "The absolute relation"
  ]
},
"The absolute": {
  "children": [
    "THE EXPOSITION OF THE ABSOLUTE",
    "THE ABSOLUTE ATTRIBUTE",
    "THE MODE OF THE ABSOLUTE"
  ]
},
"Actuality": {
  "children": [
    "CONTINGENCY OR FORMAL ACTUALITY, POSSIBILITY, AND NECESSITY",
    "RELATIVE NECESSITY OR REAL ACTUALITY, POSSIBILITY, AND NECESSITY",
    "ABSOLUTE NECESSITY"
  ]
},
"The absolute relation": {
  "children": [
    "THE RELATION OF SUBSTANTIALITY",
    "THE RELATION OF CAUSALITY",
    "RECIPROCITY OF ACTION"
  ]
},
"THE RELATION OF CAUSALITY": {
  "children": [
    "Formal causality",
    "The determinate relation of causality",
    "Action and reaction"
  ]
}
}

# Define the triad structure dictionary
triad_structure = essence;

# Create and traverse the triad tree
tree = TriadTree(triad_structure)
tree.traverse()