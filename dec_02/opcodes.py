state0=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,19,6,23,2,13,23,27,1,9,27,31,2,31,9,35,1,6,35,39,2,10,39,43,1,5,43,47,1,5,47,51,2,51,6,55,2,10,55,59,1,59,9,63,2,13,63,67,1,10,67,71,1,71,5,75,1,75,6,79,1,10,79,83,1,5,83,87,1,5,87,91,2,91,6,95,2,6,95,99,2,10,99,103,1,103,5,107,1,2,107,111,1,6,111,0,99,2,14,0,0]
state1=[1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,19,6,23,2,13,23,27,1,9,27,31,2,31,9,35,1,6,35,39,2,10,39,43,1,5,43,47,1,5,47,51,2,51,6,55,2,10,55,59,1,59,9,63,2,13,63,67,1,10,67,71,1,71,5,75,1,75,6,79,1,10,79,83,1,5,83,87,1,5,87,91,2,91,6,95,2,6,95,99,2,10,99,103,1,103,5,107,1,2,107,111,1,6,111,0,99,2,14,0,0]

def intop_computer(input_list):
    index=0
    while index < len(input_list):
        if index%4 == 0:
            op_code = input_list[index]
            if (op_code==1) or (op_code==2): #addition
                op_location1=input_list[index+1]
                op_location2=input_list[index+2]
                res_location=input_list[index+3]
            elif op_code==99:
                break
            else:
                print('Unknown opcode! ',op_code)                
            if op_code==1:    
                input_list[res_location]=input_list[op_location1]+input_list[op_location2]
            if op_code==2:
                input_list[res_location]=input_list[op_location1]*input_list[op_location2]
            index+=4
    return input_list[0]

# intop_computer(state0)
# print(state0)

# intop_computer(state1)
# print(state1)

def evaluate_location(a, input_list):
    if a<=0:
        return 1
    if a>=len(input_list):
        return len(input_list)-1
    while input_list[a] in [1,2,99]:
        a=a+1
    return a

def find_noun_and_verb(n_min=0, n_max=99, v_min=0, v_max=99, target_val=19690720):    
    n = int((n_max-n_min)/2)
    v = int((v_max-v_min)/2)
    diff = target_val
    while diff!=0:
        state=state0 # reset op_comps memory
        state[1]=n
        state[2]=v+1
        calc_val=intop_computer(state) 
        print(state)       
        diff = calc_val-target_val
        print(str(state[1]), str(state[2]),'-->', str(calc_val), 'diff=', diff)
        if abs(diff)>10000 and diff<0: # should heavily decrease operands
            n=evaluate_location(n-10, state)
            v=evaluate_location(v-9, state)
            print(str(n), str(v))
        elif abs(diff)>10000 and diff>0: # should heavily increase operands
            n=evaluate_location(n+10, state)
            v=evaluate_location(v+11, state)
            print(str(n), str(v))
        elif abs(diff)<=10000 and diff<0: # lightly decrease ops
            n=evaluate_location(n-2, state)
            v=evaluate_location(v-1, state)
            print(str(n), str(v))
        else:
            n=evaluate_location(n+1, state)
            v=evaluate_location(v+2, state)
            print(str(n), str(v))
    return n, v


noun, verb = find_noun_and_verb()

