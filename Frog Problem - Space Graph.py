import networkx as nx, matplotlib.pyplot as plt, queue

untracked = queue.Queue(0)

root = ['1', '1', '1', '0', '2', '2', '2']
goal = ['2', '2', '2', '0', '1', '1', '1']

state_graph = nx.Graph()
untracked.put(root)
count = 0

def get_children(parent):
    index0 = parent.index("0")
    length = len(parent)
    
    if index0 < length - 1 and parent[index0 + 1] == "2":
        n = parent.copy()
        swap(n, index0, index0 + 1)
        add_node(parent, n)
    if index0 < length - 2 and parent[index0 + 2] == "2":
        n = parent.copy()
        swap(n, index0, index0 + 2)
        add_node(parent, n)
    if index0 > 0 and parent[index0 - 1] == "1":
        n = parent.copy()
        swap(n, index0, index0 - 1)
        add_node(parent, n)
    if index0 > 1 and parent[index0 - 2] == "1":
        n = parent.copy()
        swap(n, index0, index0 - 2)
        add_node(parent, n)
       
def swap(element, index1, index2):
    temp = element[index1]
    element[index1] = element[index2]
    element[index2] = temp      
        
def add_node(parent, child):
    state_graph.add_edge(''.join(parent), ''.join(child))
    untracked.put(child)
    
while untracked.qsize() > 0:
    node = untracked.get()
    count = count + 1
    
    if node != goal:
        get_children(node)
                
nx.draw(state_graph, with_labels = True)
print("States:", count)