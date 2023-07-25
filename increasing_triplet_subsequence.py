'''
Wrong Anser!!!!!!!!!!!!!!!!!
这他娘的不是跟原list一样的吗？ 
index 和 value，一个单调增，另一个任意。相邻指数或值单调无法判断
要i 的 all left 和 all right 比较才行。 
'''
def increasingTriplet(nums):
        
        n = len(nums)
        pair = sorted((value, index) for index, value in enumerate(nums))
        print(pair)
        for i in range(1, n-1):
            if pair[i][1] > pair[i-1][1] and pair[i][1] < pair[i+1][1]:
                return True
        
        return False

my_list = [2,1,5,0,4,6]
result = increasingTriplet(my_list)
print(result)
print(sorted([(5,0),(4,1),(3,2)]))