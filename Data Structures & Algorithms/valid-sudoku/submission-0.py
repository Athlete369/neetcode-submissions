class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])
        row_hash_set = [set() for i in range(m)]
        column_hash_set = [set() for i in range(n)]
        subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(0,m):
            for j in range(0,n):
                num = board[i][j]
                if num != ".":
                    # print(num)
                    num = int(num)
                    if num not in row_hash_set[i]:
                        row_hash_set[i].add(num)
                    else:
                        return False

                    if num not in column_hash_set[j]:
                        column_hash_set[j].add(num)
                    else:
                        return False

                    if num not in subgrid_sets[int(i / 3)][int(j / 3)]:
                        subgrid_sets[int(i / 3)][int(j / 3)].add(num)
                    else:
                        return False
        return True
