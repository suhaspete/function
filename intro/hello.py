class Solution:
    def generate(self, numRows: int) :
        i = 1
        lst = [[1]]
        j = 0
        while(i<numRows):
            temp = [1]
            for k in range(0,i-1):
                temp.append(lst[j][k] + lst[j][k+1])
            temp.append(1)
            lst.append(temp)
            i += 1
            j += 1
            print(lst)
        return lst
                    