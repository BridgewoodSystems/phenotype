# phenotype

Setup: 

1. Create a python 3 virtual environment in the home directory via `virtualenv -p python3 env_phenotype`.
2. Install the required packages via `pip install requirements.txt`.
3. Download the genotype/phenotype dataset [FROM HERE](http://genomics.cimmyt.org/mexican_iranian/traverse/iranian/standarizedData_univariate.RData)
and move it to the `./lib/data/` directory.
4. To generate the feature and target pickle files, run `python initialize.py` from the main directory.
