def solution(n):
    number = n**(1/2)
    if number== int(number):
        return (number+1)**2
    else:
        return -1
