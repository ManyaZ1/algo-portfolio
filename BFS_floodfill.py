#floodfill
def floodFill(img, row, col, p):
    start = img[row][col]  # Get the starting value (color)
    queue = [(row, col)]   # Initialize the queue with the starting cell
    visited = set()        # Create a set to track visited cells

    while len(queue) > 0:  # Continue until the queue is empty
        row, col = queue.pop(0)  # Get the current cell from the queue
        visited.add((row, col))  # Mark the current cell as visited
        img[row][col] = p        # Fill the current cell with the new value

        # Check the neighbors of the current cell
        for row, col in neighbors(img, row, col, start):
            if (row, col) not in visited:  # Only process unvisited neighbors
                queue.append((row, col))   # Add the valid neighbor to the queue
def neighbors(img, row, col, start):
    indices = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    return [(row, col) for row, col in indices if isValid(img, row, col) and img[row][col] == start]

def isValid(img, row, col):
    return row >= 0 and col >= 0 and row < len(img) and col < len(img[0])
#bfs rec vs loop to check if two trees are the same
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = deque([(p, q)])  # Use a stack to hold pairs of nodes
        
        while stack:
            node1, node2 = stack.pop()
            
            # If both are None, continue checking other nodes
            if not node1 and not node2:
                continue
            
            # If one is None and the other isn't, or their values differ
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # Add left and right children pairs to the stack for further comparison
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
        
        return True  # All nodes were the same
#recursion:
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, trees are the same
        if not p and not q:
            return True
        # If one is None and the other isn't, or their values differ, trees are not the same
        if not p or not q or p.val != q.val:
            return False
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
