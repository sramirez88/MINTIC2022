import csv, json

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    with open('analisis_archivo.csv','w',newline='') as csvfile:
        csvfile.write('Fecha\tMean-Min-Max\tConcepto\n')
        Date=[]
        High=[]
        Low=[]
        Dif=[]
        Promedio=[]
        dic={}
        archivo=open('FB.csv','r')
        lines=archivo.read().splitlines()
        lines.pop(0)#elimina el encabezado
        for l in lines:
            linea=l.split(',')
            Date.append(linea[0])
            High.append(linea[2])
            Low.append(linea[3])
        
        for i in range(len(lines)):
            prom=(float(High[i])+float(Low[i]))/2
            Promedio.append(prom)
            if Promedio[i]<239:
                Dif.append('MUY BAJO')
            if Promedio[i]>=239 and Promedio[i]<265:
                Dif.append('BAJO')
            if Promedio[i]>=265 and Promedio[i]<291:
                Dif.append('MEDIO')
            if Promedio[i]>=291 and Promedio[i]<317:
                Dif.append('ALTO')
            if Promedio[i]>=317:
                Dif.append('MUY ALTO')
            csvfile.write('%s\t' % Date[i])
            csvfile.write('%s\t' % Promedio[i])
            csvfile.write('%s\n' % Dif[i])  
        csvfile.close()
        archivo.close()
        
        for i in range(len(Date)):
            if Promedio[i]==min(Promedio):
                dic['date_lowest_prom']=Date[i]
                dic['lowest_prom']=min(Promedio)
            if Promedio[i]==max(Promedio):    
                dic['date_highest_prom']=Date[i]
                dic['highest_prom']=max(Promedio)
        with open('detalles.json','w') as datos:
            json.dump(dic,datos)
    
    
    
    
    
