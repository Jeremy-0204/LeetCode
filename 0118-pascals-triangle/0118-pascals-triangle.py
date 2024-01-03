class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        # Initialize Pascal's triangle with the first row
        pascal = [[1]]
        
        # Iterate through each row starting from the second row
        for i in range(1, numRows):
            prev_row = pascal[i-1]  # Get the previous row
            current_row = [1]  # The first element of each row is always 1
            
            # Iterate through each element in the current row (except the first and last)
            for j in range(1, i):
                # Calculate the current element by summing the corresponding elements from the previous row
                current_row.append(prev_row[j-1] + prev_row[j])
            
            current_row.append(1)  # The last element of each row is always 1
            pascal.append(current_row)  # Add the current row to Pascal's triangle
        
        return pascal