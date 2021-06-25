"""
Let's say we have N modules in a software. A module may use the output of the other modules to complete some tasks. Now,
you are provided by an array dep of length N, which stores the dependency of the modules. For example, if module 0 needs
the output from module 1 and 2, then dep[0]=[1,2].

Your task is to arrange a proper order for the software to successfully run all the modules one by one.
Write a function schedule to return a proper order given the array dep. For example, if dep=[[],[],[0,1]],
the proper orders could be [0, 1, 2] or [1, 0, 2], because module 2 depends on module 0 and 1.

Note: When there are two modules that can run at the same time, choose the one with smaller node label.
Use the above example, both module 0 and 1 should be run before node 2, but you should return [0, 1, 2].
If there is no proper order, return None.
考察拓扑排序
"""
def schedule(dep):
    order = []
    indegree = []
    queue = []
    seen = []
    for i in range(len(dep)):
        indegree.append(len(dep[i]))
    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)
            seen.append(i)
    while len(queue) != 0:
        queue.sort()
        vertex = queue.pop(0)
        order.append(vertex)
        for i in range(len(dep)):
            if vertex in dep[i]:
                indegree[i] -= 1
            if indegree[i] == 0 and i not in seen:
                queue.append(i)
                seen.append(i)
    if len(order) <  len(dep):
        return None
    return order


dep = [[], [0, 3], [0], [2, 5], [1], [1], [3, 4, 5]]
print(schedule(dep))