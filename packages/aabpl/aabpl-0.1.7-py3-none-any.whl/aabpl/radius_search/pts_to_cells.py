from numpy import (
    array as _np_array,
    append as _np_append,
    zeros as _np_zeros,
    unique as _np_unique, 
    concatenate as _np_concatenate,
    equal as _np_equal, 
    logical_or as _np_logical_or, 
    all as _np_all, 
    sort as _np_sort
)
from pandas import (DataFrame as _pd_DataFrame, cut as _pd_cut, concat as _pd_concat) 
from aabpl.utils.general import arr_to_tpls
from aabpl.testing.test_performance import time_func_perf
# from aabpl.doc.docstrings import fixdocstring


################ assign_points_to_cells ######################################################################################
# @fixdocstring
@time_func_perf
def assign_points_to_cells(
    grid:dict,
    pts_df:_pd_DataFrame,
    y:str='lat',
    x:str='lon',
    row_name:str='id_y',
    col_name:str='id_x',
    silent:bool = False,
) -> _pd_DataFrame:
    """
    # TODO Move to class and Properly describe.
    # TODO it modifies pts_df AND grid?
    Modifies input pandas.DataFrame grid and pts_df: 
    sorts by 1) y coordinate and 2) by x coordinate

    Args:
    <y>
    
    Returns:
    gridcell_id_name: name to be appended in pts_df to indicate gridcell. If False then information will not be stored in pts_df 
    """
    # TO Do this might be significantly faster when looping through pts_df instead of through cells
    pts_df.sort_values([y, x], inplace=True)

    # . 
    row_ids = grid.row_ids
    col_ids = grid.col_ids
    # get vectors of row columns boundary values
    x_steps = grid.x_steps
    y_steps = grid.y_steps
    # store len and digits for index
    id_y_mult = grid.id_y_mult
    len_pts_df = len(pts_df)
    
    if not silent:
        print(
            'Aggregate Data from '+str(len_pts_df)+' points'+
            ' into '+str(len(y_steps))+'x'+str(len(x_steps))+
            '='+str(len(y_steps)*len(x_steps))+' cells.' 
        )

    # to do change to cut
    # for each row select relevant points, then refine selection with columns to obtain cells
    pts_df[row_name] = _pd_cut(
        x = pts_df[y],
        # bins = y_steps[::-1],
        # labels = row_ids[::-1],
        bins = y_steps,
        labels = row_ids,
        include_lowest = True
    ).astype(int)
    
    pts_df[col_name] = _pd_cut(
        x = pts_df[x],
        bins = x_steps,
        labels = col_ids,
        include_lowest = True
    ).astype(int)
    
    
    return pts_df[[row_name, col_name]]

@time_func_perf
def aggregate_point_data_to_cells(
    grid:dict,
    pts_df:_pd_DataFrame,
    sum_names:list=['employment'],
    row_name:str='id_y',
    col_name:str='id_x',
    silent = False,
) -> _pd_DataFrame:
    """
    TODO
    """
    # initialize dicts for later lookups )
    sums_zero = _np_zeros(len(sum_names),dtype=int)
    cells_containing_pts = arr_to_tpls(_np_unique(pts_df[[row_name, col_name]],axis=0),int)
    grid.id_to_pt_ids = {pt_row_col:_np_array([],dtype=int) for pt_row_col in cells_containing_pts}
    grid.id_to_sums = {pt_row_col:sums_zero for pt_row_col in cells_containing_pts}
    # grid.id_to_sums = {g_id:sums_zero for g_id in grid.ids} 
    grid.pt_id_to_row_col = {}
    
    # TODO this could be also done in batches of points belonging to a single cell
    for pt_id, pt_row_col,pt_vals in zip(
        pts_df.index, 
        arr_to_tpls(pts_df[[row_name, col_name]].values,int), 
        pts_df[sum_names].values
        ):
        grid.id_to_pt_ids[pt_row_col] = _np_append(grid.id_to_pt_ids[pt_row_col], pt_id)
        grid.id_to_sums[pt_row_col] = grid.id_to_sums[pt_row_col]+pt_vals
        grid.pt_id_to_row_col[pt_id] = pt_row_col

        #
    #
    if not silent:
        print(
            'Points assigned to grid cell:'+
            str(len(pts_df.index) - _np_logical_or(pts_df[col_name]==-1, pts_df[row_name]==-1).sum())+
            '/'+str(len(pts_df.index))
        )
        print('sum in grid:', _np_array([x for x in grid.id_to_sums.values()]).sum(axis=0), 'sum in pts_df', pts_df[sum_names].values.sum(axis=0))
    #
    return 
#