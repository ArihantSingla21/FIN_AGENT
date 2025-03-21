from phi.agent import Agent
import openai
import phi.api
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from dotenv import load_dotenv
import os
import phi 
from phi.playground import Playground, serve_playground_app




load_dotenv()

phi.api = os.getenv('PHI_API_KEY')


## web search agent 
web_search_agent = Agent(
    agent = "web_search_agent",
    role = "search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = ["always include the source url in your response"],
    show_tool_calls = True,
    markdown = True
)

## financial agent 
financial_agent = Agent(
    agent = "financial_agent",
    role = "financial analyst",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True
    )],
    instructions = ["use table to display the information"],
    show_tool_calls = True,
    markdown = True
)

app = Playground(
    agents = [web_search_agent, financial_agent],
).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)


