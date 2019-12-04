# 


edges = { 
			"S": {"A": 1, "C": 2},
			"C": {"A": 4, "D": 3},
			"A": {"B": 6},
			"B": {"D": 1, "E": 2},
			"D": {"E": 1}
		}

sources = { 
			"C": {"S": 2},
			"A": {"S": 1, "C": 4},
			"D": {"C": 3, "B": 1},
			"E": {"D": 1, "B":2},
			"B": {"A": 6}
		}

arr = [-1] * 6

arr = {"S":-, "C", "A", "B", "D", "E"]

def shortestPathDAG(graph):
	n = len(linearized)-1
	arr[0] = 0
	while n:
		mini = float.inf 
		for source, dist in sources[n]:
			cur = arr[source]



print(shortestPathDAG(edges))