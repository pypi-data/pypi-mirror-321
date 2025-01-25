# Import the Python-based implementation of TaxSEA, originally developed as an R tool.
from TaxSEA_in_python.TaxSEA import TaxSEA

# Locate the test data file within the package.
from importlib.resources import files 
TaxSEA_test_data = str(files('TaxSEA_in_python.data').joinpath('TaxSEA_test_data.csv'))

# Run the TaxSEA function on the test data.
# Optionally, you can specify an output location for the results by providing the `Output_location` argument.
# Example: TaxSEA(TaxSEA_test_data, Output_location='file/path')
TaxSEA_test_results = TaxSEA(TaxSEA_test_data)
print(TaxSEA_test_results)

# Access the three DataFrames returned in the TaxSEA_test_results dictionary.
Metabolite_producers = TaxSEA_test_results["Metabolite_producers"]
BugSigdB = TaxSEA_test_results["BugSigdB"]
Health_associations = TaxSEA_test_results["Health_associations"]

# Demonstrate other functionalities of TaxSEA: Using the `get_IDs` module to work with bacterial names.
from TaxSEA_in_python import get_IDs 

# Input a list of bacterial names.
bacteria = ['Eubacterium_sp.', 'Ruminococcaceae_', 'Blautia_', 'Lactiplantibacillus_plantarum']

# Convert bacterial names into their corresponding NCBI IDs.
bacterial_ID = get_IDs.NCBI(bacteria) 
print(bacterial_ID)

# Retrieve the Taxons corresponding to the bacterial names.
bacterial_taxon = get_IDs.Taxon(bacteria)
print(bacterial_taxon)