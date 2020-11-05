import os
import csv
import numpy as np
import pandas as pd
rootdir = './'


results = dict()
mean_results = dict()
_dirs = os.listdir(rootdir)
for _dir in _dirs:
    if os.path.isdir(_dir):
        for _file in os.listdir(_dir):
            if _file.endswith(".csv"):
                _file_path = os.path.join(_dir,_file)
                with open(_file_path, 'r') as fd:
                    reader = csv.reader(fd)
                    name = _file[:-4]
                    results[name] = dict()
                    mean_results[name] = dict()

                    for row in reader:
                        results[name][row[0]] = [el.replace(',','.') for el in row[1].split(';')]
                   
                    mean_results[name]['mem_mean'] = np.mean([float(el) for el in results[name]['mem']])
                    mean_results[name]['mem_std'] = np.std([float(el) for el in results[name]['mem']])

                    mean_results[name]['time_mean'] = np.mean([float(el) for el in results[name]['time']])
                    mean_results[name]['time_std'] = np.std([float(el) for el in results[name]['time']])


                    mean_results[name]['low_mean'] = np.mean([float(el) for el in results[name]['low']])
                    mean_results[name]['low_std'] = np.std([float(el) for el in results[name]['low']])

                    mean_results[name]['sol_mean'] = np.mean([float(el) for el in results[name]['sol']])
                    mean_results[name]['sol_std'] = np.std([float(el) for el in results[name]['sol']])

                    mean_results[name]['gap_mean'] = np.mean([float(el) for el in results[name]['gap']])
                    mean_results[name]['gap_std'] = np.std([float(el) for el in results[name]['gap']])


df_mean_results = pd.DataFrame(mean_results).transpose()
df_mean_results.to_csv('GLPK_exec.csv')
print(mean_results)
