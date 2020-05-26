from instance import instance_generator
import random
import numpy as np
import time


def gen_K(n):
    return int(np.sqrt(n))

def gen_Order(n):
    return int(np.sqrt(n))

def gen_mDistFerrovie(n):
    return int(np.sqrt(n))

def gen_CapStrada(demand, Orders):
    return  int(demand*Orders)



def generator(num_instances,min_demand, max_demand, min_costs_strade, max_costs_strade, min_costs_ferrovie, max_costs_ferrovie):

    for i in range(1, num_instances):
        n = 10**i

        K = gen_K(n)


        Orders = gen_Order(n)

        min_cap_strade = gen_CapStrada(min_demand,Orders)
        max_cap_strade = gen_CapStrada(max_demand,Orders)

        min_cap_ferrovie = min_demand
        max_cap_ferrovie = min_cap_strade -1

        min_dist_ferrovie = gen_mDistFerrovie(n)

        file_name = 'inst_'+str(n)+'_'+str(min_demand)+'_'+str(max_demand)+'_'+str(min_costs_strade)+'_'+\
        str(max_costs_strade)+'_'+str(min_costs_ferrovie)+'_'+str(max_costs_ferrovie)+'_'+str(int(time.time()*1000))+'.cmpl'

        instance_generator(k=K,Orders=Orders, Nodes=n,min_demand=min_demand,max_demand=max_demand, min_cap_strade=min_cap_strade,
        max_cap_strade=max_cap_strade, min_costs_strade=min_costs_strade, max_costs_strade=max_costs_strade,min_cap_ferrovie=min_cap_ferrovie,
        max_cap_ferrovie=max_cap_ferrovie,min_costs_ferrovie=min_costs_ferrovie,max_costs_ferrovie=max_costs_ferrovie,perc_att_ferrovie=perc_att_ferrovie,
        min_dist_ferrovie=min_dist_ferrovie,file_name=file_name)




if __name__ == "__main__":
    num_instances = 3
    ## Topologia del grafo
    perc_att_ferrovie = 0.01 #OK

    ## Demand
    min_demand = 10 #OK
    max_demand = 500 #OK
    min_costs_strade = 50
    max_costs_strade = 75
    min_costs_ferrovie = 25
    max_costs_ferrovie = 45

    generator(num_instances,min_demand, max_demand, min_costs_strade, max_costs_strade, min_costs_ferrovie, max_costs_ferrovie)