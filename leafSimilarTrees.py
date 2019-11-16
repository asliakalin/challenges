"""
The values of leaves in a binary tree from left to right form a leaf value sequence.
If two trees have the same leaf sequences, then they are leaf similar tree.
Here is a function that return true if two given trees are leaf similar, otherwise returns false.
"""


def leafSimilar(root1, root2):
	leaves1 = []
	leaves2 = []
	dfsPick(root1, leaves1)
	dfsPick(root2, leaves2)
	return compare(leaves1, leaves2)


def dfsPick(root, leaves):
	if root==None:
		return leaves
	elif root.left == None and root.right == None:
		leaves.append(root.val)
		return
	else:
		dfsPick(root.left, leaves)
		dfsPick(root.right, leaves)


def compare(one, other):
	if len(one) != len(other):
		return False
	elif one == [] and other == []:
		return True
	else:
		if one[0] != other[0]:
			return False
		else:
			return compare(one[1:], other[1:])
