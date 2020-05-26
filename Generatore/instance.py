import numpy as np
import sys
import random





def instance_generator(k=3, Orders=2, Nodes=4,min_demand=10, max_demand=50, min_cap_strade=50, max_cap_strade=100, min_costs_strade=50, max_costs_strade=100,
                                                min_cap_ferrovie=1,max_cap_ferrovie=49,min_costs_ferrovie=1,max_costs_ferrovie=49,
                                                perc_att_ferrovie=0.6, min_dist_ferrovie=1,file_name='prova.cmpl'):

    s = "%arg -ignoreZeros"
    with open(file_name, mode='w+') as myfile:
        myfile.write(s+'\n')
    with open(file_name, mode='a+') as myfile:
        myfile.write("parameters:"+'\n')






    d_Orders = [random.randint(min_demand, max_demand) for i in range(Orders)]


    ### Strade : percentuale attivazione alta e capacita alta, ferrovie il contrario. Strade lontane costano tanto
    capacities =[]
    costs =[]
    for i in range(Nodes):
        capacities.append([[random.randint(min_cap_strade, max_cap_strade)] if (i!=j) else [0] for j in range(Nodes)])
        costs.append([[random.randint(min_costs_strade, max_costs_strade)*abs(i-j)] if i!=j else [0] for j in range(Nodes)])

    ## Installiamo alcune ferrovie
    for i in range(Nodes):
        for j in range(Nodes):
            att_ferrovia = random.uniform(0,1)<perc_att_ferrovie and abs(i-j)>min_dist_ferrovie
            capacities[i][j].append(random.randint(min_cap_ferrovie, max_cap_ferrovie) if (att_ferrovia) else 0)
            capacities[i][j] = tuple(capacities[i][j])

            costs[i][j].append(random.randint(min_costs_ferrovie, max_costs_ferrovie) if (att_ferrovia) else 0)
            costs[i][j] = tuple(costs[i][j])

    capacities = tuple(tuple(x) for x in capacities)
    costs = tuple(tuple(x) for x in costs)

    b = []

    for i in range(Orders):
        _b = []
        nodes = random.sample(range(0,Nodes), 2)
        for i in range(0, Nodes):
            if i==nodes[0]:
                _b.append(-1)
            elif i==nodes[1]:
                _b.append(1)
            else:
                _b.append(0)
        b.append(_b)
    b = np.array(b).T
    b = tuple(tuple(x) for x in b)

    parameters=[]

    parameters.append('K :='+str(k)+';')
    parameters.append('ORDERS := 1(1)'+str(Orders)+';')
    parameters.append('NODES := 1(1)'+str(Nodes)+';')
    parameters.append('EDGES := 1(1)2;')
    parameters.append('d[ORDERS] := '+str(tuple(d_Orders))+';')
    parameters.append('c[NODES,NODES,EDGES] := ' +str(costs)+';')
    parameters.append('u[NODES,NODES,EDGES] := ' +str(capacities)+';')
    parameters.append('b[NODES,ORDERS] := ' +str(b)+';')

    with open(file_name, mode='a+') as myfile:
        for item in parameters:
            myfile.write(item+'\n')

    final_string = ["variables:","y[NODES,NODES,ORDERS,EDGES]: integer[0..1];",
    "objectives:","cost: sum{ i in NODES , j in NODES, e in EDGES, h in ORDERS : c[i,j,e] * y[i,j,h,e] } -> min;",
    "constraints:","bilancio  { i in NODES,  h in ORDERS: sum{ j in NODES, e in EDGES : y[j,i,h,e] } - sum{ j in NODES, e in EDGES : y[i,j,h,e] } = b[i,h]; }",
    "capacity { i in NODES , j in NODES, e in EDGES : sum{ h in ORDERS : y[i,j,h,e] * d[h] } <= u[i,j,e]; }",
    "lunghezza { h in ORDERS, e in EDGES : sum {i in NODES, j in NODES : y[i,j,h,e]} <= K ; }",
    "unico {i in NODES,  h in ORDERS, e in EDGES: sum {j in NODES: y[i,j,h,e]} <= 1; }"]
    with open(file_name, mode='a+') as myfile:
        for item in final_string:
            myfile.write(item+'\n')


if __name__ == "__main__":
    k = int(sys.argv[1])
    Orders = int(sys.argv[2])
    Nodes = int(sys.argv[3])
    min_demand = int(sys.argv[4])
    max_demand = int(sys.argv[5])
    min_cap_strade = int(sys.argv[6])
    max_cap_strade = int(sys.argv[7])
    min_costs_strade = int(sys.argv[8])
    max_costs_strade = int(sys.argv[9])

    min_cap_ferrovie = int(sys.argv[10])
    max_cap_ferrovie = int(sys.argv[11])
    min_costs_ferrovie = int(sys.argv[12])
    max_costs_ferrovie = int(sys.argv[13])
    perc_att_ferrovie = float(sys.argv[14])
    min_dist_ferrovie = float(sys.argv[15])
    file_name = sys.argv[16]


    instance_generator(k,Orders, Nodes,min_demand, max_demand,min_cap_strade,max_cap_strade,min_costs_strade,max_costs_strade,
    min_cap_ferrovie,max_cap_ferrovie,min_costs_ferrovie,max_costs_ferrovie,perc_att_ferrovie,min_dist_ferrovie,file_name )