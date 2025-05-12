import requests
from transformData import transform_and_load 

url = "https://olinda.bcb.gov.br/olinda/service/PTAX/version/v1/odata/DollarRatePeriod(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='01-09-2025'&@dataFinalCotacao='01-16-2025'&$top=100&$format=json"

def extract():
    
    try:
        response = requests.get(url)

        if response.status_code == 200:
            
            data = response.json()

            rates = data.get("value", [])
            
            return rates
        
        else:
            
            print(f"Erro ao acessar API. Código de status: {response.status_code}")
            
            return None
    
    except:
       
        print(f"Erro na requisição: {Exception}")
        
        return None
    

if __name__ == "__main__":
    rates = extract()
    resultados = transform_and_load(dados = rates)
    if resultados.empty:
        print("qlqr coisa")
    else:
        for resultado in resultados:
            print(resultado)
    
    