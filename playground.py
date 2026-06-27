from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi.api
import os
import phi
##uses fastapi to serve the playground app
from phi.playground import Playground, serve_playground_app

from dotenv import load_dotenv

load_dotenv()

phi_api = os.getenv("PHI_API_KEY")

##websearch agent will interact with another tool duckduckgo to get information from the web
websearch_agent = Agent(
    name="websearch_agent",
    role="search the web for information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[
        DuckDuckGo()
    ],
    instructions = ["Always include sources for your answers."],
    show_tool_calls=True,
    markdown=True,
)

#financial agent will interact with another tool yfinance to get stock data and perform financial analysis
financial_agent = Agent(
    name="financial_agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    role="analyze financial data and provide insights",
    tools=[
        YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True , company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

app=Playground(agents=[websearch_agent, financial_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)