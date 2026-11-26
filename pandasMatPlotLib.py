import pandas as pd
import matplotlib.pyplot as plt

def gerar_Grafico(op, name_op, aluno):
    plt.figure(figsize=(8, 4))
    df_aluno = df[df["Aluno"] == aluno]  
    plt.plot(df_aluno["Mês"].str[:3], df_aluno[name_op], marker="o", markersize=10, mfc='red', mec='black', label=aluno, linestyle="-.")
    plt.title(f"{name_op} por mês")
    plt.xlabel("Período")
    plt.ylabel(op)
    plt.ylim(0, 4)
    plt.grid(True, linestyle=":", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()
    
df = pd.read_excel("controle_entregas_matematica_ficticio.xlsx", skiprows=3)
df.columns = df.columns.str.strip()


print("== escolha uma opção == \n")
Series_Alunos = df["Aluno"].drop_duplicates()
for i, aluno in enumerate(Series_Alunos, start=1):
    print(i, " - ", aluno)
    
print(" $ escolha um aluno $")
aluno_id = int(input("Resposta: "))

if(aluno_id <= len(Series_Alunos)):
    for i, aluno in enumerate(Series_Alunos, start=1):
        if aluno_id == i:
            print(aluno, i)
            print("$ digite uma tipo de análise $")
            print("1 - analisar entregas por mês")
            print("2- analisar entregas atrasadas por mês")
            resp = int(input("resposta: "))
            if resp == 1:
                gerar_Grafico("entrega", "Atividades entregues", aluno)
            elif resp == 2:
                gerar_Grafico("atraso", "Entregues com atraso", aluno)
            else:
                print("id de análise não existente :/")
else:
    print("esse id de aluno não existe :/")
    
             
        


