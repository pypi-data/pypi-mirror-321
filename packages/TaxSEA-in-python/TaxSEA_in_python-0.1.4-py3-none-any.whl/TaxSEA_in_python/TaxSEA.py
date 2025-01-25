# TaxSEA: Taxon Set Enrichment Analysis
#
# TaxSEA is designed to enable rapid annotation of changes observed in a
# microbiome association study
# by testing for enrichment for producers of particular metabolites, or
# associations with marker taxa
# for particular diseases. It focuses specifically on human gut
# microbiome #' associations and uses
# a Kolmogorov-Smirnov test to test if a particular set of taxa is
# changed
# relative to a control group.
# The input taxon_ranks are log2 fold changes between control and test
# group
# (e.g., healthy and IBD).
# 
# @param taxon_ranks A named vector of log2 fold changes between control
# and test group.
# @param lookup_missing Logical value indicating whether to fetch missing
# NCBI IDs. Default is FALSE.
# @param min_set_size Minimum size of taxon sets to include in the
# analysis.
# Default is 5.
# @param max_set_size Maximum size of taxon sets to include in the
# analysis.
# Default is 100.
# @return A list of data frames with taxon set enrichment results.
# @seealso
# \itemize{
#   \item \url{https://doi.org/10.1093/nar/gkac868} for MiMeDB
#   \item \url{https://doi.org/10.1093/nar/gkab1019} for GMrepo
#   \item \url{https://doi.org/10.1093/nar/gkab786} for gutMGene
#   \item \url{https://doi.org/10.1038/s41587-023-01872-y} for BugSigDB


from TaxSEA_in_python import get_IDs
from scipy.stats import ks_2samp
import pandas as pd
import numpy as np
import os
from statsmodels.stats.multitest import multipletests

def TaxSEA(taxon_ranks, Output_location=None):
    """
    The input is a taxon_rank list, can be either a dictionary, tsv or csv file. 

    Arguments: 
        taxon_ranks is the taxon_rank list 
        Output_location (str): is the output location for results to be printed out as 3 csv files

    return: 
        A results dictionary of the 3 dataframes.
    """
    def ensure_input(taxon_rank):
        """
        This function ensure that the input is either a dictionary, tsv or csv file.
        """
        if isinstance(taxon_rank, dict):
            return taxon_rank 
        
        elif isinstance(taxon_rank, str) and taxon_rank.endswith(('.csv', '.tsv')):
            print(f"Input is not a dictionary, converting ...")
            delimiter = ',' if taxon_rank.endswith('.csv') else '\t'
            
            try:
                df = pd.read_csv(taxon_rank, delimiter=delimiter, header=None)
                if df.shape[1] != 2:
                    raise ValueError("The file must have exactly 2 columns: Taxon_name and values.")
                
                converted_dict = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))
                print(f"Successfully converted file '{taxon_rank}' to a dictionary.")
                return converted_dict

            except Exception as e:
                raise ValueError(f"Error processing the file: {e}")

        else:
            raise ValueError("Input must be either a dictionary or a valid CSV/TSV file path.")

    # Checking for correct input format: 
    taxon_ranks = ensure_input(taxon_ranks)
    
    # Setting up Taxon_ranks: 
    taxon_ranks_name = taxon_ranks.keys()
    if len(taxon_ranks_name) < 3: 
        raise ValueError("Error: Very few taxa provided")
    
    # Converting Bacterial name into ncbi ids
    taxon_ranks_original = get_IDs.NCBI(taxon_ranks_name)
    taxon_ranks = {taxon_ranks_original[ID]: values for ID, values in taxon_ranks.items()}
    
    # Filtering the taxon_sets for taxon ranks name: 
    taxon_sets = get_IDs.Taxon(taxon_ranks_name)
    taxon_sets = {
        taxon : [ncbi_id for ncbi_id in ids if ncbi_id in taxon_ranks]
        for taxon, ids in taxon_sets.items()
    }

    # setting the min and max length for taxon sets
    taxon_sets = {
        taxon: ids for taxon, ids in taxon_sets.items() 
        if 5 <= len(ids) <= 100
    }

    # Perform KS test:
    ks_results = {}
    for taxon_name, ncbi_ids in taxon_sets.items(): # taxon_sets_ranks contain ncbi id and ranks 
        taxon_sets_ranks = {ncbi_id : taxon_ranks[ncbi_id] for ncbi_id in ncbi_ids if ncbi_id in taxon_ranks.keys()}
        
        # Isolating the values from the dictionaries:
        taxon_sets_ranks_values = list(taxon_sets_ranks.values())
        taxon_ranks_values = list(taxon_ranks.values())

        # perform the kstest: 
        # ks_test = ks_2samp(taxon_sets_ranks_values, taxon_ranks_values)
        nes = float(np.median(taxon_sets_ranks_values))

        taxon_set_name = [bacterial_name for bacterial_name, ncbi_id in taxon_ranks_original.items() if ncbi_id in ncbi_ids]

        pvalue = [float(ks_2samp(taxon_sets_ranks_values, taxon_ranks_values).pvalue) for taxon_name in taxon_sets]
        _, FDR, _, _ = multipletests(pvalue, alpha=0.05, method='fdr_bh')

        # concluding the results: 
        ks_results[taxon_name] = {
            'median_rank_of_set_members': nes,
            'pvalue': pvalue[0],
            'FDR' : FDR[0],
            'TaxonSet': taxon_set_name
        }

    # seperating the taxons into different categories: 

    metabolites_dict = {key : values for key, values in ks_results.items() if 'producers_of' in key}
    bsdb_dict = {key : values for key, values in ks_results.items() if 'bsdb' in key}
    disease_dict = {key : values for key, values in ks_results.items()  if "producers_of" not in key and "bsdb" not in key}

    # Turing ks_results into a dataframe: 
    metabolites_df = pd.DataFrame(metabolites_dict).T
    bsdb_df = pd.DataFrame(bsdb_dict).T
    disease_df = pd.DataFrame(disease_dict).T

    # Placing them in a dictionary and recalculating FDR values according to their categories
    list_of_df = {"Metabolite_producers" : metabolites_df , "BugSigdB" : bsdb_df, "Health_associations" : disease_df}
    for df in list_of_df.values():
        if not df.empty:
            pvalues = df['pvalue'].values
            df['FDR'] = multipletests(pvalues, alpha=0.05, method='fdr_bh')[1]

    # Output_location if specified:
    if Output_location:
        # Ensure the directory exists
        os.makedirs(Output_location, exist_ok=True)

        # Save each DataFrame to a CSV file
        for categories, df in list_of_df.items():
            if df is not None: 
                csv_path = os.path.join(Output_location, f"{categories}.csv")
                df.to_csv(csv_path, index=False)
                print(f"Saved {categories} to {csv_path}")

    return list_of_df
