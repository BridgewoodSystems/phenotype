import os
import rpy2.robjects as robjects
import numpy as np
import pandas as pd

def feature_target_load(datapath, save_pickles=True):
    if not os.path.isfile(datapath+'X.pkl') or not os.path.isfile(datapath+'/y.pkl'):
        print(datapath+'standarizedData_univariate.RData')
        robjects.r['load'](datapath+'standarizedData_univariate.RData')

    if not os.path.isfile(datapath+'/X.pkl'):

        # Load the individual feature variables
        X = np.array(robjects.r['X'])
        G = np.array(robjects.r['G'])
        D = np.array(robjects.r['D'])
        partitions = np.array(robjects.r['partitions'])

        # Get the number of entries
        N = X.shape[0]
        idx = range(N)

        x_names = ['x'+str(i) for i in range(X.shape[1])]
        df_X = pd.DataFrame(X, columns=x_names, index=idx)

        g_names = ['g'+str(i) for i in range(G.shape[1])]
        df_G = pd.DataFrame(G, columns=g_names, index=idx)

        d_names = ['d'+str(i) for i in range(D.shape[1])]
        df_D = pd.DataFrame(D, columns=d_names, index=idx)

        pa_names = ['pa'+str(i) for i in range(partitions.shape[1])]
        df_partitions = pd.DataFrame(partitions, columns=pa_names, index=idx)

        # Concatinate all feature dataframes together
        feature_frames = [df_X, df_G, df_D, df_partitions]
        F = pd.concat(feature_frames, axis=1)

        # Save full feature dataframe as pickle
        if save_pickles:
            F.to_pickle(datapath+'/X.pkl')
    else:
        F = pd.read_pickle(datapath+'/X.pkl')

    if not os.path.isfile(datapath+'/y.pkl'):

        # Load the phenotype targets
        pheno = np.array(robjects.r['pheno'])

        # Get the number of entires
        N = pheno.shape[0]
        idx = range(N)

        # Create dataframe
        ph_names = ['ph'+str(i) for i in range(pheno.shape[1])]
        y = pd.DataFrame(pheno, columns=ph_names, index=idx)

        # Save as pickle
        if save_pickles:
            y.to_pickle(datapath+'/y.pkl')

    else:
        y = pd.read_pickle(datapath+'/y.pkl')

    return F, y
