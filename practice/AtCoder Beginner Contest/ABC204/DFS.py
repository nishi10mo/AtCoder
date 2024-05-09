from collections import deque

# 木構造
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 二分木を作成するためのメソッド
def make_tree(tree, node, i, n):
    # tree: 木(リスト)
    # 今見ているノード(TreeNodeクラス)
    # 今見ているノードのインデックス(整数)
    # 木のノード数(整数)
    if n > i:
        if tree[i] is None:
            return None
        node = TreeNode(i)
        node.left = make_tree(tree, node.left, 2*i+1, n)
        node.right = make_tree(tree, node.right, 2*i+2, n)
    return node

tree = [1, 3, 5, 6, 7]
root = make_tree(tree, None, 0, len(tree))
ans = []
stack = deque([root])
while stack:
    node = stack.pop()
    ans.append(node.val)
    if node.right:
        ans.append(node.right.val)
    if node.left:
        ans.append(node.left.val)
print(ans)

