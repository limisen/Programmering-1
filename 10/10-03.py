from random import sample

def listig(x):
    """ Slumpar 100 tal i intervallet 1-1000 och sedan beräknar största, minsta och medelvärdet för att sedan skriva ut det """
    default_list = sample([i for i in range(1,1000)], x)
    
    sorted_list = sorted(default_list)
    lowest = min(sorted_list)
    biggest = max(sorted_list)

    for i in range(0,len(sorted_list)):
        x = sorted_list[i] + sorted_list[i]
    avg = x // len(sorted_list)

    print('Minst: {0}'.format(lowest))
    print('Störst: {0}'.format(biggest))
    print('Medel: {0}'.format(avg))

print(listig(10))

#Är detta ok?