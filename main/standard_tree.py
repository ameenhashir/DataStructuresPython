class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_node(self):
        level = self.get_level()
        prefix = ' ' * level * 3 + '|--'
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_node()

def configure_tree():
    root = TreeNode('Electronics')

    laptops = TreeNode('Laptops')
    laptops.add_child(TreeNode('MacBook'))
    laptops.add_child(TreeNode('MS Surface'))
    laptops.add_child(TreeNode('Thinkpad'))

    cellPhones = TreeNode('Cell Phones')
    cellPhones.add_child(TreeNode('iphone'))
    cellPhones.add_child(TreeNode('Google Pixel'))
    cellPhones.add_child(TreeNode('vivo'))

    televisions = TreeNode('Television')
    televisions.add_child(TreeNode('Samsung'))
    televisions.add_child(TreeNode('LG'))

    root.add_child(laptops)
    root.add_child(cellPhones)
    root.add_child(televisions)

    return root

if __name__ == '__main__':
    root = configure_tree()
    root.print_node()
