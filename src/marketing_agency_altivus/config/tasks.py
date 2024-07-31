from textwrap import dedent

from crewai import Task

from marketing_agency_altivus.config.agents import planejador, pesquisador, escritor, fotografo, gerente

plano_task = Task(
    description=(
        "1. Priorize as últimas tendências, principais 'players', "
        "e notícias relevantes sobre {topic}.\n"
        "2. Identifique o público-alvo, considerando "
        "seus interesses e pontos de dor.\n"
        "3. Desenvolva um plano de conteúdo detalhado, incluindo "
        "uma introdução, pontos principais e um chamado à ação.\n"
        "4. Inclua palavras-chave de SEO e dados ou fontes relevantes."
    ),
    expected_output="Um documento de plano de conteúdo para {n} posts sobre {topic} "
                    "com um esboço, análise do público, "
                    "palavras-chave de SEO e recursos.",
    agent=planejador,
    verbose=2
)

pesquisa_task = Task(
    description="Pesquise as últimas tendências sobre {topic}.",
    expected_output="Um relatório detalhado sobre as tendências mais recentes sobre {topic} na área de tecnologia.",
    agent=pesquisador,
    verbose=2
)

escrita_task = Task(
    description=dedent("""Escreva {n} postagens envolventes em português do Brasil com base nas tendências 
    pesquisadas sobre {topic} com no mínimo 250 palavras e no máximo 350 palavras cada. Cada post deve ser formatado 
    como: \n\nPOST:\ntexto do post em português do brasil \n\nPROMPT:\nPrompt da imagem desse post\n\n"""),
    expected_output="{n} postagens de Instagram bem escritas, atraentes e em português do Brasil, formatadas conforme "
                    "especificado para o tópico {topic}.",
    agent=escritor,
    verbose=2
)

criacao_imagem_task = Task(
    description="Crie {n} prompts para criar uma imagem atraente para acompanhar a postagem no Instagram sobre {topic}.",
    expected_output="{n} prompts de alta qualidade adequados para o Instagram based in {topic}.",
    agent=fotografo,
    verbose=2
)

revisao_task = Task(
    description=dedent("""Revise as {n} escritas e prompts de imagens
                          para as {n} postagens do cliente e garanta
                          que as informações de cada postagem estejam organizadas, sem erros e cativantes
                          em português do Brasil sobre {topic}.
                          Certifique-se de que cada post está formatado como:
                          \n\nPOST:\ntexto do post em português do brasil
                          \n\nPROMPT:\nPrompt da imagem desse post\n\n"""),
    expected_output="{n} textos e prompts de imagens organizados por post, revisados e prontos para serem publicados "
                    "em português do Brasil, formatados conforme especificado.",
    agent=gerente,
    verbose=2
)
