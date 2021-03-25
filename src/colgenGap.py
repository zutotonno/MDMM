import argparse
import xml.etree.ElementTree as ET
import numpy as np
from ast import literal_eval as make_tuple



def d_problem(problem_instance):
    with open(problem_instance, mode='r') as myfile:
        init_c = False
        str_problem=''
        for line in myfile:
            if line.startswith('d'):
                init_c=True
                str_problem+=line
            elif line.startswith('c'):
                init_c=False
                break
    str_problem = str_problem.replace(";", "")
    str_problem = str_problem.replace("\n", "")
    str_problem = str_problem.replace("d[ORDERS] := ", "")
    tuple_problem = make_tuple(str_problem)
    array_problem = np.array(tuple_problem)
    return array_problem

def u_problem(problem_instance, valid_nodes):
    with open(problem_instance, mode='r') as myfile:
        init_c = False
        str_problem='('
        for line in myfile:
            if line.startswith('u'):
                init_c=True
            elif line.startswith('b'):
                init_c=False
                break
            elif init_c:
                str_problem+=line
    str_problem = str_problem.replace(";", "")
    str_problem = str_problem.replace("\n", "")
    tuple_problem = make_tuple(str_problem)
    array_problem = np.array(tuple_problem)
    return array_problem[np.ix_(valid_nodes,valid_nodes)]

def c_problem(problem_instance, valid_nodes):
    with open(problem_instance, mode='r') as myfile:
        init_c = False
        str_problem='('
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

    

    return array_problem[np.ix_(valid_nodes,valid_nodes)]

def read_problem(problem_instance, nagg=None):
    with open(problem_instance, mode='r') as myfile:
        init_c = False
        str_problem=''
        for line in myfile:
            if line.startswith('b'):
                init_c=True
                str_problem+=line
                break

    str_problem = str_problem.replace(";", "")
    str_problem = str_problem.replace("\n", "")
    str_problem = str_problem.replace("b[NODES,ORDERS] := ", "")
    tuple_problem = make_tuple(str_problem)
    array_problem = np.array(tuple_problem)

    valid_nodes = set()
    for i in range(0, array_problem.shape[1]):
        curr = array_problem[:,i]
        dest = np.argwhere(curr == 1).flatten()[0]
        part = np.argwhere(curr == -1).flatten()[0]
        valid_nodes.add(dest)
        valid_nodes.add(part)
    if nagg is not None:
        valid_nodes.update(nagg)
    valid_array = np.array(list(valid_nodes))
    return valid_array, array_problem[valid_array]



def generate_newinstance(k, d_Orders, costs, capacities, b_array, filename, gencolID):

    Nodes = costs.shape[0]
    Orders = len(d_Orders)
    print('Nodi: ',Nodes,', Ordini: ', Orders,', Barray shape: ', b_array.shape)
    print('Costarray shape: ',costs.shape,', Caparray shape: ', capacities.shape,', Ordarray shape: ', d_Orders.shape)
    # Installiamo alcune ferrovie
    strCap = '('
    strCosts = '('
    for i in range(Nodes):
        strCap+='\n'
        strCosts+='\n'
        strCap+='('
        strCosts+='('
        for j in range(Nodes):

            fn='),'
            if j==Nodes-1:
                fn = ')'
            strCap+='( '+str(capacities[i,j,0])+' , '+str(capacities[i,j,1]) +fn
            strCosts+='( '+str(costs[i,j,0])+' , '+str(costs[i,j,1]) +fn

        fn='),'
        if i==Nodes-1:
            fn = ')'
        strCap+=fn
        strCosts+=fn
    strCap+=')'
    strCosts+=')'

    b = np.array(b_array)
    b = tuple(tuple(x) for x in b)

    for i in range(0,4):
        file_name = filename[:-5]+'_ColGen_'+str(gencolID)+'.cmpl'
        parameters=[]
        parameters.append('K :='+str(k)+';')
        parameters.append('ORDERS := 1(1)'+str(Orders)+';')
        parameters.append('NODES := 1(1)'+str(Nodes)+';')
        parameters.append('EDGES := 1(1)2;')
        parameters.append('d[ORDERS] := '+str(tuple(d_Orders))+';')
        parameters.append('c[NODES,NODES,EDGES] := ' +strCosts+';')
        parameters.append('u[NODES,NODES,EDGES] := ' +strCap+';')
        parameters.append('b[NODES,ORDERS] := ' +str(b)+';')


        s = "%arg -ignoreZeros"
        t = "%arg -solver glpk\n%opt glpk tmlim 300"
        with open(file_name, mode='w+') as myfile:
            myfile.write(s+'\n')
        with open(file_name, mode='a+') as myfile:
            myfile.write(t+'\n')
        with open(file_name, mode='a+') as myfile:
            myfile.write("parameters:"+'\n')

        with open(file_name, mode='a+') as myfile:
            for item in parameters:
                myfile.write(item+'\n')

        final_string = ["variables:","y[ORDERS,NODES,NODES,EDGES]: integer[0..1];",
        "objectives:","cost: sum{ h in ORDERS, i in NODES , j in NODES, e in EDGES : c[i,j,e] * y[h,i,j,e] } -> min;",
        "constraints:","bilancio  { i in NODES,  h in ORDERS: sum{ j in NODES, e in EDGES : y[h,j,i,e] } - sum{ j in NODES, e in EDGES : y[h,i,j,e] } = b[i,h]; }",
        "capacity { i in NODES , j in NODES, e in EDGES : sum{ h in ORDERS : y[h,i,j,e] * d[h] } <= u[i,j,e]; }",
        "lunghezza { h in ORDERS : sum {i in NODES, j in NODES, e in EDGES : y[h,i,j,e]} <= K ; }",
        "unico {h in ORDERS, i in NODES, e in EDGES: sum {j in NODES: y[h,i,j,e]} <= 1; }"]
        with open(file_name, mode='a+') as myfile:
            for item in final_string:
                myfile.write(item+'\n')


def k_problem(problem_instance):
    with open(problem_instance, mode='r') as myfile:
        init_c = False
        str_problem=''
        for line in myfile:
            if line.startswith('K'):
                init_c=True
                str_problem+=line
            elif line.startswith('O'):
                init_c=False
                break

    str_problem = str_problem.replace(";", "")
    str_problem = str_problem.replace("\n", "")
    str_problem = str_problem.replace("K :=", "")
    k_problem = int(str_problem)
    return k_problem


def n_problem(problem_instance):
    with open(problem_instance, mode='r') as myfile:
        init_c = False
        str_problem=''
        for line in myfile:
            if line.startswith('N'):
                init_c=True
                str_problem+=line
            elif line.startswith('E'):
                init_c=False
                break

    str_problem = str_problem.replace(";", "")
    str_problem = str_problem.replace("\n", "")
    str_problem = str_problem.replace("NODES := 1(1)", "")
    n_problem = int(str_problem)
    return n_problem


def cost_sort(narray, odarray, carray, how='S'):
    cn = dict()
    for n in narray:
        if n not in cn.keys():
            cn[n] = 0
        for od in odarray:
            if how == 'S':
                costo = carray[n,od,0] + carray[od,n,0]
            elif how == 'R':
                costo = carray[n,od,1] + carray[od,n,1]
            elif how == 'B':
                costo = carray[n,od,1] + carray[od,n,1] + carray[n,od,0] + carray[od,n,0]
            cn[n]+=costo
    return sorted(cn.items(), key=lambda x: x[1])




if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        type=str,
        nargs="+",
        help='Path of the .cmpl instance'
    )
    parser.add_argument(
        "--how",
        type=str,
        help='S for street, R for railways, B for both'
    )


    args = parser.parse_args()
    how = args.how
    all_inst_path = args.p
    for inst_path in all_inst_path:
        b_array, valid_b = read_problem(inst_path, nagg=None)
        d_array = d_problem(inst_path)
        

        k = k_problem(inst_path)
        n_p = n_problem(inst_path)
        tot_array = np.arange(0,n_p)
        tot_cost = c_problem(inst_path, tot_array)
        del_array = np.sort(list(set(tot_array) - set(b_array)))

        del_array = [c[0] for c in cost_sort(del_array, b_array, tot_cost,how=how)]
        for i in range(0,10):
            b_array, valid_b = read_problem(inst_path, nagg = del_array[:i+1])
            c_array = c_problem(inst_path, b_array)
            u_array = u_problem(inst_path, b_array)
            generate_newinstance(k, d_array, c_array, u_array, valid_b, inst_path, i+1)