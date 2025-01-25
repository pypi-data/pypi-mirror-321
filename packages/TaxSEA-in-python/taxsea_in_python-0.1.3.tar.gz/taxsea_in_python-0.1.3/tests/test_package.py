# TaxSEA_in_python is the python based tools imported from the tool TaxSEA based in R language.
from TaxSEA_in_python.TaxSEA import TaxSEA

# Locating the test data: 
from importlib.resources import files 
TaxSEA_test_data = str(files('TaxSEA_in_python.data').joinpath('TaxSEA_test_data.csv'))

# TaxSEA main code: 
TaxSEA_test_results = TaxSEA(TaxSEA_test_data) # The output is a dictionary of 3 dataframes
print(TaxSEA_test_results) 

# Calling the 3 dataframes in TaxSEA_test_results: 
Metabolite_producers = TaxSEA_test_results["Metabolite_producers"]

BugSigdB = TaxSEA_test_results["BugSigdB"]

Health_associations = TaxSEA_test_results["Health_associations"]

# Other uses of TaxSEA: get_IDs is a tools that convert bacterial names in NCBI_IDs and Taxons
from TaxSEA_in_python import get_IDs 

bacteria = ['Eubacterium_sp.', 'Ruminococcaceae_', 'Blautia_', 'Lactiplantibacillus_plantarum'] # Input must be a list.

# Converting bacterial names into NCBI ID
bacterial_ID = get_IDs.NCBI(bacteria) 
print(bacterial_ID)

# Finding the Taxons correspond to those bacterial names.
bacterial_taxon = get_IDs.Taxon(bacteria)
print(bacterial_taxon)
