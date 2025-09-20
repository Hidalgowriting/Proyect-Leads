import requests
from bs4 import BeautifulSoup
import pandas as pd

# Ejemplo: buscar leads de empresas (esto es un demo sencillo)
def get_leads():
    leads = [
        {"name": "John Doe", "email": "john@example.com", "company": "ABC Pools", "website": "https://abcpools.com"},
        {"name": "Maria Lopez", "email": "maria@cleanpools.com", "company": "Clean Pools Miami", "website": "https://cleanpools.com"}
    ]
    df = pd.DataFrame(leads)
    df.to_csv("leads.csv", index=False)
    print("Leads guardados en leads.csv")

if __name__ == "__main__":
    get_leads()
