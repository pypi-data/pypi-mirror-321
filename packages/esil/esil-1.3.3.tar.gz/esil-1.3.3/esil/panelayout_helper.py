'''
Author: Devin
Date: 2024-03-09 11:11:25
LastEditors: Devin
LastEditTime: 2024-04-22 22:21:15
FilePath: \PythonDemo\esil\PaneLayout.py
Description: 

Copyright (c) 2024 by Devin, All Rights Reserved. 
'''

# Description: This is a python script to calculate the number of columns and rows for the pane layout.
#description: Define the auto layout options for the pane layout.
class PaneLayout():
    # Layout the pane with a square grid: The number of panes in the row and column are the same.
    ForceSquare = 1
    # Layout the pane with a square grid: The number of panes in the row and column are the same. If the number of panes is not a perfect square, the number of panes in the row is one less than the number of panes in the column.
    SquareColPreferred = 2
    # Layout the pane with a square grid: The number of panes in the row and column are the same. If the number of panes is not a perfect square, the number of panes in the column is one less than the number of panes in the row.
    SquareRowPreferred = 3
    # Layout the pane with a single row: The number of panes in the row is 1 and the number of panes in the column is the same as the number of panes.
    SingleRow = 4
    # Layout the pane with a single column: The number of panes in the row is the same as the number of panes and the number of panes in the column is 1.
    SingleColumn = 5
    # Layout the pane with an explicit number of columns: The first row has 1 column and the second row has 2 columns for a total of 3 panes.
    ExplicitCol12 = 6
    # Layout the pane with an explicit number of columns: The first row has 2 columns and the second row has 1 column for a total of 3 panes.
    ExplicitCol21 = 7
    # Layout the pane with an explicit number of columns: The first row has 2 columns and the second row has 3 columns for a total of 5 panes.
    ExplicitCol23 = 8
    # Layout the pane with an explicit number of columns: The first row has 3 columns and the second row has 2 columns for a total of 5 panes.
    ExplicitCol32 = 9
    # Layout the pane with an explicit number of rows: The first column has 1 row and the second column has 2 rows for a total of 3 panes.
    ExplicitRow12 = 10
    # Layout the pane with an explicit number of rows: The first column has 2 rows and the second column has 1 row for a total of 3 panes.
    ExplicitRow21 = 11
    # Layout the pane with an explicit number of rows: The first column has 2 rows and the second column has 3 rows for a total of 5 panes.
    ExplicitRow23 = 12
    # Layout the pane with an explicit number of rows: The first column has 3 rows and the second column has 2 rows for a total of 5 panes.
    ExplicitRow32 = 13
    ExplicitRow34 =14

#description: 根据count和panel_layout返回col和row
#param count: int
#param panel_layout: PaneLayout,可以是整数，元组，或者None, tuple, None, default None
#return: col(int), row(int)
def get_layout_col_row(count, panel_layout=None):
    '''
    @description: 根据count和panel_layout返回col和row
    @param count: int
    @param panel_layout: PaneLayout,可以是整数，元组，或者None, tuple, None, default None
    @return: col(int),row(int)
    '''
    if count != 0:        
        if isinstance(panel_layout, tuple):#如果是元组，直接返回
            col,row=panel_layout
        else:
            num = int((count ** 0.5) + 0.9999999)
            if panel_layout == PaneLayout.ForceSquare:
                row = num
                col = num
            elif panel_layout == PaneLayout.SquareColPreferred:
                row = num
                if count <= num * (num - 1):
                    row -= 1               
            elif panel_layout == PaneLayout.SquareRowPreferred:
                row = num
                col = num
                if count <= num * (num - 1):
                    col -= 1
            elif panel_layout == PaneLayout.SingleRow:
                row = 1
                col = count
            elif panel_layout == PaneLayout.SingleColumn:
                row = count
                col = 1       
            elif panel_layout == PaneLayout.ExplicitCol12:
                col = 1
                row = 2
            elif panel_layout == PaneLayout.ExplicitCol21:   
                col = 2
                row = 1
            elif panel_layout == PaneLayout.ExplicitCol23:
                col = 2
                row = 3
            elif panel_layout == PaneLayout.ExplicitCol32:
                col = 3
                row = 2
            elif panel_layout == PaneLayout.ExplicitRow12:
                row = 1
                col = 2
            elif panel_layout == PaneLayout.ExplicitRow21:
                row = 2
                col = 1
            elif panel_layout == PaneLayout.ExplicitRow23:
                row = 2
                col = 3
            elif panel_layout == PaneLayout.ExplicitRow32:
                row = 3
                col = 2 
            elif panel_layout == PaneLayout.ExplicitRow34:
                row = 3
                col = 4 
            elif panel_layout == None and count in (2,3,5,7):   
                row = 1
                col = count         
            else:#include none and others                  
                while count % num != 0 and num > 1:
                    num -= 1  
                if num >1:
                    row = num
                    col = count//num 
                else: 
                    num = int((count ** 0.5) + 0.9999999)                
                    row = num
                    col = num  
                    if count <= num * (num - 1):
                        row -= 1 
        return col, row

if __name__ == '__main__':
    count = 8
    pane_layout = PaneLayout.ForceSquare    
    col,row= get_layout_col_row(count, pane_layout)
    print(col, row)
    
    col1,row1= get_layout_col_row(count, None)
    print(col1, row1)
    col2,row2= get_layout_col_row(count, (4,2))
    print(col2, row2)
    col3,row3= get_layout_col_row(count, (3,3))
    print(col3, row3)
    col4,row4= get_layout_col_row(count, 5)
    print(col4, row4)
 