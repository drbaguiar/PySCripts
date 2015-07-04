
def bfs(startNode):
		
	stack = [];
	startNode.visited = True;
	stack.append(startNode);

	#ez addig fog futni amig nem lesz ures, ez tipikus pythonos megoldas
	while stack: 

		actualNode = stack.pop();
		print("%s -> " % actualNode.name );
		
		for n in actualNode.adjacenciesList:
			if not n.visited:
				n.visited = True;
				stack.append(n);
