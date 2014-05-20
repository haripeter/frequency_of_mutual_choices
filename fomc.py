filename='C:/Users/Peti/Desktop/Virtual Teams Study/netminer inputs/TXT/2013_3_10/2013_3_10_info.txt'


f=open(filename, 'r')
line=f.readlines()
header=[]
adat=[]
adat2=[]
adat3=[]
adat4=[]
lista=[]
#levágja a headert és megtisztítja
for i in line:
    lista.append(i.split('\t'))
for i in lista[0]:
    if len(i)>0:
        header.append(i)
header=[i.strip('\n') for i in header]
#print(header)
#levágja az első oszlopot:
for i in lista:
    adat=lista[1:]
#print(adat)
#levágja az első sort:
for i in adat:
    adat2.append(i[1:])
#kivágja az utolsó oszlopot:
for i in adat2:
   adat3.append(i[-1])
#kivágja a newline chart az utolsó oszlopból:
for i in adat3:
    if len(i) > 1:
        adat4.append(i[:-1])
    else:
        adat4.append(i)
#maaagic: a letisztított utolsó oszlopot bevágja az newlinecharos utolsó oszlop helyére:
g=0
for i in adat2:
    i[-1]=adat4[g]
    g=g+1
#making int in list of lists instead of str; adat5=a végleges, letisztított adatmátrix fuckyeah
adat2=[[int(g) for g in x] for x in adat2]
#print(adat2)

##Hub-------------------------------

p=0
list_of_row=adat2
list_of_row_zeros=[]
for i in list_of_row:
    p+=1
    if sum(i) == 0:
        list_of_row_zeros.append(p)
#print(list_of_row)
#print(adat2)
        
#    i.append(p)
#    if (sum(i)-p) == 0:
#        list_of_row_zeros.append(p)
#print(list_of_row_zeros)

list_of_column=[sum(i) for i in zip(*adat2)]
#print(list_of_column)


list_of_column_zeros=[]
z=0
for i in list_of_column:
    z+=1
    if i == 0:
        list_of_column_zeros.append(z)
#print(list_of_column_zeros)

list_of_column_row_zeros=[]
for i in list_of_column_zeros:
    for k in list_of_row_zeros:
        if i==k:
            list_of_column_row_zeros.append(i)
#print(list_of_column_row_zeros)

##Hibakezelés:

y=0
b=1
for i in list_of_column_row_zeros:
    while b < len(list_of_column_row_zeros):
        if list_of_column_row_zeros[b] < list_of_column_row_zeros[b-1]:
            print("hiba")
            b+=1
        else:
#            print("minden okés")
            y=y+1
            b=b+1
#            print(y)
            if y == len(list_of_column_row_zeros)-1:
                print("")

##ez itt felül tartalmazza azokat a pozíciókat, ahol a sorban és az oszlopban 0 van.

before_clean_data_column=[]
clean_data=[]

def delete_optimization(adat):
    h=0
    j=0
    q=[]
    for i in adat:
        h+=1
        j=i-h
        q.append(j)
    return(q)

list_of_column_row_zeros_opt=delete_optimization(list_of_column_row_zeros)
#print(list_of_column_row_zeros_opt)

def before_clean_data_column_function(datalist):
    for i in datalist:
        for w in list_of_column_row_zeros_opt:
            p=w
            del(i[p])
    return(datalist)

before_clean_data_column=before_clean_data_column_function(adat2)

#print(before_clean_data_column)

def data_cleaned_from_row_zeros(datalist):
    for w in list_of_column_row_zeros_opt:
        q=w
        del(datalist[q])
    return(datalist)

clean_data=data_cleaned_from_row_zeros(before_clean_data_column)
#print(clean_data)

##transzformált adatmátrix (data): az 1-nél nagyobb értékek 1-es értéket kapnak:
data=[]
data=[[i if i == 0 else 1 for i in x] for x in clean_data]

#*****************************
summa=[]
for j in range(len(data)):
    for k in range(len(data)):
        summa.append(data[j][k])
summa=sum(summa)

kl=0
for x in range(len(data)):
    for y in range(len(data)):
        if data[x][y]==data[y][x]:
            if data[x][y]>0:
                kl=kl+1

#******************************
#frequency_of_mutual_choices=kl/summa
print("frequency of mutual choices (total number of ties/number of mutual ties): ", kl/summa)
print("total number of nodes/number of mutual ties :", kl/len(data))

