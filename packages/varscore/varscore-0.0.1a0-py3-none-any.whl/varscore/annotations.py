import polars as pl
import pandas as pd
import pybedtools
from typing import List, Tuple


def add_n_closest_elements(variant_scores: pl.DataFrame, elements_file, n_elements, element_label) -> pl.DataFrame:
    """
    Add the n closest elements to each variant in the variant_scores DataFrame.
    Parameters:
    variant_scores (pl.DataFrame): A DataFrame containing variant information with columns 'variant_id', 'chrom', 'start', 'end', etc.
    elements_file (str): Path to a file containing elements to be considered for proximity calculations.
    n_elements (int): The number of closest elements to add for each variant.
    element_label (str): A label to use for the new columns indicating the closest elements and their distances. Example: 'gene'.
    Returns:
    pl.DataFrame: The updated variant_scores DataFrame with additional columns for the closest elements and their distances, such as
    'variant_id', 'closest_gene_1', 'closest_gene_distance_1', 'closest_gene_2', 'closest_gene_distance_2', etc.
    """
    variant_bed = pybedtools.BedTool.from_dataframe(bed_df.to_pandas())
    # Take in the elements file
    element_df = pd.read_table(elements_file, header=None)
    element_bed = pybedtools.BedTool.from_dataframe(element_df)
    # Get the n closest elements to each variant.
    closest_elements_bed = variant_bed.closest(element_bed, d=True, t='first', k=n_elements)

    closest_element_df = pl.from_pandas(closest_elements_bed.to_dataframe(header=None))
    new_cols = []
    if not closest_element_df.is_empty():
        
        closest_element_df = closest_element_df.rename({'5': 'variant_id', '9':'close_element', closest_element_df.columns[-1]: 'element_distance'})
        for col in closest_element_df.columns:
            print(closest_element_df[col])
        closest_element_df = closest_element_df.group_by(pl.col('variant_id'), maintain_order=True).agg(pl.col('close_element'), pl.col('element_distance'))

        for i in range(n_elements):
            new_cols.append(pl.col('close_element').list.get(i, null_on_oob=True).alias(f'closest_{element_label}_{i+1}'))
            new_cols.append(pl.col('element_distance').list.get(i, null_on_oob=True).alias(f'closest_{element_label}_distance_{i+1}'))
        closest_element_df = closest_element_df.with_columns(
            new_cols
        )
        closest_element_df = closest_element_df.drop(['close_element', 'element_distance'])
    else:  
        # Make empty columns if no elements are found.
        closest_element_df = pl.DataFrame(columns=['variant_id'])
        for i in range(n_elements):
            new_cols.append(pl.lit(None).alias(f'closest_{element_label}_{i+1}')),
            new_cols.append(pl.lit(None).alias(f'closest_{element_label}_distance_{i+1}'))
    return variant_scores


def add_closest_elements_in_window(variant_scores: pd.DataFrame, closest_elements_in_window_args: List[Tuple[str, int, str]], bed_df):
    # Add closest elements within a window to the variant_scores dataframe.
    variant_bed = pybedtools.BedTool.from_dataframe(bed_df)
    for elements_file, window_size, element_label in closest_elements_in_window_args:
        element_df = pd.read_table(elements_file, header=None)
        element_bed = pybedtools.BedTool.from_dataframe(element_df)
        closest_elements_bed = variant_bed.window(element_bed, w=window_size)
        closest_element_df = pl.from_pandas(closest_elements_bed.to_dataframe(header=None))
        result_label = f"{element_label}_within_{window_size}_bp"
        if not closest_element_df.is_empty():
            closest_element_df = closest_element_df.rename({'5': 'variant_id', '9': 'close_element'})

            # print(closest_element_df.group_by(pl.col('variant_id')).agg(pl.col('close_element')).n_unique())
            closest_element_df = closest_element_df.group_by(pl.col('variant_id'), maintain_order=True).agg(pl.col('close_element'))
            closest_element_df = closest_element_df.with_columns(
                pl.col('close_element').list.join(';').alias(result_label)
            )

            closest_element_df = closest_element_df.drop('close_element')

        else:
            # Make empty 
            # column if no elements are within the window.
            # TODO convert this to polars
            closest_element_df = pl.DataFrame({
                "variant_id": variant_scores["variant_id"],
                f"{element_label}_within_{window_size}_bp": [""] * len(variant_scores["variant_id"])
            })
        variant_scores = variant_scores.join(closest_element_df, on='variant_id', how='left')
    return variant_scores


