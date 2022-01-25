def maximal(num):
    arr=[]
    output = []

    count=0
    maxnum=0

    for i in range(num):
        inp=int(input(f"enter the index element no { i }"))
        arr.append(inp)
    print("**You entered elements*\n",arr)
    for item in arr:
        while (item) %2==0:
            item /=2
            count=count+1
        output.append(int(item))
    output.sort()
    store = max(output)
    print("after divide by 2 and sorted list is =\n",output)
    lastindex=len(output)
    while count>0:

        store=store*2
        count = count - 1
    output[lastindex-1]=store

    for item in output:
        maxnum=maxnum+item
    print("maximum Number after sum of item which is divide by 2 and multiply by twice of its largest no while as long as counter\n",maxnum)
if __name__ == '__main__':
    print("Enter How many elements U want to be check for  =\n")
    size=int(input())
    maximal(size) 