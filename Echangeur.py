print("Echangeur")
Tce=input("Entrez la température chaud Tce: ")
Tcs=input("Entrez la température chaud Tcs: ")
Tfe=input("Entrez la température froid Tfe: ")
Cpc=input("Entrez la capacité calorique Cps: ")
Cpf=input("Entrez la capacité calorique Cpf: ")
mc=input("Entrez le débit massique mc: ")
mf=input("Entrez le débit massique mf: ")
try:
    Tce = float(Tce)
    Tcs = float(Tcs)
    Tfe = float(Tfe)
    Cpc = float(Cpc)
    Cpf = float(Cpf)
    mc = float(mc)
    mf = float(mf)
    Tfs=((mc*Cpc*(Tcs-Tce))/(mc*Cpf))+Tfe
    print("Tfs ", Tfs)
except:
    print("erreur")