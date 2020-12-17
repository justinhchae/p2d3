import os
import pandas as pd
import numpy as np

from p2d3.pandas_to_d3 import PandastoD3

if __name__ == '__main__':
    filename = '311_City_Service_Requests_in_2020.zip'
    folder = 'data'
    path = os.environ['PWD'] + os.sep + os.sep.join([folder, filename])

    usecols = ['WARD', 'ORGANIZATIONACRONYM', 'SERVICECODEDESCRIPTION', 'SERVICEORDERSTATUS', 'SERVICEORDERDATE', 'RESOLUTIONDATE']
    dtype = {'WARD':'category'}
    parse_dates = ['SERVICEORDERDATE', 'RESOLUTIONDATE']

    df = pd.read_csv(path, usecols=usecols, dtype=dtype, parse_dates=parse_dates)

    df['service_time'] = df['RESOLUTIONDATE'] - df['SERVICEORDERDATE']
    df['service_time'] = df['service_time'] / np.timedelta64(1, 'h')
    df['SERVICEORDERSTATUS'] = df['SERVICEORDERSTATUS'].str.lower()
    df = df[(df['SERVICEORDERSTATUS'] == 'closed')]

    parse_dates.append('SERVICEORDERSTATUS')
    df.drop(columns=parse_dates, axis=1, inplace=True)

    group = ['WARD', 'ORGANIZATIONACRONYM', 'SERVICECODEDESCRIPTION']
    df = df[['WARD', 'ORGANIZATIONACRONYM', 'SERVICECODEDESCRIPTION', 'service_time']]

    df.dropna(thresh=2, inplace=True)

    df['WARD'] = 'WARD ' + df['WARD'].astype(str)

    df = df.groupby(group)[['service_time']].mean().dropna(axis=0, how='any')

    df = df.reset_index()
    print(df.head(2))

    convert = PandastoD3()
    convert.p2d3(df)

