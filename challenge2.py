def solution(A):
    digit_sums = {}
    max_sum = -1

    for num in A:
        digit_sum = sum(int(digit) for digit in str(num))
    
        if digit_sum in digit_sums:
            max_sum = max(max_sum, num + digit_sums[digit_sum])
        else:
            digit_sums[digit_sum] = num
    return max_sum

print(solution([51, 32, 43]))