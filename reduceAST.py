from zss import Node
from clangData import *
import clang.cindex as ci
from clang.cindex import TypeKind as tk
from clang.cindex import CursorKind as ck
import hashlib


class CustomNode(Node):
    def __init__(self, label, children=None, spelling=None, parent=None, line=None, column=None):
        super().__init__(label, children)
        self.hashcode = int(hashlib.md5(label.encode()).hexdigest(), 16)
        self.hashnode = self.hashcode
        self.parent = parent
        self.spelling = spelling
        self.start = (line, column)
        self.end = None
        self.get_end_location()

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

    def get_end_location(self):
        def traverse_set_location(node):
            if node is not None:
                positions = []
                # Recurse for children of this node
                children = CustomNode.get_children(node)
                if children:
                    for childNode in children:
                        positions.append(traverse_set_location(childNode))

                    positions = sorted(positions, reverse=True)
                    node.end = positions[0]
                else:
                    node.end = node.start
                return node.end

        traverse_set_location(self)


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
                    tmp = "conv_constructor"
                elif cursor_node.is_copy_constructor():
                    tmp = "copy_constructor"
                elif cursor_node.is_default_constructor():
                    tmp = "def_constructor"
                elif cursor_node.is_move_constructor():
                    tmp = "move_constructor"
                else:
                    tmp = "constructor"
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
            return [CustomNode(idf.lower(), cursors,
                               line=cursor_node.location.line,
                               column=cursor_node.location.column)]
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


def default_tree_size(tree, get_children):
    size = 1
    children = get_children(tree)
    if children:
        size = size + sum(default_tree_size(child, get_children) for child in children)
    return size


def printASTNode(node, level):
    for i in range(0, level - 1):
        print('  ', end="")
    parent = None
    if CustomNode.get_parent(node):
        parent = CustomNode.get_label(CustomNode.get_parent(node))
    print(f'+-- {CustomNode.get_label(node)}    <start={node.start} end={node.end}>')


def visualizeAST(node, level):
    if node is not None:
        level = level + 1
        printASTNode(node, level)
        # Recurse for children of this node
        for childNode in CustomNode.get_children(node):
            visualizeAST(childNode, level)
        level = level - 1


if __name__ == '__main__':
    path_1 = 'test_data/test_1.cpp'
    path_2 = 'test_data/test_2.cpp'
    reduce_ast1 = reduceAST(path_1)
    reduce_ast2 = reduceAST(path_2)
    size_1 = default_tree_size(reduce_ast1, CustomNode.get_children)
    size_2 = default_tree_size(reduce_ast2, CustomNode.get_children)
    print('-------AST--------')
    print(size_1)
    visualizeAST(reduce_ast1, 0)
    print('-' * 20)
    print(size_2)
    visualizeAST(reduce_ast2, 0)

    print('-------Sequences--------')
    sequence_1 = traverseAST(reduce_ast1)
    sequence_2 = traverseAST(reduce_ast2)

    print(sequence_1)
    print(sequence_2)
