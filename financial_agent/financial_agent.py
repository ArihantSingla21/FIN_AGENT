import os
from dotenv import load_dotenv
from phi.agent import Agent 
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools 
from phi.tools.duckduckgo import DuckDuckGo


# Load environment variables from .env file first
load_dotenv()

# Get the API key from environment and set it
groq_api_key = os.getenv('GROQ_API_KEY')
if not groq_api_key:
    raise EnvironmentError("GROQ_API_KEY environment variable is not set")
os.environ['GROQ_API_KEY'] = groq_api_key


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

multi_ai_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team = [web_search_agent, financial_agent],
    instructions = [
        "you are a financial analyst, you are given a question and you need to answer it by searching the web and using the financial data",
        "always include the source url in your response",
        "display the information in a table"
    ],
    show_tool_calls = True,
    markdown = True
)

def main():
    try:
        # Example query with fixed typo
        query = "what is the stock price of apple? summarize the analyst recommendations and share the latest news for apple"
        response = multi_ai_agent.print_response(query)
        return response
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    main()








