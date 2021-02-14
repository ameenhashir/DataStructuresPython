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

    def print_node(self,lvl):
        level = self.get_level()
        prefix = ' ' * level * 3 + '|--'
        print(prefix + self.data)
        if self.children and level < lvl:
            for child in self.children:
                child.print_node(lvl)

def configure_tree():
    #level0
    Global = TreeNode('Global')

    # level1
    india = TreeNode("India")
    USA = TreeNode("USA")
    Global.add_child(india)
    Global.add_child(USA)

    # level2
    Gujarath = TreeNode('Gujarath')
    Karnataka = TreeNode('Karnataka')
    NewJersey = TreeNode('New Jersey')
    California = TreeNode('California')
    india.add_child(Gujarath)
    india.add_child(Karnataka)
    USA.add_child(NewJersey)
    USA.add_child(California)

    # level3
    Gujarath.add_child(TreeNode('Ahmedabad'))
    Gujarath.add_child(TreeNode('Baroda'))
    Karnataka.add_child(TreeNode('Bangalore'))
    Karnataka.add_child(TreeNode('Mysore'))
    NewJersey.add_child(TreeNode('Priceton'))
    NewJersey.add_child(TreeNode('Trenton'))
    California.add_child(TreeNode('San Francisco'))
    California.add_child(TreeNode('Mountain View'))
    California.add_child(TreeNode('Palo Alto'))

    return Global

if __name__ == '__main__':
    root = configure_tree()
    root.print_node(2)
