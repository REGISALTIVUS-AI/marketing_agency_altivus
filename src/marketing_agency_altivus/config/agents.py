import os
from textwrap import dedent

from crewai import Agent
from crewai_tools.tools.scrape_website_tool.scrape_website_tool import ScrapeWebsiteTool
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

# from langchain_openai import ChatOpenAI

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração das chaves de API (substitua com suas chaves reais)
openai_api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")
#
# gpt3_llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)
#
gpt4o_mini_llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)
#
llama3_70b = ChatGroq(model="llama3-70b-8192", api_key=groq_api_key)

# llm = Ollama(
#     model = "crewai-llama2",
#     base_url = "http://localhost:11434")


# ainew = ScrapeWebsiteTool(
#     website_url="https://www.artificialintelligence-news.com/"
# )
#
# forbes = ScrapeWebsiteTool(
#     website_url="https://www.forbes.com/ai/"
# )

def create_scrape_tools(urls):
    tools = []
    for url in urls:
        tool = ScrapeWebsiteTool(website_url=url)
        tools.append(tool)
    return tools


urls = [
    "https://www.artificialintelligence-news.com/"
    "https://www.forbes.com/ai/"
]

scrape_tools = create_scrape_tools(urls)

# Divide e organiza as tarefas
planejador = Agent(
    role="Planejador de postagem",
    goal="Planejar conteúdo envolvente para instagram sobre {topic}",
    backstory="Você está trabalhando no planejamento de {n} posts para o instagram "
              "sobre o tema: {topic}. "
              "Você coleta informações que ajudam o "
              "público se informar sobre {topic}. "
              "Seu trabalho é a base para que "
              "o Pesquisador de Conteúdo procure na web sobre {topic}.",
    verbose=True,
    llm=gpt4o_mini_llm,
    # max_rpm=1,
    allow_delegation=False
)

estrategista_de_conteudo = Agent(
    role='Estrategista',
    goal=' Criar um calendário de postagens com os '
         ' melhores horários de postagem para cada dia da semana. '
         ' baseado em sua experiência sobre {topic}. '
    ,
    verbose=True,
    backstory="Você é um pesquisador experiente, sempre em busca das últimas tendências e informações relevantes sobre {topic}.",
    llm=gpt4o_mini_llm,
    # tools=[Google Keyword Planner],
    allow_delegation=False
)

# Vai explorar a internet
pesquisador = Agent(
    role='Pesquisador',
    goal='Pesquisar tendências para postagens sobre {topic} na área '
         'de tecnologia com base no planejamento do Planejador. '
         'Seu trabalho é a base para que '
         'o escritor possa escrever {n} posts sobre {topic}',
    verbose=True,
    backstory="Você é um pesquisador experiente, sempre em busca das últimas tendências e informações relevantes sobre {topic}.",
    llm=gpt4o_mini_llm,
    # max_rpm=1,
    tools=scrape_tools,
    allow_delegation=False
)

#É importante falar a lingua de saída para escrita
escritor = Agent(
    role='Escritor',
    goal='Escrever {n} postagens cativantes em português do Brasil para o Instagram sobre {topic} com no mínimo 250 palavras e no máximo 350 palavras.'
         'Seu trabalho é a base para que o fotografo possa escrever prompts de imagens para os {n} posts',
    backstory="Você é um escritor criativo, capaz de transformar informações em conteúdo atraente para postagens no Instagram.",
    llm=gpt4o_mini_llm,
    verbose=True,
    # max_rpm=1,
    allow_delegation=False
)

fotografo = Agent(
    role='Fotógrafo',
    goal='Escrever prompts de imagens para as {n} postagens para gerar imagens cativantes para o Instagram sobre {topic}.',
    backstory=dedent("""Você é um fotógrafo criativo,
                        capaz de transformar informações em imagens e escrever prompts
                        de imagens atraentes para postagens no Instagram."""),
    verbose=True,
    llm=gpt4o_mini_llm,
    # max_rpm=1,
    allow_delegation=False
)

#Supervisiona o trabalho e revisa o resultado final
gerente = Agent(
    role='Gerente de postagens',
    goal=dedent("""Supervisione o trabalho de uma equipe de postagens no Instagram. Você é bem crítico em relação
            ao que vai ser postado no Instagram da empresa de notícias na área da tecnologia.
            Você delegará tarefas à sua equipe e fará perguntas esclarecedoras
            para revisar e aprovar as {n} posts sobre {topic} que foram solicitadas pela direção da empresa."""),
    verbose=True,
    backstory=dedent("""Você é um gerente experiente, sempre em busca das últimas tendências e informações relevantes.
                 Você está trabalhando com uma nova demanda e faz com que sua equipe realize o trabalho da
                 melhor forma possível."""),
    llm=gpt4o_mini_llm,
    # max_rpm=1,
)