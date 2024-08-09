from crewai_tools.tools.scrape_website_tool.scrape_website_tool import ScrapeWebsiteTool

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
