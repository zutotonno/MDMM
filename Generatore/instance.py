import numpy as np
import sys
import random
from scipy.stats import norm, lognorm


def instance_generator(Orders=2, Nodes=4,min_demand=10, max_demand=50, min_cap_strade=50, max_cap_strade=100, min_costs_strade=50, max_costs_strade=100,
                                                min_cap_ferrovie=1,max_cap_ferrovie=49,min_costs_ferrovie=1,max_costs_ferrovie=49,
                                                perc_att_ferrovie=0.6, min_dist_ferrovie=1,_file_name='prova.cmpl'):



    d_Orders = [random.randint(min_demand, max_demand) for i in range(Orders)]
    #d_Orders = [int(norm.rvs(1.5,size=1)[0])+min_demand for i in range(Orders)]


    ## Strade : percentuale attivazione alta e capacita alta, ferrovie il contrario. Strade lontane costano tanto
    capacities = np.zeros((Nodes,Nodes,2), dtype=int)
    costs = np.zeros((Nodes,Nodes,2),dtype=int)

    for i in range(capacities.shape[0]):
        for j in range(capacities.shape[1]):
            att_strade = i!=j and random.uniform(0,1)<0.9
            capacities[i,j,0] = int(lognorm.rvs(2.5,size=1)[0])+max_cap_strade if att_strade else 0
            costs[i,j,0] = (int(lognorm.rvs(1.25,size=1)[0])+min_costs_strade)*abs(i-j) if att_strade else 0

    num_ferr = 0
    # Installiamo alcune ferrovie
    strCap = '('
    strCosts = '('
    for i in range(Nodes):
        strCap+='\n'
        strCosts+='\n'
        strCap+='('
        strCosts+='('
        for j in range(Nodes):

            att_ferrovia = random.uniform(0,1)<(abs(i-j)/(Nodes-1)*perc_att_ferrovie)
            if(att_ferrovia):
                num_ferr+=1
            capacities[i,j,1] = (int(norm.rvs(1,size=1)[0])+max_cap_ferrovie if (att_ferrovia) else 0)
            #capacities[i,j] = tuple(capacities[i,j])

            costs[i,j,1] = (int(lognorm.rvs(1.25,size=1)[0])+min_costs_ferrovie if (att_ferrovia) else 0)
            #costs[i,j] = tuple(costs[i,j])
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

    print(num_ferr)

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

    for i in range(0,4):
        k = int(np.ceil((Nodes)/((i+1)*(i+1)))) if i>0 else 2
        file_name = _file_name+'_'+str(k)+'.cmpl'
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
        t = "%arg -solver glpk"
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
        "lunghezza { h in ORDERS, e in EDGES : sum {i in NODES, j in NODES : y[h,i,j,e]} <= K ; }",
        "unico {h in ORDERS, i in NODES, e in EDGES: sum {j in NODES: y[h,i,j,e]} <= 1; }"]
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