import sys
import math
## Promila Agarwal
## March 12, 2016
def Pogo():
    in_f = open('A-large.in', 'r')
    out_f = open('output_large1.txt', 'w')
    num_of_case = int(in_f.readline().rstrip('\n'))
    for i in range(1, num_of_case+1):
        solve_case(in_f, out_f, i)

def get_sale(in_s,num):
    out_s = []
    copy_s = in_s[:]
    for i in range(num):
        cur = copy_s.pop(0)
        out_s.append(cur)
        copy_s.remove((cur/3)*4)
       
    return out_s
	
def solve_case(in_f, out_f, case_index):
	num =int(in_f.readline().rstrip('\n'))
	in_s = in_f.readline().rstrip('\n').split(" ")
	in_s = map(int,in_s)
	out_s = get_sale(in_s,num)
	str1=' '.join(map(str, out_s))
	out_f.write("Case #{}: {}\n".format(case_index, str1))
if __name__ == '__main__':    
    Pogo()
