#!/usr/bin/env python
from marketing_agency_altivus.crew import crew
from datetime import datetime

result = crew.kickoff(inputs={
    'topic': 'Inteligência Artificial e Agentes Inteligêntes',
    'n': 1})

# Converter o resultado para string antes de escrever no arquivo
result_str = str(result)

# Salvar o resultado em um arquivo
# current_date = datetime.now().strftime("%Y-%m-%d")
# filename = f"posts-{current_date}.txt"
# with open(filename, 'w', encoding='utf-8') as file:
#     file.write(result_str)