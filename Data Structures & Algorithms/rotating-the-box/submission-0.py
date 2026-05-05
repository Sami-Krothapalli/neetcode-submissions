class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])

        for row in boxGrid:
            write = n - 1
            for read in reversed(range(n)):
                if row[read] == "*":
                    write = read - 1 
                elif row[read] == '#':
                    row[read], row[write] = '.', '#'
                    write -= 1
        
        return [[boxGrid[r][c] for r in reversed(range(m))] for c in range(n)]
        


        