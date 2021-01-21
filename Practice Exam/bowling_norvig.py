'''Peter Norvig's two solutions to computing the score for a player's game of bowling'''

def bowling(balls):
    "Compute the total score for a player's game of bowling."
    ## bowling([int, ...]) -> int
    total = 0
    for frame in range(10):
        score, balls = score_frame(balls)
        total += score
    return total

def score_frame(balls):
    "Return two values: (score_for_this_frame, remaining_balls)."
    n_used, n_scoring = ((1, 3) if balls[0] == 10 # strike
                    else (2, 3) if balls[0] + balls[1] == 10 # spare
                    else (2, 2)) # open frame
    return (sum(balls[:n_scoring]), balls[n_used:])


def bowling2(balls):
    "Compute the score for one player's game of bowling."
    return sum(score_frame1(balls) for frame in range(10))

def score_frame1(balls):
    "Return (score, balls): the score for this frame and the remaining balls."
    n_used, n_scoring = ((1, 3) if balls[0] == 10 # strike
                    else (2, 3) if balls[0] + balls[1] == 10 # spare
                    else (2, 2)) # open frame
    score = sum(balls[:n_scoring])
    balls[:n_used] = []
    return score

def test_bowling():
    assert   0 == bowling([0] * 20)
    assert  20 == bowling([1] * 20)
    assert  80 == bowling([4] * 20)
    assert 190 == bowling([9,1] * 10 + [9])
    assert 300 == bowling([10] * 12)
    assert 200 == bowling([10, 5,5] * 5 + [10])
    assert  11 == bowling([0,0] * 9 + [10,1,0])
    assert  12 == bowling([0,0] * 8 + [10, 1,0])
    assert  20 == bowling([0, 0] * 9 + [10, 10,0])
    assert  30 == bowling([0, 0] * 8 + [10, 10,0])
    assert 168 == bowling([9,1, 0,10, 10, 10, 6,2, 7,3, 8,2, 10, 9,0, 9,1,10])
    assert  24 == bowling([10, 3, 4] + [0] * 17)
    assert 168 == bowling([10, 7,3, 7,2, 9,1, 10, 10, 10, 2,3, 6,4, 7,3,3])
    assert 133 == bowling([1,4, 4,5, 6,4, 5,5, 10, 0,1, 7,3, 6,4, 10, 2,8,6])
    assert  16 == bowling([5,5, 3,0] + [0,0] * 8)
    assert 200 == bowling([5,5] + [10, 5,5] * 5)
    assert  20 == bowling([0,0] * 9 + [10,5,5])