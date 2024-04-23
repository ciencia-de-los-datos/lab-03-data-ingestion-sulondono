"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd    


def ingest_data():

    data2=[]

    with open('clusters_report.txt', 'r') as file: 
        headers = file.readline().strip().split() + file.readline().strip().split()

        headers.insert(3, 'palabras')
        headers.insert(4, 'clave')
        headers.insert(7, 'palabras')
        headers.insert(8, 'clave')
        headers.pop(15)
        headers.pop(14)
        headers.pop(13)
        headers.pop(12)

        headers = ['cluster']+['_'.join(headers[i:i+4]).lower() for i in range(1, len(headers), 4)]

        for line in file:            
            col=line.split()

            if line.strip() == '---------------------------------------------------------------------------------------------------------------------':
                continue  
            
            elif len(col)>0:
                if len(col[0])<=2:
                    cluster=int(col[0])
                    cantidad_de_palabras_clave=int(col[1])
                    flotante_col2=col[2].replace(',', '.')
                    porcentaje_de_palabras_clave=float(flotante_col2)
                    principales_palabras_clave=' '.join(col[4:])

                    data2.append([cluster, cantidad_de_palabras_clave, porcentaje_de_palabras_clave, principales_palabras_clave])
                else:
                    palabras_clave_limpia=[item.replace('.','') for item in col]
                    principales_palabras_clave=' '.join(palabras_clave_limpia)
                    data2[len(data2)-1][3] += ' ' + principales_palabras_clave 

        df=pd.DataFrame(data2, columns=headers)
        return df


print(ingest_data())
