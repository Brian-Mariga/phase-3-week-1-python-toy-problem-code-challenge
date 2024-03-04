def solution(N):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    full_cycles = N // 26
    
    result += alphabet * full_cycles

    # print(remainder)
    remainder = N % 26
        
    result += alphabet[:remainder]
    
    # print(result)
    return result

solution(5)
