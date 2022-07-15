from binarytree import tree
  
  
# Create a random binary 
# tree of any height
root = tree()
print("Binary tree of any height :")
print(root)
  
# Create a random binary 
# tree of given height
root2 = tree(height = 2)
print("Binary tree of given height :")
print(root2)
  
# Create a random perfect 
# binary tree of given height
root3 = tree(height = 2,
             is_perfect = True)
print("Perfect binary tree of given height :")
print(root3)