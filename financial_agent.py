from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()



##websearch agent will interact with another tool duckduckgo to get information from the web
websearch_agent = Agent(
    name="websearch_agent",
    role="search the web for information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[
        DuckDuckGo()
    ],
    instructions = ["Always include sources for your answers."],
    show_tools_calls=True,
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

multi_ai_agent = Agent(
    team=[websearch_agent, financial_agent],
    model=Groq(id="llama-3.3-70b-versatile"),

    instructions=["always include sources for your answers.","Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendations for AAPL stock and provide a brief overview of the company's recent news for NVDA.",stream=True)

