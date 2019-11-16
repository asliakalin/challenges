"""
Given a binary search tree, find the kth smallest element.
"""

def kthSmallest(root, k):
	if root == None:
		return False
	elif k <= 0:
		return False
	else:
		ordered = []
		inOrder(root, k, ordered)
		return ordered[k-1]


def inOrder(root, k, arr):
	if root == None or k >= len(arr):
		return
	elif root.left == None and root.right == None:
		arr.append(root.val)
		return
	else:
		inOrder(root.left)
		arr.append(root.val)
		inOrder(root.right)