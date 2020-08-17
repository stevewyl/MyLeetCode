
def numSquares(n: int) -> int:

    def gen_squares(n):
        cur_squre = 1
        num = 1
        squares = [cur_squre]
        while True:
            num += 1
            square = num ** 2
            if square > n:
                return squares
            squares.append(square)