# import math
# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]
# l3 = []
# c = 0
# s = 0


# def numb(lst):
#     a = len(lst)
#     n = 0 
#     for i in range (0,a):
#         n = n + math.pow(10,i)*lst[i]
#     return n 
    
# s = numb(l1) + numb(l2)
# while s != 0:
#     l3.append(int(s%10))
#     s = int(s/10)


lst = [1,4,7,8,9,8]

class Single:
    
    def __init__ (self, val, next = None):
        self.val = val
        self.next = next
        
    # def __str__(self):
    #     return str(self.val)
    


def lst2link(lst):
    curr = dummy  = Single(0)
    for e in lst:
        curr.next = Single(e)
        curr = curr.next
    return dummy.next    

# def display(head):
#     curr = head
#     e = []
#     while curr:
#         e.append(str(curr.val))
#         curr = curr.next
#         print(" -> ".join(e))
        

# print(display(lst2link(lst)))

