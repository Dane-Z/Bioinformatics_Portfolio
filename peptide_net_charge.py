#!/usr/bin/env python3
# Dane Zeeb
# Polypeptide net charge calculator



#peptide_seq = 'IKELKMSKDEIKREYKEMEGSPEIKSKRRQFHQEIQSGNMRENVKRSSVVVADPTHIAIGILYKRGETPLPLVTFKYTDAQVQTVRKIAEEEGVPILQRIPLARALYWDALVDHYIPAEQIEATAEVLRWLERQNIEKQHSEML'


def peptide_net_charge(pH = None, peptide_seq = None):
#List of possible variables
    k = 0.0
    hPlus = 0.0
    p_charge = False
    n_charge = False
    net_charge = 0.0
    pk = 0.0
    ionic = False
    ionic_list = {'D', 'E', 'Y', 'C', 'H', 'K', 'R'}
    D_count = 0
    E_count = 0
    Y_count = 0
    C_count = 0
    H_count = 0
    K_count = 0
    R_count = 0
    
#N-terminus pK1 is I; C-terminus pK2 is L
    pK_N = 2.3
    pK_C = 9.7
    
#Calculate hPlus
    hPlus = 10 ** pH
    
#Check if pH is < or > pK for N- and C-terminus
    if pH > pK_N:
        net_charge = net_charge
    if pH < pK_N:
        net_charge += 1
        
    if pH > pK_C:
        net_charge -= 1
    if pH < pK_C:
        net_charge = net_charge

#Check if char is ionic
    for char in peptide_seq:
        if char in ionic_list:
            ionic = True

#Calculate K if ionic and check if pH is < or > of pK. Add or subtract 1 from net_charge
        if ionic == True:
            if char == 'D':
                D_count += 1
                pK = 3.86
                k = 10 ** pK
                if pH > pK:
                    net_charge -= 1
                if pH < pK:
                    net_charge = net_charge
                    
            if char == 'E':
                E_count += 1
                pK = 4.25
                k = 10 ** pK
                if pH > pK:
                    net_charge -= 1
                if pH < pK:
                    net_charge = net_charge
                    
            if char == 'Y':
                Y_count += 1
                pK = 10.07
                k = 10 ** pK
                if pH > pK:
                    net_charge -= 1
                if pH < pK:
                    net_charge = net_charge
                    
            if char == 'C':
                C_count += 1
                pK = 8.33
                k = 10 ** pK
                if pH > pK:
                    net_charge -= 1
                if pH < pK:
                    net_charge = net_charge



            if char == 'H':
                H_count += 1
                pK = 6.00
                k = 10 ** pK
                if pH > pK:
                    net_charge = net_charge
                if pH < pK:
                    net_charge += 1
                    
            if char == 'K':
                K_count += 1
                pK = 10.79
                k = 10 ** pK
                if pH > pK:
                    net_charge = net_charge
                if pH < pK:
                    net_charge += 1
                    
            if char == 'R':
                R_count += 1
                pK = 12.48
                k =  10 ** pK
                if pH > pK:
                    net_charge = net_charge
                if pH < pK:
                    net_charge += 1 

    print(net_charge)
    #print(D_count, E_count, Y_count, C_count, H_count, K_count, R_count)

# Input commands
pH = float(input("Please input a pH value: "))
peptide_seq = input("Please provide the peptide sequence: ")
peptide_net_charge(pH, peptide_seq)


            
        


