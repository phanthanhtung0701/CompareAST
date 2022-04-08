from zss import simple_distance, distance, Node
from clangData import *
import clang.cindex as ci
from clang.cindex import TypeKind as tk
from clang.cindex import CursorKind as ck

path1 = 'test_data/test_1.cpp'
path2 = 'test_data/test_2.cpp'


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
            return [Node(idf.lower(), cursors)]
        else:
            return cursors


def reduceAST(path):
    index = ci.Index.create()
    tu = index.parse(path, ['-x', 'c++', '-std=c++11', '-D__CODE_GENERATOR__'])  # Root of the AST
    cursor = tu.cursor
    res = traverse_reduce(cursor, path)
    return res


def default_tree_size(tree, get_children):
    size = 1
    children = get_children(tree)
    if children:
        size = size + sum(default_tree_size(child, get_children) for child in children)
    return size


def compute_normalized_distance(edit_distance, alpha, size_A, size_B):
    return (2 * edit_distance) / (alpha * (size_A + size_B) + edit_distance)


def compute_normalized_distance2(edit_distance, alpha, size_A, size_B):
    return edit_distance / max(size_A, size_B)


def printASTNode(node, level):
    for i in range(0, level - 1):
        print('  ', end="")
    print(f'+-- {Node.get_label(node)}')


def visualizeAST(node, level):
    if node is not None:
        level = level + 1
        printASTNode(node, level)
        # Recurse for children of this node
        for childNode in Node.get_children(node):
            visualizeAST(childNode, level)
        level = level - 1


if __name__ == '__main__':
    reduce_ast1 = reduceAST(path1)[0]
    reduce_ast2 = reduceAST(path2)[0]
    size_1 = default_tree_size(reduce_ast1, Node.get_children)
    size_2 = default_tree_size(reduce_ast2, Node.get_children)
    print(size_1)
    print(size_2)
    print(visualizeAST(reduce_ast1, 0))
    print('-' * 20)
    print(visualizeAST(reduce_ast2, 0))
    # dist = simple_distance(reduce_ast1, reduce_ast2)
    dist = distance(reduce_ast1, reduce_ast2, Node.get_children, insert_cost=lambda node: 1,
                    remove_cost=lambda node: 1, update_cost=lambda a, b: 0)
    print(dist)
    sim = compute_normalized_distance(dist, 1, size_1, size_2)
    print(1 - sim)
