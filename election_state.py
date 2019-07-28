nda = 0
upa = 0
others = 0


def getting_weights(lines, count_dict, diff_dict, actual_dict):
    count = 0
    for line in lines:
        l = line.split(' ')
        if(l[0][0] != '(' and l[0] != '\n'):
            a = actual_dict[ l[0] ]
            b = int(a[0])
            c = int(a[1])
            o = int(a[2])
            if( l[1] in count_dict.keys() ):
                count_dict[ l[1] ] = count_dict[ l[1] ] + 1
                diff = ( abs(b - int(l[2])) + abs(c - int(l[3])) + abs(o - int(l[4])) ) / 3
                diff_dict[ l[1] ] += diff
    print("-----------------------")
    print(diff_dict)
    print("-----------------------")
    print(count_dict)
    for i in diff_dict:
        if(count_dict[i] != 0):
            diff_dict[i] = (diff_dict[i]/count_dict[i])**-2
            
    return diff_dict


def predict_output(diff_dict, lines):
    ob = 0
    oc = 0
    oo = 0
    w = 0
    global nda, upa, others
    for line in lines:
        l = line.split(' ')
        if(l[0][0] == '(' or l[0] == '\n'):
            if(w != 0):
                nda += ob/w
                upa += oc/w
                others += oo/w
            ob = 0
            oc = 0
            oo = 0
            w = 0
            continue
        if(l[1] not in diff_dict.keys()):
            continue
        used_dict[l[1]] = 0
        ob += int(l[2])*diff_dict[ l[1] ]
        oc += int(l[3])*diff_dict[ l[1] ]
        oo += int(l[4])*diff_dict[ l[1] ]
        w += diff_dict[ l[1] ]

        
file_2019 = open('statewise.txt', 'r')
file_2014 = open('statewise2014.txt', 'r')
file_actual = open('actual_result.txt', 'r')
file_temp_2019 = open('temp_2019.txt', 'r')

if(file_2014.closed or file_2019.closed or file_actual.closed):
    print("Could not open file!")
used_dict = {}
actual_dict = {}
count_dict = {}
diff_dict = {}
lines_2014 = file_2014.readlines()
lines_2019 = file_2019.readlines()
lines_file_temp_2019 = file_temp_2019.readlines()
for line in lines_2014:
    l = line.split(' ')
    if(l[0][0] != '(' and l[0] != '\n'):
        count_dict[ l[1] ] = 0
        diff_dict[ l[1] ] = 0


actual_line = file_actual.readlines()
for i in actual_line:
    l = i.split(' ')
    bjp = int(l[1])
    cong = int(l[2])
    othr = int(l[3])
    a = [bjp, cong, othr]
    actual_dict[l[0]] = a

diff_dict = getting_weights(lines_2014, count_dict, diff_dict, actual_dict)
print(diff_dict)
predict_output(diff_dict, lines_2019)

weight = 0
count_ = 0
for i in diff_dict:
    count_ += 1
    weight += diff_dict[i]
print(weight/count_)

file_temp_2019.close()
file_temp_2019 =  open('temp_2019.txt', 'w')

for item in lines_file_temp_2019:
    i = item.split(' ')
    if(i[0][0] == 'M' and i[0][1] == 'I' and i[0][2] == 'N' and i[0][3] == 'E'):
        continue
    file_temp_2019.write("%s" % item)
s = "MINE " + str(int(nda)) + " " + str(int(upa)) + " " + str(int(others))  
file_temp_2019.write('\n')
file_temp_2019.write(s)


print("-----Using only statewise data------")

print(nda)
print(upa)
print(others)

file_result = open('result.txt', 'w')
file_result.write('Using only statewise data\n')
file_result.write(str(nda))
file_result.write('\n')
file_result.write(str(upa))
file_result.write('\n')
file_result.write(str(others))
