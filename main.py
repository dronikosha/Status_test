items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]


class TreeStore():
    def __init__(self, tree):
        self.tree = tree

    def getAll(self):
        return self.tree

    def getItem(self, id):
        for item in self.tree:
            if item["id"] == id:
                return item
        return None

    def getChildren(self, id):
        children = []
        for item in self.tree:
            if item["parent"] == id:
                children.append(item)
        return children

    def getAllParents(self, id):
        parents = []
        item = self.getItem(id)
        while item["parent"] != "root":
            item = self.getItem(item["parent"])
            parents.append(item)
        return parents


ts = TreeStore(items)
print("GET ALL:", ts.getAll())
print("GET ITEM: ", ts.getItem(7))
print("GET CHILDREN: ", ts.getChildren(4))
print("GET PARENTS: ", ts.getAllParents(7))
