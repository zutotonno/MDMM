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
        relax_original_cost += problem_cost[curr_y[1]-1,curr_y[2]-1,curr_y[3]-1]


    return relax_original_cost,y_lagranges


def read_problem(problem_instance):
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
    args = parser.parse_args()
    arr_prob = read_problem(args.p)
    from_ = 1
    to_ = 1
    while(from_ != -1 and to_ != -1):
        from_ = int(input("Inserisci PARTENZA\n"))
        to_ = int(input("Inseirisci DESTINAZIONE\n"))
        f_cost = arr_prob[from_,to_][1]
        if arr_prob[from_,to_][1] > 1e6:
            f_cost = None
        s_cost = arr_prob[from_,to_][0]
        if arr_prob[from_,to_][0] > 1e6:
            s_cost = None
        print('*******************')
        if from_ * to_ >= 0:
            print("Cost:")
            print("Strada:", s_cost, "Ferrovia:", f_cost)
            print('******************')