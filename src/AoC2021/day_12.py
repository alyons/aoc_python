from typing import List, Set
from reprint import output
from time import clock_gettime_ns, CLOCK_REALTIME

def get_other_node(node: str, edge: List[str]) -> str:
    if node == edge[0]:
        return edge[1]
    else:
        return edge[0]


def simple_paths(edges: List[List[str]]) -> List[str]:
    complete = []
    potential = [['start']]

    while potential:
        to_parse = potential.pop() # The next list to go through
        n = to_parse[-1]

        # Add any paths that have end at the end
        if n == 'end' and not to_parse in complete:
            complete.append(to_parse)
            continue

        # Find all of the nodes one could travel to from the last node
        test_nodes = []
        for e in edges:
            if n in e:
                test_nodes.append(get_other_node(n, e))
        
        # For each of those nodes one could travel to
        for t in test_nodes:
            add = to_parse.copy()

            if t.isupper():
                add.append(t)
            elif t.islower():
                if t == 'start' or t in add:
                    add.clear()
                else:
                    add.append(t)

            if add and not add in potential and not add in complete:
                potential.append(add)

    return complete


def has_double_vist(path: List[str], small_caves: Set[str]) -> bool:
    small_count = [path.count(c) for c in small_caves]

    return any(c == 2 for c in small_count)


def complex_paths(edges: List[List[str]], show_console: bool = False) -> List[str]:
    complete = []
    potential = [['start']]
    small_caves = {e for edge in edges for e in edge if e.islower()}
    if show_console: print(f'Small Caves: {small_caves}')

    with output('dict') as output_lines:
        while potential:
            to_parse = potential.pop() # The next list to go through
            n = to_parse[-1]

            # Add any paths that have end at the end
            if n == 'end' and not to_parse in complete:
                complete.append(to_parse)
                continue

            # Find all of the nodes one could travel to from the last node
            test_nodes = [get_other_node(n, edge) for edge in edges if n in edge]
            
            # For each of those nodes one could travel to
            for t in test_nodes:
                add = to_parse.copy()

                if t.isupper():
                    add.append(t)
                elif t.islower():
                    if (t == 'start') or (t == 'end' and t in add) or (has_double_vist(add, small_caves) and t in add):
                        add.clear()
                    else:
                        add.append(t)

                if add and not add in potential and not add in complete:
                    potential.append(add)

            # Print Current State
            if show_console: output_lines['Test Path Count'] = len(potential)
            if show_console: output_lines['Testing'] = potential[-1] if potential else 'N/A'
            if show_console: output_lines['Current Complete Count'] = len(complete)

    return complete


def valid_simple_path(path: List[str]) -> bool:
    return path[0] == 'start' and path.count('end') <= 1 and all([path.count(n) == 1 or n.isupper() for n in path])

def complete_simple_path(path: List[str]) -> bool:
    return path[0] == 'start' and path[-1] == 'end' and all([path.count(n) == 1 or n.isupper() for n in path])


def simple_paths_recursive(edges: List[List[str]], cave: str = 'start', path: List[str] = [], complete_paths: List[List[str]] = []) -> List[List[str]]:
    path.append(cave)
    if cave == 'end' and complete_simple_path(path):
        complete_paths.append(path)
        return complete_paths

    next_nodes = [get_other_node(cave, edge) for edge in edges if cave in edge]

    for n in next_nodes:
        next_path = path.copy()

        if valid_simple_path(next_path):
            simple_paths_recursive(edges, n, next_path, complete_paths)

    return complete_paths
