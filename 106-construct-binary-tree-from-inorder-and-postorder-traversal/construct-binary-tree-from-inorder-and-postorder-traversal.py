
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_map = {value: i for i, value in enumerate(inorder)}
        post_idx = len(postorder) - 1

        def build(left, right):
            nonlocal post_idx

            if left > right:
                return None

            root_val = postorder[post_idx]
            post_idx -= 1

            root = TreeNode(root_val)

            mid = index_map[root_val]

            # Build right subtree first
            root.right = build(mid + 1, right)

            # Build left subtree
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)
