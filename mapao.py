def bubble(list_a):
    for n in range(len(list_a)-1):
        for m in range(len(list_a)-1-n):
            if list_a[m]>list_a[m+1] :
                list_a[m],list_a[m+1]= list_a[m+1],list_a[m]
            print(list_a)

list_a = [2,1,6,4,7,5]
bubble(list_a)