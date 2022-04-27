import clang.cindex
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_file', type=str, default='test_data_2/test_11.cpp', help="input file C++")

args = parser.parse_args()

function_calls = []  # List of AST node objects that are function calls
function_declarations = []  # List of AST node objects that are fucntion declarations

file_path = args.input_file
tree_line_arr = []

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


def printASTNode(node, level, is_last_child):
    global tree_line_arr
    tree_line_str = ""
    for i in range(0, level-1):
        tree_line_str += '   '

    if is_last_child:
        prefix_str = '└──'
    else:
        prefix_str = '├──'

    if node.kind == clang.cindex.CursorKind.BINARY_OPERATOR or node.kind == clang.cindex.CursorKind.COMPOUND_ASSIGNMENT_OPERATOR:
        binaryOp = parse_binary_op(node)
        tree_line_str += (f'{prefix_str}{node.kind.name} {binaryOp} {node.type.spelling} [line={node.location.line}, col={node.location.column}]')
    else:
        tree_line_str += (f'{prefix_str}{node.kind.name} {node.spelling} {node.type.spelling} [line={node.location.line}, col={node.location.column}]')

    tree_line_arr.append(tree_line_str)

    # Xu ly ky tu
    idx = 0;
    tree_line_qty_of_char = len(tree_line_arr)
    for tmp_line in reversed(tree_line_arr):
        if idx == 0:
            idx += 1
            continue

        tmp_line_str = list(tmp_line)
        tmp_line_char_pos = 3 * (level - 1)
        tmp_line_char = tmp_line_str[tmp_line_char_pos];
        if(tmp_line_char != " " or tmp_line_char == "├" or tmp_line_char == "└"):
             break

        tmp_line_str[tmp_line_char_pos] = "│"
        tree_line_arr[tree_line_qty_of_char - 1 - idx] = "".join(tmp_line_str)
        idx += 1

def traverseAST(node, level, is_last_child):
    list_parent_level = []
    if node is not None:
        level = level + 1
        if level == 1 or (node.location.file and node.location.file.name == file_path):
            printASTNode(node, level, is_last_child)
        # Recurse for children of this node
        count_children = len(list(node.get_children()))
        j = 0
        for childNode in node.get_children():
            list_parent_level.append(level)
            j = j + 1
            traverseAST(childNode, level, j == count_children)
        level = level - 1


# Tell clang.cindex where libclang.dylib is
# clang.cindex.Config.set_library_path("/usr/lib/llvm-6.0/lib/")
index = clang.cindex.Index.create()

# Generate AST from filepath passed in the command line
tu = index.parse(file_path, ['-x', 'c++', '-std=c++11', '-D__CODE_GENERATOR__'])

root = tu.cursor  # Get the root of the AST
traverseAST(root, 0, False)

# print result
print("\n".join(tree_line_arr))
