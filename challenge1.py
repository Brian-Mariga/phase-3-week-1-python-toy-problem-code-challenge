def solution(A):
    moves =0
    total_moves = 0
    N =len(A)
    available_bricks = sum(A)
    # print(available_bricks)
    required_bicks = N*10

    if available_bricks != required_bicks:
        # print("Can't do")
        return -1
    else:
        # print("Can do")
        avg_bricks_per_box = available_bricks // N
        # print(avg_bricks_per_box)
        for bricks in A:
            difference = avg_bricks_per_box - bricks
            total_moves += difference

            moves +=abs(total_moves)
            # print(moves)
            # if difference > 0:
            #     moves += difference
            # elif difference <0:
                # moves -= difference
        print(int(moves))
        return int(moves)

solution([7, 15, 10, 8])