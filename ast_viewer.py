import clang.cindex
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_file', type=str, default='test_data/test_1.cpp', help="input file C++")

args = parser.parse_args()

function_calls = []  # List of AST node objects that are function calls
function_declarations = []  # List of AST node objects that are fucntion declarations

file_path = args.input_file


# Traverse the AST tree
def trimClangNodeName(nodeName):
    ret = str(nodeName)
    ret = ret.split(".")[1]
    return ret


def parse_binary_op(cursor):
    # assert cursor.kind == clang.cindex.CursorKind.BINARY_OPERATOR
    children_list = [i for i in cursor.get_children()]
    assert len(children_list) == 2
    left_offset = len([i for i in children_list[0].get_tokens()])
    op = [i for i in cursor.get_tokens()][left_offset].spelling
    return op


def printASTNode(node, level):
    for i in range(0, level-1):
        print('  ', end="")
    if node.kind == clang.cindex.CursorKind.BINARY_OPERATOR or node.kind == clang.cindex.CursorKind.COMPOUND_ASSIGNMENT_OPERATOR:
        binaryOp = parse_binary_op(node)
        print(f'+--{node.kind.name}  {binaryOp}  {node.type.kind}')
    else:
        print(f'+--{node.kind.name}  {node.spelling}  {node.type.kind}')


def traverseAST(node, level):
    if node is not None:
        level = level + 1
        if level == 1 or (node.location.file and node.location.file.name == file_path):
            printASTNode(node, level)
        # Recurse for children of this node
        for childNode in node.get_children():
            traverseAST(childNode, level)
        level = level - 1


# Tell clang.cindex where libclang.dylib is
# clang.cindex.Config.set_library_path("/usr/lib/llvm-6.0/lib/")
index = clang.cindex.Index.create()

# Generate AST from filepath passed in the command line
tu = index.parse(file_path, ['-x', 'c++', '-std=c++11', '-D__CODE_GENERATOR__'])

root = tu.cursor  # Get the root of the AST
traverseAST(root, 0)
