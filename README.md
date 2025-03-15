# Financial and PDF Assistant

A powerful AI-powered application that combines financial analysis and PDF document processing capabilities using Groq's LLM.

## Features

### 1. Financial Agent
- Real-time stock price tracking
- Analyst recommendations analysis
- Company fundamentals research
- Latest financial news aggregation
- Web search integration for comprehensive market research

### 2. PDF Assistant
- PDF document analysis
- Knowledge base integration
- Persistent chat history
- Interactive CLI interface
- Vector database storage for efficient document retrieval

## Prerequisites

- Python 3.8+
- PostgreSQL with pgvector extension
- Groq API key
- PhiData API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ArihantSingla21/FIN_AGENT.git
cd https://github.com/ArihantSingla21/FIN_AGENT.git
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
.\venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables in `.env`:
```env
GROQ_API_KEY=your_groq_api_key
PHIDATA_API_KEY=your_phidata_api_key
```

5. Set up PostgreSQL:
```bash
# Create database and user
createdb ai
createuser ai -P  # Set password to 'ai'

# Enable pgvector extension in PostgreSQL
psql -d ai -c 'CREATE EXTENSION IF NOT EXISTS vector;'
```

## Usage

### Financial Agent

The financial agent provides real-time financial analysis and market insights:

```bash
python financial_agent/financial_agent.py
```

Example query:
```
"what is the stock price of apple? summarize the analyst recommendations and share the latest news"
```

### PDF Assistant

The PDF assistant helps analyze PDF documents and maintain conversation history:

```bash
python pdf_assistant/pdf_assistant.py
```

### Interactive Playground

Launch the interactive web interface:

```bash
python financial_agent/playground.py
```

## Project Structure

```
.
├── financial_agent/
│   ├── financial_agent.py    # Main financial analysis agent
│   └── playground.py         # Interactive web interface
├── pdf_assistant/
│   └── pdf_assistant.py      # PDF processing and analysis
├── requirements.txt          # Project dependencies
├── .env                     # Environment variables
└── README.md               # Project documentation
```

## Dependencies

- `groq`: Groq LLM API client
- `phidata`: AI agent framework
- `yfinance`: Financial data retrieval
- `pgvector`: Vector similarity search in PostgreSQL
- `duckduckgo-search`: Web search capabilities
- `fastapi` & `uvicorn`: Web server for playground
- `typer`: CLI interface
- `pypdf`: PDF processing
- Full list in `requirements.txt`

## Configuration

The application uses PostgreSQL for storage with the following default configuration:
- Host: localhost
- Port: 5532
- Database: ai
- Username: ai
- Password: ai

Modify the `db_url` in the respective files if you need different settings.

## Features in Detail

### Financial Agent
- **Web Search**: Integrated DuckDuckGo search for market research
- **Stock Analysis**: Real-time stock data and financial metrics
- **News Aggregation**: Latest company and market news
- **Analyst Insights**: Professional market analysis and recommendations

### PDF Assistant
- **Document Processing**: Extract and analyze PDF content
- **Vector Search**: Efficient document querying using pgvector
- **Conversation History**: Persistent chat storage
- **Interactive CLI**: User-friendly command-line interface

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

[Your chosen license]

## Acknowledgments

- Groq for their powerful LLM API
- PhiData for the AI agent framework
- All other open-source contributors
