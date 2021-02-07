class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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

    def print_node(self,display_as):
        level = self.get_level()
        prefix = ' ' * level * 3 + '|--'
        data = None
        if display_as == 'name':
            data = self.name
        elif display_as == 'designation':
            data = self.designation
        else:
            data = self.name + ' (' + self.designation + ')'

        print(prefix + data)
        if self.children:
            for child in self.children:
                child.print_node(display_as)

def build_management_tree():
    Nilupul = TreeNode('Nilupul','CEO')
    Cinmay = TreeNode('Cinmay','CTO')
    Viswa = TreeNode('Viswa','Infra Head')
    Viswa.add_child(TreeNode('Dhaval','Cloud Manager'))
    Viswa.add_child(TreeNode('Abhijith','App Manager'))
    Cinmay.add_child(Viswa)
    Cinmay.add_child(TreeNode('Aamir', 'Application head'))

    Gels = TreeNode('Gels','HR Head')
    Gels.add_child(TreeNode('Peter','Recritment Manager'))
    Gels.add_child(TreeNode('Waqas', 'Policy Manager'))

    Nilupul.add_child(Cinmay)
    Nilupul.add_child(Gels)

    return Nilupul

if __name__ == '__main__':
    root = build_management_tree()
    root.print_node('name')
    print('\n')
    root.print_node('designation')
    print('\n')
    root.print_node('both')
