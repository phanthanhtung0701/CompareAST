from zss import simple_distance, distance, Node
from clangData import *
import clang.cindex as ci
from clang.cindex import TypeKind as tk
from clang.cindex import CursorKind as ck
import hashlib
from similarity import *

path_1 = 'test_data/00-original.cpp'
path_2 = 'test_data/02-order-changed.cpp'


class CustomNode(Node):
    def __init__(self, label, children=None, parent=None):
        super().__init__(label, children)
        self.hashcode = int(hashlib.md5(label.encode()).hexdigest(), 16)
        self.hashnode = self.hashcode
        self.parent = parent

    @staticmethod
    def get_parent(node):
        """
        Default value of ``get_parent``.

        :returns: ``self.parent``.
        """
        return node.parent

    def set_parent(self, parent):
        """
        Default value of ``get_parent``.

        :returns: ``self.parent``.
        """
        self.parent = parent

    def get_hashcode(self):
        """
        Default value of ``get_hashcode``.

        :returns: ``self.hashcode``.
        """
        return self.hashcode


def traverse_reduce(cursor_node, path):
    if (cursor_node.location.file and str(
            cursor_node.location.file) == path) or cursor_node.kind == ck.TRANSLATION_UNIT:
        ckind = cursor_node.kind
        tkind = cursor_node.type.kind
        idf = None
        cursors = []
        if ckind == ck.TRANSLATION_UNIT:
            idf = "TRANSLATION_UNIT"
        elif ckind != ck.UNEXPOSED_EXPR:
            # Function declarations:
            if ckind in funcDec:
                if cursor_node.is_const_method():
                    idf = "const_func"
                elif cursor_node.is_static_method():
                    idf = "static_func"
                else:
                    idf = "func"
                # https://stackoverflow.com/questions/7035356/c-why-static-member-function-cant-be-created-with-const-qualifier

            # Constructors:
            elif ckind == ck.CONSTRUCTOR:
                if cursor_node.is_converting_constructor():
                    tmp = "conv_con"
                elif cursor_node.is_copy_constructor():
                    tmp = "copy_con"
                elif cursor_node.is_default_constructor():
                    tmp = "def_con"
                elif cursor_node.is_move_constructor():
                    tmp = "move_con"
                else:
                    tmp = "con"
                idf = tmp

            # Variable declarations:
            elif ckind == ck.VAR_DECL:
                if tkind not in ignoreTypeKinds:
                    if tkind in numeric_types:
                        idf = "num_var"
                    else:
                        idf = tkind.name + "_var"
                else:
                    idf = "var"

            # Parameter declarations:
            elif ckind == ck.PARM_DECL:
                if tkind not in ignoreTypeKinds:
                    if tkind in numeric_types:
                        idf = "num_par"
                    else:
                        idf = tkind.name + "_par"
                else:
                    idf = "par"

            elif ckind == ck.TEMPLATE_TYPE_PARAMETER:
                idf = "T_par"

            # Access specifiers:
            elif ckind == ck.CXX_ACCESS_SPEC_DECL:
                idf = str(cursor_node.access_specifier).split('.')[1]

            # Usage of an already declared variable:
            elif ckind == ck.DECL_REF_EXPR:
                if tkind not in ignoreTypeKinds:
                    if tkind in numeric_types:
                        idf = "num_used"
                    else:
                        idf = tkind.name + "_used"

            # Function calls:
            elif ckind == ck.CALL_EXPR:
                if tkind not in ignoreTypeKinds:
                    if tkind in numeric_types:
                        idf = "num_called"
                    else:
                        idf = tkind.name + "_called"

            # Unary operator:
            elif ckind == ck.UNARY_OPERATOR:
                subnode = cursor_node.get_tokens()
                for st in subnode:
                    if st.kind.name == "PUNCTUATION" and st.spelling in unary_operators:
                        idf = st.spelling

            # Binary operators:
            elif ckind == ck.BINARY_OPERATOR:
                children_list = [i for i in cursor_node.get_children()]
                assert len(children_list) == 2
                left_offset = len([i for i in children_list[0].get_tokens()])
                op = [i for i in cursor_node.get_tokens()][left_offset].spelling
                idf = op

            # Compound operators:
            elif ckind == ck.COMPOUND_ASSIGNMENT_OPERATOR:
                # Compund assignment operator is equivalent to binary operator
                children_list = [i for i in cursor_node.get_children()]
                assert len(children_list) == 2
                left_offset = len([i for i in children_list[0].get_tokens()])
                op = [i for i in cursor_node.get_tokens()][left_offset].spelling
                idf = op

            # Conditional operators:
            elif ckind == ck.CONDITIONAL_OPERATOR:
                idf = "?:"

            # Explicit type casting:
            elif ckind == ck.CSTYLE_CAST_EXPR or ckind == ck.CXX_FUNCTIONAL_CAST_EXPR:
                if tkind not in ignoreTypeKinds:
                    if tkind in numeric_types:
                        idf = "cast_num"
                    else:
                        idf = "cast_" + tkind.name
                else:
                    idf = "cast"

            # Boolean literals
            elif ckind == ck.CXX_BOOL_LITERAL_EXPR:
                idf = "bool_literal"

            # Null pointer literals
            elif ckind == ck.CXX_NULL_PTR_LITERAL_EXPR:
                idf = "nullptr"

            # Common keywords
            elif ckind == ck.CXX_THIS_EXPR:
                idf = "this"
            elif ckind == ck.CXX_THROW_EXPR:
                idf = "throw"
            elif ckind == ck.CXX_NEW_EXPR:
                idf = "new"
            elif ckind == ck.CXX_DELETE_EXPR:
                idf = "delete"

            # for(:) is treated the same as for(;;)
            elif ckind == ck.CXX_FOR_RANGE_STMT:
                idf = "for_stmt"

            # All numeric literals are treated the same:
            elif ckind in numeric_literals:
                idf = "num_literal"

            # Directly add miscellanous node
            elif ckind in misc:
                idf = ckind.name

            elif tkind not in ignoreTypeKinds:
                idf = ckind.name
        for c in cursor_node.get_children():
            child_node = traverse_reduce(c, path)
            if child_node:
                for c_n in child_node:
                    cursors.append(c_n)
        if idf:
            return [CustomNode(idf.lower(), cursors)]
        else:
            return cursors


def traverse_set_parent_hashcode(node):
    if node is not None:
        # Recurse for children of this node
        children = CustomNode.get_children(node)
        if children:
            for childNode in children:
                childNode.set_parent(node)
                traverse_set_parent_hashcode(childNode)
                node.hashnode += childNode.hashnode


def reduceAST(path):
    index = ci.Index.create()
    tu = index.parse(path, ['-x', 'c++', '-std=c++11', '-D__CODE_GENERATOR__'])  # Root of the AST
    cursor = tu.cursor
    res = traverse_reduce(cursor, path)[0]
    traverse_set_parent_hashcode(res)
    return res


def traverseAST(node):
    sequence = []
    if node is not None:
        sequence.append(CustomNode.get_label(node))
        for childNode in CustomNode.get_children(node):
            sequence.extend(traverseAST(childNode))
    return sequence


def hashListClassify(node, size):
    # hashList = list()
    # for i in range(size+1):
    #
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


def compare(hashList_1, hashList_2):
    n = min(len(hashList_1), len(hashList_2))
    pair = []
    ls = []
    for n_sub_node in range(1, n):
        L1 = hashList_1[n_sub_node]
        L2 = hashList_2[n_sub_node]
        L1 = sorted(L1, key=lambda x: x.hashnode)
        L2 = sorted(L2, key=lambda x: x.hashnode)
        i = 0
        j = 0
        while i < len(L1) and j < len(L2):
            P1 = CustomNode.get_parent(L1[i])
            P2 = CustomNode.get_parent(L2[j])
            if P1 and P2 and P1 in ls:
                i += 1
                continue
            elif P1 and P2 and P2 in ls:
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


def compare_from_root(hashList_1, hashList_2):
    n = min(len(hashList_1), len(hashList_2))
    pair = []
    for n_sub_node in range(n-1, 0, -1):
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


def default_tree_size(tree, get_children):
    size = 1
    children = get_children(tree)
    if children:
        size = size + sum(default_tree_size(child, get_children) for child in children)
    return size


def compute_normalized_distance_3(edit_distance, alpha, size_A, size_B):
    return (2 * edit_distance) / (alpha * (size_A + size_B) + edit_distance)


def compute_normalized_distance_2(edit_distance, alpha, size_A, size_B):
    return (alpha * (size_A + size_B) - edit_distance) / 2


def compute_normalized_distance_0(edit_distance, alpha, size_A, size_B):
    return 2 * edit_distance / (size_A + size_B)


def compute_normalized_distance_1(edit_distance, alpha, size_A, size_B):
    return edit_distance / max(size_A, size_B)


def printASTNode(node, level):
    for i in range(0, level - 1):
        print('  ', end="")
    parent = None
    if CustomNode.get_parent(node):
        parent = CustomNode.get_label(CustomNode.get_parent(node))
    print(f'+-- {CustomNode.get_label(node)}    {parent}')


def visualizeAST(node, level):
    if node is not None:
        level = level + 1
        printASTNode(node, level)
        # Recurse for children of this node
        for childNode in CustomNode.get_children(node):
            visualizeAST(childNode, level)
        level = level - 1


def _str_dist(i, j):
    return 0 if i == j else 1
    # return 0


if __name__ == '__main__':
    reduce_ast1 = reduceAST(path_1)
    reduce_ast2 = reduceAST(path_2)
    size_1 = default_tree_size(reduce_ast1, CustomNode.get_children)
    size_2 = default_tree_size(reduce_ast2, CustomNode.get_children)
    print(size_1)
    print(size_2)
    print(visualizeAST(reduce_ast1, 0))
    print('-' * 20)
    print(visualizeAST(reduce_ast2, 0))
    # # dist = simple_distance(reduce_ast1, reduce_ast2)
    # dist = distance(reduce_ast1, reduce_ast2, CustomNode.get_children, insert_cost=lambda node: 1,
    #                 remove_cost=lambda node: 1, update_cost=lambda a, b: _str_dist(a, b))
    # print(dist)
    #
    # # sim = compute_normalized_distance_2(dist, 1, size_1, size_2)
    # print(1 - compute_normalized_distance_0(dist, 1, size_1, size_2))
    # print(1 - compute_normalized_distance_1(dist, 1, size_1, size_2))
    # print(1 - compute_normalized_distance_3(dist, 1, size_1, size_2))

    hashList1 = hashListClassify(reduce_ast1, size_1)
    hashList2 = hashListClassify(reduce_ast2, size_2)

    res = compare(hashList1, hashList2)
    total = 0
    for r in res:
        print(r)
        total += default_tree_size(r[0], CustomNode.get_children)

    print(total)
    print(size_1)
    print(size_2)
    print(2*total/(size_1+size_2))
    results1 = traverseAST(reduce_ast1)
    results2 = traverseAST(reduce_ast2)
    #
    print(results1)
    print(results2)
    #
    # # normalized distance between 2 sequences
    # print('---LCS\t\t\t\t\t: ', end='')
    # print(lcs_based_coeff(results1, results2))
    #
    # print('---Ratcliff/Obershelp Sequence Matcher: ', end='')
    # print(SequenceMatcher(None, results1, results2).ratio())
    #
    # print('---Damerau–Levenshtein\t: ', end='')
    # print(compare_stats(results1, results2)[0])
    #
    # print('---TF_IDF\t\t\t\t: ', end='')
    # print(tf_idf_similarity(results1, results2)[0][1])
