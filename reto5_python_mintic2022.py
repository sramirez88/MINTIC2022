import csv, json

def solucion():
    
    with open('analisis_archivo.csv','w',newline='') as csvfile:
        csvfile.write('Fecha analizada\tComportamiento de la accion\tabs Diferencia Close-Open\n')
        Date=[]
        Open=[]
        Close=[]
        Dif=[]
        Vabs=[]
        Volume=[]
        dic={}
        archivo=open('JandJ.csv','r')
        lines=archivo.read().splitlines()
        lines.pop(0)#elimina el encabezado
        for l in lines:
            linea=l.split(',')
            Date.append(linea[0])
            Open.append(linea[1])
            Close.append(linea[4])
            Volume.append(int(linea[6]))
        for i in range(len(lines)):
            resta=float(Close[i])-float(Open[i])
            Vabs.append(abs(resta))
            if resta>0:
                Dif.append('SUBE')
            if resta<0:
                Dif.append('BAJA')
            if resta==0:
                Dif.append('ESTABLE')
            csvfile.write('%s\t' % Date[i])
            csvfile.write('%s\t' % Dif[i])
            csvfile.write('%s\n' % Vabs[i])  
        csvfile.close()
        archivo.close()
        for i in range(len(Date)):
            if Volume[i]==min(Volume):
                dic['date_lowest_volume']=Date[i]
                dic['lowest_volume']=min(Volume)
            if Volume[i]==max(Volume):    
                dic['date_highest_volume']=Date[i]
                dic['highest_volume']=max(Volume)
                dic['mean_volume']=sum(Volume)/len(Volume)
            if Vabs[i]==max(Vabs):
                dic['date_greatest_difference']=Date[i]
                dic['greatest_difference']=max(Vabs)
        with open('detalles.json','w') as datos:
            json.dump(dic,datos)
    
    
    
