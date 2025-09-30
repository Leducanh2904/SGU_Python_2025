def A(list1):
    list1.append(2*list1[0]) 
    print(list1) 
def B(list2): 
    list2.append(2+list2[1]) 
    ist2 = [] 
    print(list2) 
def C(list1,list2): 
    A(list1) 
    print(list1) 
    print(list2) 
    B(list2) 
    print(list2)