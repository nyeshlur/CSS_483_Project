# from Processing.GraphClass import Graph

class Vertex:
    def __init__(self, node):
        self.id = node
        self.neighbors = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.neighbors])

    def add_neighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vertices[node] = new_vertex
        return new_vertex

    def get_vertex(self, node):
        if node in self.vertices:
            return self.vertices[node]
        else:
            return None

    def add_edge(self, frm, to, weight=0):
        if frm not in self.vertices:
            self.add_vertex(frm)
        if to not in self.vertices:
            self.add_vertex(to)

        self.vertices[frm].add_neighbor(self.vertices[to], weight)
        self.vertices[to].add_neighbor(self.vertices[frm], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def to_file(self, trans_dict, file_name):
        with open(file_name, ".txt") as f:
            for idx in range(len(trans_dict)):
                if trans_dict[idx] in self.vertices:
                    neighs = self.vertices[trans_dict[idx]].neighbors


org_label = {}
with open("label.txt") as f:
    for line in f:
        (key, val) = line.split()
        org_label[key.strip()] = val.strip()
print("label_dict", len(org_label))

graph_part = Graph()
with open("networkdata.txt") as f:
    for line in f:
        v1, v2, w = line.split()
        if v1 in org_label and v2 in org_label and int(w) >= 750:
            graph_part.add_edge(v1, v2, int(w))

print(graph_part.num_vertices)

trans_dict = {}
trans_dict_reverse = {}
idx = 0
for v in graph_part.vertices:
    trans_dict[idx] = v
    trans_dict_reverse[v] = idx
    idx += 1

label_list = []
for i in range(idx):
    item = 1 if (org_label[trans_dict[i]]) == "E" else 0
    label_list.append(item)
print("Count of essentials", label_list.count(1))

num_edges = 0
for v in graph_part.get_vertices():
    num_edges += len(graph_part.get_vertex(v).get_neighbors())
print(num_edges)  # 1021786 correct

with open('NetworkForMotif.txt', 'w') as f:
    for v in graph_part.get_vertices():
        vwrite = trans_dict_reverse[v]
        for t in graph_part.get_vertex(v).get_neighbors():
            f.write("%d %d\n" % (vwrite, trans_dict_reverse[t.id]))
