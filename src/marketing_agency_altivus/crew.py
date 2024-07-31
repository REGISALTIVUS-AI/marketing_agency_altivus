from crewai import Crew, Process

from marketing_agency_altivus.config.agents import planejador, pesquisador, escritor, fotografo, gerente, \
    estrategista_de_conteudo
from marketing_agency_altivus.config.tasks import revisao_task, criacao_imagem_task, escrita_task, pesquisa_task, \
    plano_task, estrategia_task

# Uncomment the following line to use an example of a custom tool
# from marketing_agency_altivus.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

#Organiza uma ordem de execução tanto de agentes quanto de tarefas, process define que é sequencial.
crew = Crew(
    agents=[planejador, estrategista_de_conteudo, pesquisador, escritor, fotografo, gerente],
    tasks=[plano_task, estrategia_task, pesquisa_task, escrita_task, criacao_imagem_task, revisao_task],
    process=Process.sequential,
    verbose=2,
    memory=True
)


