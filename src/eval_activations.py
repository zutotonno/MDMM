import argparse
import xml.etree.ElementTree as ET
import numpy as np
from ast import literal_eval as make_tuple
import re

def read_lagrange(lagrange_instance):
    root = ET.parse(lagrange_instance).getroot()
    relax_original_cost = 0
    y_lagranges = []
    strada = 0
    ferr = 0
    for f in root.iter("variable"):
        __curr_y = f.attrib['name']
        _curr_y = __curr_y[2:-1]
        curr_y = np.fromstring(_curr_y, dtype=int, sep=',')
        y_lagranges.append(curr_y)
        if curr_y[-1] == 1:
            strada+=1
        else:
            ferr+=1

    return y_lagranges,strada,ferr






if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-sol",
        type=str,
        nargs='*'
    )
    args = parser.parse_args()

    for s in args.sol:
        print(s)

        n_nodes = int(int((s.split("_"))[1])/2)
        y_lagranges,y_strada,y_ferr = read_lagrange(s)
        print('*******************')
        print("N_Orders")
        print(n_nodes)
        print("Attivazioni strade e ferrovie:")
        print(y_strada, y_ferr)
        print("Tot attivazioni:")
        print(y_strada+y_ferr)
        print('******************')