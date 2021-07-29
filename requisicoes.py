import csv
from datetime import datetime
from tkinter import*
import time
print("Registro de req's")
import os

def salvar_req(num_req,planilha):
    with open(planilha, newline='',mode='a') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(num_req)

planilhas = ['requisicoes.csv']

for name in planilhas:
    if (os.path.exists(name) == False):
        salvar_req(['Data','Tipo','Número da Requisição','valor'],name)

arquivo = 'requisicoes.csv'

acesso_time = os.path.getatime(arquivo)
hora_convert = time.ctime(acesso_time)
print("seu ultimo acesso foi: ",hora_convert)

while(True):

    entrada = str(input("Entre com o número da req: "))
    valor = int(input("Entre com o valor: "))
    if len(entrada) == 6:
        print(entrada)
        dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        row = [dt, 'Modelo 1', entrada,valor]
        salvar_req(row,'requisicoes.csv')
        print("Req CAT adicionada com sucesso.")


    elif len(entrada) == 4:
        print(entrada)
        dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        row = [dt, 'Modelo 2', entrada,valor]
        salvar_req(row, 'requisicoes.csv')
        print("Req MERCADO adicionada com sucesso. ")

    elif len(entrada) == 3:
        print(entrada)
        dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        row = [dt, 'Modelo 3', entrada,valor]
        salvar_req(row, 'requisicoes.csv')
        print("Req OS adicionada com sucesso. ")

    continuar = input("Deseja continuar? S/N :")
    if continuar == "S":
        pass
    else:
        break

