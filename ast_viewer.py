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


def printASTNode(node, level):
    for i in range(0, level-1):
        print('|  ', end="")

    print(f'|--{trimClangNodeName(node.kind)}  {node.spelling}')


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
