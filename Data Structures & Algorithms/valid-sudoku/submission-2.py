class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def general_validation(li):
            traverse = []

            if len(li) != 9:
               return False

            for num in li:

                if num not in [".","1","2","3","4","5","6","7","8","9"]:
                    return False
                if num in traverse:
                    return False
                if num != ".":
                    traverse.append(num)

            return True


        # check each raw
        for i in range(9):
            result = general_validation(board[i])
            if not result:
                return False
        
        for i in range(9):
            check_list = [board[j][i] for j in range(9)]
            result = general_validation(check_list)
            if not result:
                return False

        
        combinations = [
            [0, 3, 0, 3],
            [3, 6, 0, 3],
            [6, 9, 0, 3],

            [0, 3, 3, 6],
            [3, 6, 3, 6],
            [6, 9, 3, 6],

            [0, 3, 6, 9],
            [3, 6, 6, 9],
            [6, 9, 6, 9],

            ]
        
        for combination in combinations:
            check_list = []
            # check each 3 * 3 box
            for i in range(combination[0], combination[1]):
                for j in range(combination[2], combination[3]):
                    check_list.append(board[i][j])
            result = general_validation(check_list)
            if not result:
                return False
        
        return True