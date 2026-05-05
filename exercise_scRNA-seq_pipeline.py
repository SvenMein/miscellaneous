# this is excersie aims to replicate some of the data and graphs found in Melms, J.C. et al. (2020)
# the original paper can be found here: https://www.nature.com/articles/s41586-021-03569-1
# !pip install scanpy

import scanpy as sc

adata = sc.read_csv("data\GSE171524_RAW\GSM5226574_C51ctr_raw_counts.csv\GSM5226574_C51ctr_raw_counts.csv").T
#print(adata) # gives cell x genes
#print(adata.obs) # prints observations, right now just cell barcodes
#print(adata.var) # prints genes

# preprocessing
## Doublet removal
    ## Doublet removal is optional but preferred

import scvi
print(adata) 
sc.pp.filter_genes(adata, min_cells = 10) # filters out all genes detected in less than 10 cells
print(adata)
sc.pp.highly_variable_genes(adata, n_top_genes=2000, subset=True, flavor="seurat_v3")
scvi.model.SCVI.setup_anndata(adata)
vae = scvi.model.SCVI(adata)
vae.train()

solo = scvi.external.SOLO.from_scvi_model(vae) # creates a model to detect doublets
solo.train()
# now this model should be saved

df = solo.predict() 
df["prediction"] = solo.predict(soft = False)
df.index = df.index.map(lambda X: X[:-2])
print(df) # prints table containing prediction for singlet/doublet cells
df.groupby("prediction").count()
