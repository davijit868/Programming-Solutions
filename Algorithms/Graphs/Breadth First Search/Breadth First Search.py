# Pseudocode for Breadth First Search Algorithm

BFS (G,s)
	let Q be Queue.
	Q.enqueue(s) 
	mark s as visited.
	print(s)
	while ( Q is not empty )
		v = Q.dequeue()
		for all neighbours w of v in graph G:
			if w is not visited.
				print(w)
				Q.enqueue(w)
				mark w as visited.
		
