# -*- coding: utf-8 -*-
"""
GWAS variant colocalization analysis on MTClass results
@author: ronnieli
"""

import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None

def load_gwas_catalog(genome='hg38'):
    
    '''
    loads a processed version of the GWAS Catalog from Ronnie Li's GitHub page
    Inputs:
        - genome: the genome build to use. Default='hg38'
    Returns:
        - processed version of the GWAS Catalog as a pandas DataFrame
    '''

    gwas_catalog_url = r'https://github.com/ronnieli0114/MTClass/raw/refs/heads/main/data/gwas_catalog_associations_processed.tsv.gz'
    gwas_table = pd.read_table(gwas_catalog_url, sep='\t', header=0, low_memory=False)
    
    # Define appropriate columns and make GenomicRanges object
    gwas_table['seqnames'] = gwas_table['CHR_ID'].apply(lambda x: "chr"+str(x))
    gwas_table['starts'] = gwas_table[f'pos_{genome}'].astype(int)
    gwas_table['ends'] = gwas_table[f'pos_{genome}'].astype(int)
    print('loaded GWAS table')
    return gwas_table.loc[:,['seqnames','starts','ends']]

def gwas_hits(results, gwas_table, metric, n_top, bp=10_000, genome='hg38'):
    
    """ 
    Counts number of GWAS hits in neighborhood window of selected
    variants (both upstream and downstream).
    
    Input: 
        - results = MTClass results dataframe. Can be obtained by running run_mtclass().
        - gwas_table = GWAS Catalog dataframe. Can be obtained by running load_gwas_catalog().
        - metric = metric to sort by ('pval' if MultiPhen or MANOVA)
        - n_top = number of top eQTLs to include in the analysis
        - bp = +/- base pairs to consider in interval. Default=10,000 bp.
        - genome version that variants are formatted in. Default='hg38'.
    Returns:
        - a float of the total number of GWAS hits nearby (adjusted for ties in metrics).
    """
    
    if 'pval' in metric: # sort by p-values in ascending order
        results = results.sort_values(by=metric, ascending=True)
        thres = results.iloc[n_top,:][metric]
        thres_list = []
        for metr in results[metric]:
            if metr < thres:
                thres_list.append('include')
            elif metr == thres:
                thres_list.append('dw')
            else:
                thres_list.append('exclude')
                
    else: # assume it's classification metric
        results = results.sort_values(by=metric, ascending=False)
        thres = results.iloc[n_top,:][metric] # value to break ties
        thres_list = [] 
        for metr in results[metric]:
            if metr > thres:
                thres_list.append('include')
            elif metr == thres:
                thres_list.append('dw')
            else:
                thres_list.append('exclude')
        
    results['thres'] = thres_list

    if genome=='hg38':
        results['seqnames'] = results['variant'].apply(lambda x: x.split('_')[0])
    elif genome=='hg19':
        results['seqnames'] = results['variant'].apply(lambda x: 'chr'+str(x.split('_')[0]))
    else:
        raise ValueError('genome is not hg38 or hg19. please specify.')
    results['starts'] = results['variant'].apply(lambda x: x.split('_')[1]).astype(int)
    results['ends'] = results['variant'].apply(lambda x: x.split('_')[1]).astype(int)
    
    # Search upstream and downstream 10kb
    results['starts'] = results['starts'].subtract(bp)
    results['ends'] = results['ends'].add(bp)
    
    df_inc = results[results['thres']=='include']
    df_dw = results[results['thres']=='dw']
    
    # count number of GWAS hits to include
    df_inc = df_inc.loc[:,['seqnames','starts','ends']]
    count_inc = 0
    
    for chrom in set(df_inc['seqnames']):
        df_inc_chrom = df_inc[df_inc['seqnames']==chrom]
        gwas_chrom = gwas_table[gwas_table['seqnames']==chrom]
        for _, row in df_inc_chrom.iterrows():
            interval = range(row['starts'], row['ends']+1)
            for gwas_pos in gwas_chrom['starts']:
                if gwas_pos in interval:
                    count_inc += 1
    
    # count number of GWAS hits to down-weight
    df_dw = df_dw.loc[:,['seqnames','starts','ends']]
    count_dw = 0
    
    for chrom in set(df_dw['seqnames']):
        df_dw_chrom = df_dw[df_dw['seqnames']==chrom]
        gwas_chrom = gwas_table[gwas_table['seqnames']==chrom]
        for _, row in df_dw_chrom.iterrows():
            interval = range(row['starts'], row['ends']+1)
            for gwas_pos in gwas_chrom['starts']:
                if gwas_pos in interval:
                    count_dw += 1
    
    # Down-weight the counts with threshold values
    n_have = df_dw.shape[0]
    n_needed = n_top - df_inc.shape[0]
    ratio = n_needed/n_have
    count_dw = count_dw * ratio
    
    # Return total GWAS hits
    total_count = np.around((count_inc + count_dw), 2)
    return total_count