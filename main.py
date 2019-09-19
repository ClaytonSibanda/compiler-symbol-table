#!/usr/bin/python




def handle_define(s_list,data,stack):
    stack[len(stack)-1][s_list[1]] = s_list[2]
    print(stack)

def handle_use(s_list,stack,output):
    pass

def handle_endscope(stack,output):
    stack.pop()

def handle_beginscope(stack,output):
    stack.append({})
    output.append('beginscope')

def handle_output(output):

    for s in output:
        print(s)

def main():
    # stack.append({})
    data =[]
    stack =[]
    output = []
    with open('testdata/test1.dat','r') as file:
        data= [s.strip() for s in file.readlines()]
    print(data)

    for s in data:
        s_list = s.split()
        #print(s_list)
        if s_list[0]=='define':
            print('define identified')
            handle_define(s_list,data,stack)
                
        elif s_list[0]=='use':
            print('use identified')
            handle_use(s_list,stack,output)
        elif s=='beginscope':
            print('begin scope')
            handle_beginscope(stack,output)
          
        elif s=='endscope':
            print('end scope')
            handle_endscope(stack,output)
    
    handle_output(output)
           





if __name__=='__main__':
    main()