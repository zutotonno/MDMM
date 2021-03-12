import argparse
import xml.etree.ElementTree as ET
import numpy as np
from ast import literal_eval as make_tuple

def read_lagrange(lagrange_instance, problem_cost):
    root = ET.parse(lagrange_instance).getroot()
    relax_original_cost = 0
    y_lagranges = []
    for f in root.iter("variable"):
        __curr_y = f.attrib['name']
        _curr_y = __curr_y[2:-1]
        y_lagranges.append(_curr_y)
        curr_y = np.fromstring(_curr_y, dtype=int, sep=',')
        print(curr_y)
        relax_original_cost += problem_cost[curr_y[1]-1,curr_y[2]-1,curr_y[3]-1]


    return relax_original_cost,y_lagranges


def read_problem(problem_instance,cost=True):
    str_problem = '('
    with open(problem_instance, mode='r') as myfile:
        init_c = False
        for line in myfile:
            if line.startswith('c'):
                init_c=True
            elif line.startswith('u'):
                init_c=False
                break
            elif init_c:
                str_problem+=line

    str_problem = str_problem.replace(";", "")
    str_problem = str_problem.replace("\n", "")
    tuple_problem = make_tuple(str_problem)
    array_problem = np.array(tuple_problem)

    return array_problem






if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        type=str,
    )

    parser.add_argument(
        "-l",
        type=str,
    )

    args = parser.parse_args()
    arr_prob = read_problem(args.p)

    lag_cost, y_lagranges = read_lagrange(args.l, arr_prob)
    print('*******************')
    print("Lag cost:")
    print(lag_cost)
    print('******************')