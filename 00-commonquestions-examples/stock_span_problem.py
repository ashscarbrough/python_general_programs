''' Python3 program for a linear time solution for stock span problem using stack '''


def calculateSpan(a, n):
    s = []
    ans = []
    for i in range(0, n):

        while(s != [] and a[s[-1]] <= a[i]):
            s.pop()

        if(s == []):
            ans.append(i+1)

        else:
            top = s[-1]
            ans.append(i - top)

        s.append(i)

    return ans

# A utility function to print elements
# of array


def printArray(arr, n):

    for i in range(n):
        print(arr[i], end=' ')
    print()


# Driver code
price = [10, 4, 5, 90, 120, 80]
n = len(price)
ans = calculateSpan(price, n)

# Print the calculated span values
printArray(ans, n)
