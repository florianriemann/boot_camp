import classes.py
import pandas as pd
from datetime import datetime, time, timedelta

aldi=Supermarket()
aldi.simulation()

#save MCMC df to csv
aldi.df_random_walks.to_csv("MCMC_aldi_result.csv", sep=";")