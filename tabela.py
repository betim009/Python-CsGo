import pandas as pd
from request_api import (
    get_random_weapon,
    get_random_class,
    get_specific_skin,
    get_random_skin,
)

def tabela(query, painel):
    
    if painel == "A" or "a":
        search_query = get_random_weapon(query)
        df = pd.DataFrame([search_query])
        print(df)
