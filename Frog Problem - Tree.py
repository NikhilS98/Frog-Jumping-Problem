from ete3 import Tree, TreeStyle, TextFace, add_face_to_node
import queue

untracked = queue.Queue(0)

root = ['1', '1', '1', '0', '2', '2', '2']
goal = ['2', '2', '2', '0', '1', '1', '1']

search_tree = Tree()
untracked.put(search_tree.add_child(name = root))
count = 0

def get_children(parent):
    name = parent.name
    index0 = name.index("0")
    
    if index0 < len(name) - 1 and name[index0 + 1] == "2":
        n = name.copy()
        swap(n, index0, index0 + 1)
        add_node(parent, n)
    if index0 < len(name) - 2 and name[index0 + 2] == "2":
        n = name.copy()
        swap(n, index0, index0 + 2)
        add_node(parent, n)
    if index0 > 0 and name[index0 - 1] == "1":
        n = name.copy()
        swap(n, index0, index0 - 1)
        add_node(parent, n)
    if index0 > 1 and name[index0 - 2] == "1":
        n = name.copy()
        swap(n, index0, index0 - 2)
        add_node(parent, n)
       
def swap(element, index1, index2):
    temp = element[index1]
    element[index1] = element[index2]
    element[index2] = temp      
        
def add_node(parent, child):
    untracked.put(parent.add_child(name = child))

while untracked.qsize() > 0:
    node = untracked.get()
    count = count + 1
    
    if node.name != goal:
        get_children(node)
        
        
ts = TreeStyle()
ts.show_leaf_name = False

def my_layout(node):
        F = TextFace(''.join(node.name))
        add_face_to_node(F, node, column=0, position="branch-right")
ts.layout_fn = my_layout

search_tree.show(tree_style=ts)
print("States:", count)
        