from reduceAST import CustomNode, default_tree_size


def hashListClassify(node, size):
    hashList = [[] for _ in range(size + 1)]

    def traverseHash(sub_node):
        if sub_node is not None:
            n_node = default_tree_size(sub_node, CustomNode.get_children)
            if n_node > 0:
                hashList[n_node].append(sub_node)
            for childNode in CustomNode.get_children(sub_node):
                traverseHash(childNode)

    traverseHash(node)
    return hashList


def compare_from_parent(hashList_1, hashList_2, threshold=1):
    n = min(len(hashList_1), len(hashList_2))
    pair = []
    ls = []
    for n_sub_node in range(n - 1, threshold - 1, -1):
        L1 = hashList_1[n_sub_node]
        L2 = hashList_2[n_sub_node]
        L1 = sorted(L1, key=lambda x: x.hashnode)
        L2 = sorted(L2, key=lambda x: x.hashnode)
        i = 0
        j = 0
        while i < len(L1) and j < len(L2):
            P1 = CustomNode.get_parent(L1[i])
            P2 = CustomNode.get_parent(L2[j])
            if P1 and P1 in ls:
                ls.append(L1[i])
                i += 1
                continue
            elif P2 and P2 in ls:
                ls.append(L2[j])
                j += 1
                continue
            if L1[i].hashnode > L2[j].hashnode:
                j += 1
            elif L1[i].hashnode < L2[j].hashnode:
                i += 1
            else:
                pair.append([L1[i], L2[j]])
                ls.append(L1[i])
                ls.append(L2[j])
                i += 1
                j += 1

    return pair


def compare(hashList_1, hashList_2, threshold=1):
    n = min(len(hashList_1), len(hashList_2))
    pair = []
    for n_sub_node in range(threshold, n):
        L1 = hashList_1[n_sub_node]
        L2 = hashList_2[n_sub_node]
        L1 = sorted(L1, key=lambda x: x.hashnode)
        L2 = sorted(L2, key=lambda x: x.hashnode)
        i = 0
        j = 0
        while i < len(L1) and j < len(L2):
            P1 = CustomNode.get_parent(L1[i])
            P2 = CustomNode.get_parent(L2[j])
            if P1 and P2 and P1.hashnode == P2.hashnode:
                i += 1
                j += 1
                continue
            if L1[i].hashnode > L2[j].hashnode:
                j += 1
            elif L1[i].hashnode < L2[j].hashnode:
                i += 1
            else:
                pair.append([L1[i], L2[j]])
                i += 1
                j += 1

    return pair


def ast_cc_similarity(ast1, ast2):
    size_1 = default_tree_size(ast1, CustomNode.get_children)
    size_2 = default_tree_size(ast2, CustomNode.get_children)

    hashList1 = hashListClassify(ast1, size_1)
    hashList2 = hashListClassify(ast2, size_2)

    res = compare(hashList1, hashList2, threshold=2)
    total = 0
    for r in res:
        total += default_tree_size(r[0], CustomNode.get_children)

    return 2 * total / (size_1 + size_2)


def ast_cc_compare(ast1, ast2):
    size_1 = default_tree_size(ast1, CustomNode.get_children)
    size_2 = default_tree_size(ast2, CustomNode.get_children)

    hashList1 = hashListClassify(ast1, size_1)
    hashList2 = hashListClassify(ast2, size_2)

    res = compare_from_parent(hashList1, hashList2, threshold=2)
    total = 0
    if not res:
        print('There aren\'t common')
        return 0
    print('---------AST1--------- | ---------AST2---------')
    for r in res:
        print('(%3d, %3d), (%3d, %3d) | (%3d, %3d), (%3d, %3d)'
              % (r[0].start[0], r[0].start[1], r[0].end[0], r[0].end[1],
                 r[1].start[0], r[1].start[1], r[1].end[0], r[1].end[1]))
        total += default_tree_size(r[0], CustomNode.get_children)

    return 2 * total / (size_1 + size_2)
