def binSearch(A, x):
    begin = 0
    end = len(A)-1
    result = -1
    while(begin <= end):
        mid = (begin+end)/2
        if(A[mid] <= x):
            begin = mid + 1
            result = mid
        else:
            end = mid - 1

    return result


def main():
    res = binSearch([1,2,3,4],4)
    print(res)


if __name__ == "__main__":
    main()
