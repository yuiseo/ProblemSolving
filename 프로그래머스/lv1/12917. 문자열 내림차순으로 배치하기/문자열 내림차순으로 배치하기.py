def solution(s):
    arr = list(map(str,s))
    arr.sort(reverse=True)
    return ('').join(arr)