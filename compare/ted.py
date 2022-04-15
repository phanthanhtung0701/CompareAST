from zss import simple_distance, distance, Node
from reduceAST import CustomNode, default_tree_size


def compute_normalized_distance_3(edit_distance, alpha, size_A, size_B):
    return (2 * edit_distance) / (alpha * (size_A + size_B) + edit_distance)


def compute_normalized_distance_2(edit_distance, alpha, size_A, size_B):
    return (alpha * (size_A + size_B) - edit_distance) / 2


def compute_normalized_distance_0(edit_distance, alpha, size_A, size_B):
    return 2 * edit_distance / (size_A + size_B)


def compute_normalized_distance_1(edit_distance, alpha, size_A, size_B):
    return edit_distance / max(size_A, size_B)


def _str_dist(i, j):
    return 0 if i == j else 1
    # return 0


def ted(ast1, ast2):
    dist = distance(ast1, ast2, CustomNode.get_children, insert_cost=lambda node: 1,
                    remove_cost=lambda node: 1, update_cost=lambda a, b: _str_dist(a, b))
    return dist


def ted_similarity(ast1, ast2):
    dist = ted(ast1, ast2)
    size_1 = default_tree_size(ast1, CustomNode.get_children)
    size_2 = default_tree_size(ast2, CustomNode.get_children)
    sim = 1 - compute_normalized_distance_3(dist, 1, size_1, size_2)
    return sim
