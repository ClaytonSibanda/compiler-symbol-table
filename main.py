#!/usr/bin/python

import sys
import copy
# print(sys.argv)

def handle_define(s_list,data,stack,output):
    stack[len(stack)-1][s_list[1]] = s_list[2]
    output.append(" ".join(s_list))
    # print(stack)

def handle_use(key,stack,output):
    if len(stack)>0:
        scope = stack[len(stack)-1]
        if(key in scope):
            output.append('use '+key+ ' = '+scope[key])
        else:
            output.append('use '+key+ ' = undefined')
    else:
        output.append('use '+key+ ' = undefined')
 

def handle_endscope(stack,output):
    stack.pop()
    output.append('endscope')

def handle_beginscope(stack,output):
    stack.append(copy.deepcopy(stack[len(stack)-1]) if len(stack)>0 else {})
    output.append('beginscope')

def handle_output(output):

    for s in output:
        print(s)

def read_data(filename):
    with open(filename,'r') as file:
        data= [s.strip() for s in file.readlines()]
    # print(data)
    return data

def construct_table(stack,output,data):
    for s in data:
        s_list = s.split()
        if len(s_list)==0:
            continue
        # print(s_list)
        if s_list[0]=='define':
            # print('define identified')
            handle_define(s_list,data,stack,output)
                
        elif s_list[0]=='use':
            # print('use identified')
            handle_use(s_list[1],stack,output)
        elif s=='beginscope':
            # print('begin scope')
            handle_beginscope(stack,output)
          
        elif s=='endscope':
            # print('end scope')
            handle_endscope(stack,output)

def main():
  
    stack =[]
    output = []
    filename = sys.argv[1]
    data = read_data(filename)
    construct_table(stack,output,data)
    
    
    handle_output(output)
           





if __name__=='__main__':
    main()