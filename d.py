class Node :
    def __init__ (self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
class Tree :
    def __init__(self,root=None):
        self.root=root
    def insert(self,item):
        new_node =Node (item)
        temp=self.root
        if not self.root :
            self.root=new_node
        while temp:
          if new_node.value< self.root.value :
              if temp.left==None:
                  temp.left=new_node
          else:
              if temp.right==None: 
                  temp.right=new_node
            

         
    

    