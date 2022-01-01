# Difference Between pivot and pivot_table

- pivot_table = It is generalization of **pivot** that can handle duplicate values for one pivoted index/column pair. Specifically, you can give pivot_table a list of aggregation function using keyword argument aggfunc. The default aggfunc of pivot_table is np.mean
- Syntax - Dataframe.pivot_table(values, index, columns, aggfunc, fill_value, margind, dropna, margins_name = 'All', observed, sort)
   - **values** - column to aggregate, optional
   - **index** - mostly the rows you want to display or analyze
   - **columns** - To group by pivot table column 
   - **aggfunc** - to get the values filled based on the function specified. such as np.mean,np.sum etc.
   - **fill_vale** - Vale to replace missing values with (in the resulting pivot table, after aggregation)
   - **margins** - Add all row / column (e.g. for subtotal/ grand totals) by defaut in it is boolean variable with False as its value
   - **margins_name - String variable with default value as "All". Name of the row / column that will contain the totals when margins is True.
   - **dropna** - bool, default True Do not Include columns whose entries are all NaN
   - **observed** - bool, default False. It applies for categorical data. 
                   - If true: Only show observed values for categorical groupers. 
                   - If false: show all values for categorical groupers
    - **sort** - bool, default True Specifies, if the result should be sorted.
   
 - pivot(index = None, columns =None, values = None)
   - it 's almost same as pure function but without any aggregated values, so it just display the row, columns and values needed. 

