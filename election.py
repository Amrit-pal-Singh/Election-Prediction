file_2014 = open('temp_2014.txt', 'r')
file_2019 = open('temp_2019.txt', 'r')
if(file_2014.closed or file_2019.closed):
    print("Could not open file!")
lines_2014 = file_2014.readlines()
lines_2019 = file_2019.readlines()

dict_bjp = {}
dict_cong = {}
dict_oth = {}


for iter_line in lines_2014:
    line = iter_line.split(' ')
    dict_bjp[ line[0] ] = int(line[1])
    
for iter_line in lines_2014:
    line = iter_line.split(' ')
    dict_cong[ line[0] ] = int(line[2])
    
for iter_line in lines_2014:
    line = iter_line.split(' ')
    dict_oth[ line[0] ] = int(line[3])

print('\n2014 BJP seats')
print(dict_bjp)
print('\n2014 CONG seats')
print(dict_cong)
print('\n2014 OTH seats')
print(dict_oth)


actual_result = (lines_2014[len(lines_2014) - 1]).split(' ')
actual_bjp = int(actual_result[1])
actual_cong = int(actual_result[2])
actual_oth = int(actual_result[3])

dict_weight = {}
for iter_line in  lines_2014:
    line = iter_line.split(' ')
    
    if(line[0] == 'ActualResults'):
        continue
    bw = abs(actual_bjp - int(line[1]))
    cw = abs(actual_cong - int(line[2]))
    ow = abs(actual_oth - int(line[3]))
    avg = (bw+cw+ow)/3
    if(avg  != 0):
        aw = (avg) ** -2
    dict_weight[ line[0] ] = aw

print('\nWeight of Polls')
print(dict_weight)

dict_bjp_2019 = {}
dict_cong_2019 = {}
dict_oth_2019 = {}

print('\n\n')
print('Polls common in both 2019 and 2014')
for iter_line in lines_2019:
    line = iter_line.split(' ')
    if(line[0] in dict_bjp):
        dict_bjp_2019[ line[0] ] = int(line[1])
        print(line[0])


for iter_line in lines_2019:
    line = iter_line.split(' ')
    if(line[0] in dict_cong):
        dict_cong_2019[ line[0] ] = int(line[2])
    
for iter_line in lines_2019:
    line = iter_line.split(' ')
    if(line[0] in dict_oth):
        dict_oth_2019[ line[0] ] = int(line[3])

print('\n2019 BJP seats')
print(dict_bjp_2019)
print('\n2019 CONG seats')
print(dict_cong_2019)
print('\n2019 OTH seats')
print(dict_oth_2019)

b_2019 = 0
c_2019 = 0
o_2019 = 0
sum_weight = 0
for i in dict_bjp_2019:
    b_2019 = b_2019 + (dict_weight[i] * dict_bjp_2019[i])
    sum_weight = sum_weight + dict_weight[i]
    
for i in dict_cong_2019:
    c_2019 = c_2019 + (dict_weight[i] * dict_cong_2019[i])
    
for i in dict_oth_2019:
    o_2019 = o_2019 + (dict_weight[i] * dict_oth_2019[i])
    

b_2019 = b_2019/sum_weight
c_2019 = c_2019/sum_weight
o_2019 = o_2019/sum_weight


print(dict_weight)

print('----- Fine tuning the result with others polls not present in statewise data')
print('\nbjp_actual ', b_2019)
print('\ncong_actual ', c_2019)
print('\nother_actual ', o_2019)




file_result = open('result.txt', 'a')
file_result.write('\nfine tuning with other polls not present in statewise data\n')
file_result.write(str(b_2019))
file_result.write('\n')
file_result.write(str(c_2019))
file_result.write('\n')
file_result.write(str(o_2019))