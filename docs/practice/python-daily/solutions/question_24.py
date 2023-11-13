class list:


    def __init__(self,matrix):
        self.matrix: [list] = matrix
        self.output = []



        for i in self.matrix:
            for j in i:
                self.output.append(j)
        print(self.output)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
list1 = list(matrix)