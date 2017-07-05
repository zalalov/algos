class TreeNode(object):
    """
    Tree node class
    """
    def __init__(self, value=None):
        """
        Constructor
        :param value:
        """
        self.left = None
        self.right = None
        self.value = value


def lowest_common_ancestor(root, node1, node2):
    result = [False, False]

    if root.value == node1.value:
        result[0] = True

    if root.value == node2.value:
        result[1] = True

    if root.left:
        left_res = lowest_common_ancestor(root.left, node1, node2)

        if isinstance(left_res, TreeNode):
            return left_res
        else:
            result = result[0] or left_res[0], result[1] or left_res[1]

    if root.right:
        right_res = lowest_common_ancestor(root.right, node1, node2)

        if isinstance(right_res, TreeNode):
            return right_res
        else:
            result = result[0] or right_res[0], result[1] or right_res[1]

    return root if result[0] and result[1] else result


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n4.left = n7
    n4.right = n8

    res = lowest_common_ancestor(n1, n6, n8)
    print(res.value)
