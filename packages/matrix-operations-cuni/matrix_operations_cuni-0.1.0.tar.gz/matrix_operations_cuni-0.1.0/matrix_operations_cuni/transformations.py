from matrix_operations_cuni.core import Matrix


class Transformations(Matrix):
    """
    Default class for matrix transformations.
    These are the operations which take only single matrix as an input.
    """

    def transpose(self):
        """
        Transposes the matrix.
        :return: Transposed matrix.
        """
        transposed = []
        for c_index in range(self.cols):
            new_row = []
            for r_index in range(self.rows):
                new_row.append(self[r_index, c_index])
            transposed.append(new_row)
        return Matrix(transposed)

    def find_nonzero_row(self, r_pivot_index, col):
        """
        Finds index of the first row in a given column that
        contains a non-zero element.
        :param r_pivot_index: From which row to find the index.
        :param col: At which column find the index.
        :return: Index of the found row (if exists, else None).
        """
        for r_index in range(r_pivot_index, self.rows):
            if self[r_index, col] != 0:
                return r_index
        return None

    def row_swap(self, r_index1, r_index2):
        """
        Swaps 2 rows.
        :param r_index1: First row to swap.
        :param r_index2: Second row to swap.
        """
        matrix_copy = [row.copy() for row in self]
        matrix_copy[r_index1], matrix_copy[r_index2] = (
            matrix_copy[r_index2],
            matrix_copy[r_index1],
        )
        self.data = matrix_copy

    def zero_below_pivot(self, row_pivot, col_pivot):
        """
        Zeroes all elements below the pivot.
        :param row_pivot: Row with the pivot.
        :param col_pivot: Column with the pivot.
        """
        pivot = self[row_pivot, col_pivot]
        for r_index in range(row_pivot + 1, self.rows):
            factor = self[r_index, col_pivot] / pivot
            for c_index in range(self.cols):    # subtract the factor* row with pivot
                self.data[r_index][c_index] -= factor * self[row_pivot, c_index]

    def ref(self):
        """
        Transforms the matrix into row echelon form.
        :return: Matrix in its row echelon form.
        """
        row_with_pivot = 0
        for c_index in range(self.cols):
            nonzero_row = self.find_nonzero_row(row_with_pivot, c_index)
            if nonzero_row is not None:
                self.row_swap(row_with_pivot, nonzero_row)
                self.zero_below_pivot(row_with_pivot, c_index)
                row_with_pivot += 1
        return self

    def pivot_to_one(self, row_pivot, col_pivot):
        """
        Sets pivot element to 1 and appropriately modifies the rest of the row
        :param row_pivot: Row with the pivot.
        :param col_pivot: Column with the pivot.
        """
        pivot = self[row_pivot, col_pivot]
        old_row = self[row_pivot]
        new_row = []
        for element in old_row:
            new_row.append(element / pivot)
        matrix_copy = [row.copy() for row in self]
        matrix_copy[row_pivot] = new_row
        self.data = matrix_copy

    def zero_above_pivot(self, row_pivot, col_pivot):
        """
        Zeroes all elements above the pivot.
        :param row_pivot: Row with the pivot.
        :param col_pivot: Column with the pivot.
        """
        pivot = self[row_pivot, col_pivot]
        for r_index in range(row_pivot - 1, -1, -1):
            factor = self[r_index, col_pivot] / pivot
            for c_index in range(self.cols):
                self.data[r_index][c_index] -= factor * self[row_pivot, c_index]

    def rref(self):
        """
        Transforms the matrix into reduced row echelon form.
        :return:
        """
        self.ref()
        for r_index in range(self.rows):
            c_index = 0
            while (c_index < self.cols) and (self[r_index, c_index] == 0):
                c_index += 1    # while we don't find pivot
            if c_index < self.cols: # we found one
                self.pivot_to_one(r_index, c_index)
                self.zero_above_pivot(r_index, c_index)
        return self

    def is_regular(self):
        """
        Checks regularity of the matrix.
        :return: True if regular, False if not.
        """
        if self.cols != self.rows:
            return False
        matrix_copy = Transformations([row[:] for row in self.data])
        matrix_copy.rref()
        for index in range(matrix_copy.rows):
            if matrix_copy[index, index] != 1:
                return False
        return True

    def inverse(self):
        """
        Finds the inverse of the given matrix.
        :return: Inverse matrix, if exists, else ValueError.
        """
        if not self.is_regular():
            raise ValueError("Matrix must be regular to calculate the inverse.")
        expanded = [row[:] for row in self.data]    # copying elements
        for r_index in range(self.rows):    # appending regular matrix
            for c_index in range(self.cols):
                if c_index == r_index:
                    expanded[r_index].append(1)
                else:
                    expanded[r_index].append(0)
        augmented_matrix = Transformations(expanded)
        augmented_matrix.rref()
        inverse_matrix = []
        for r_index in range(self.rows):    # slicing, so only portion behind rref is appended
            inverse_matrix.append(augmented_matrix[r_index][self.cols:])
        return Matrix(inverse_matrix)

    def trace(self):
        """
        Calculates the trace of the matrix.
        :return: Sum of the elements on the main diagonal.
        """
        if self.rows != self.cols:
            raise ValueError("Matrix must be square to calculate the trace.")
        return sum(self[index, index] for index in range(self.rows))


if __name__ == "__main__":
    testMatica1 = Transformations(
        [[2, 2, 3, 1, 0, 0], [1, 3, 4, 0, 1, 0], [1, 1, 1, 0, 0, 1]]
    )
    testMatica1.rref().pretty_print()
    testMatica = Transformations([[2, 2, 3], [1, 3, 4], [1, 1, 1]])
    testMatica.inverse().pretty_print()
    print(testMatica1.inverse())
    # testMatica.inverse().pretty_print()
