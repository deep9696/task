import sys



# import fileinput
# for line in fileinput.input():
#     print(line)

fout = open('input_dummy.txt', 'w')
for line in sys.stdin:
    content = line
    if content.rstrip():
        fout.write(content)
    #fout.write(content)
fout.close()

with open('input_dummy.txt') as f:
    input_text = f.readlines()
    ls = ''.join(input_text)
    ls = ls.split('\n')


#print(ls)
check = '*'
count = 1
for idx in ls:
    if idx.startswith("*"):
        if len(idx.replace('*', str(count)).split()[0]) == 1:
            single_star = idx.replace('*', str(count))
            print(single_star)


        if len(idx.replace('**', str(count)+'1').split()[0])==2:
            double_star = idx.replace('**', str(count-1)+'.'+'1')
            print(double_star)

        if len(idx.replace('***', str(count) + '11').split()[0]) == 3:
            t_star = idx.replace('***', str(count - 2) + '.' + '1' + '.' + '1')
            print(t_star)

        if len(idx.replace('****', str(count)+'111').split()[0])==4:

            f_star = idx.replace('****', str(count-3)+'.'+'1'+'.'+'1'+'.'+'1')
            print(f_star)
        count+=1
    elif idx.startswith(".") and len(idx.replace('.', str(count)).split()[0]) == 1:
        single_star_dot = idx.replace('.', ' +')
        print(single_star_dot)
    elif idx.startswith("..") and len(idx.replace('..', str(count-4)).split()[0]) == 2:
        single_star_dot = idx.replace('..', '  -')
        print(single_star_dot)

    elif idx.startswith("...") and len(idx.replace('...', str(count+1)).split()[0]) == 3:
        single_star_dot = idx.replace('...', '   -')
        print("333 count", count)
        print(single_star_dot)
    elif idx.startswith(".") and len(idx.replace('.', str(count-9)).split()[0]) == 1:
        single_star_dot = idx.replace('.', '  -')
        print(single_star_dot)

    else:

        print(idx)







    # else:
    #     print(idx)

    # if idx.startswith("**"):
    #     print(idx.replace('**',  str(count)+'.'+'1'))
    #
    #     count = count + 1



#print(input_text)








# with open(outFile,'w') as o:
#     for line in content:
#         o.write(line)


