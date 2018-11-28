# phenotype

Setup: 

1. Create a python 3 virtual environment in the home directory via `virtualenv -p python3 env_phenotype`.
2. Activate the virtual environment `source env_phenotype/bin/activate`.
3. Install the required packages via `pip install requirements.txt`.
4. Download the genotype/phenotype dataset [FROM HERE](http://genomics.cimmyt.org/mexican_iranian/traverse/iranian/standarizedData_univariate.RData)
and move it to the `./lib/data/` directory.
5. To generate the feature and target pickle files, run `python initialize.py` from the main directory.

An example of how to load the prepared feature (X) and target (y) dataframes is given in `scripts/data_load_example.ipynb`.
