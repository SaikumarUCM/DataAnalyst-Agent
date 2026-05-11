# LangGraph Agent

A data analytics AI agent built with LangGraph that can query databases, perform data analysis, and generate visualizations.

## Project Structure

```
langgraph-agent/
├── scout/                      # Main package
│   ├── __init__.py
│   ├── graph.py               # Core LangGraph workflow definition
│   ├── tools.py               # Tool implementations for agent actions
│   ├── env.py                 # Environment configuration
│   └── prompts/
│       ├── __init__.py
│       ├── prompts.py         # LLM prompts and instructions
│       └── scout.md           # Agent behavior documentation
├── frontend/                   # User interfaces
│   ├── chat_local.py          # Local chat interface
│   └── chat_deployed.py       # Deployed chat interface
├── sample_data/               # Sample datasets
│   ├── creators_2023.csv
│   ├── customers_2023.csv
│   └── transactions_2023_2024.csv
├── static/                    # Static assets
├── pyproject.toml             # Project configuration and dependencies
├── langgraph.json             # LangGraph configuration
├── Dockerfile                 # Container definition
└── README.md
```

## Design Architecture

### Agent Graph Structure

The agent uses LangGraph's StateGraph pattern to implement a multi-step workflow:

1. **State Management** (`ScoutState`)
   - Maintains message history for conversation context
   - Stores chart JSON data for visualizations
   - Uses Pydantic models for type safety

2. **Core Workflow**
   - **Assistant Node**: Processes messages using LLM with bound tools
   - **Tool Router**: Determines whether to invoke tools or end conversation
   - **Tool Node**: Executes database queries and visualization generation
   - **Conditional Edges**: Routes between nodes based on LLM output

3. **Tool System**
   - `query_db`: Execute SQL queries against the database
   - `generate_visualization`: Create interactive charts and plots
   - Structured tool definitions with docstrings for LLM understanding

4. **Message Flow**
   - HumanMessage → LLM Processing → Tool Calls (if needed) → AIMessage Response

### LLM Integration

- Uses ChatOpenAI with gpt-4.1-mini-2025-04-14
- Function calling enabled for deterministic tool invocation
- System prompts guide agent behavior and response format

### Data Layer

- SQL/PostgreSQL database queries
- Pandas DataFrames for data manipulation
- Plotly for interactive visualization generation

## Skills & Technologies Used

### Core Technologies

- **LangGraph**: Agentic workflow orchestration and state management
- **LangChain**: LLM integration and tool abstractions
- **OpenAI API**: Large Language Model backbone

### Backend Technologies

- **Python 3.12+**: Core programming language
- **Pydantic**: Data validation and schema definition
- **SQLAlchemy**: SQL toolkit and ORM
- **Pandas**: Data analysis and manipulation
- **Plotly**: Interactive data visualization

### Software Architecture

- **State Management**: Persistent conversation context with Pydantic models
- **Conditional Routing**: Dynamic graph routing based on LLM outputs
- **Tool Integration**: Function calling for deterministic agent actions
- **Checkpoint System**: Memory-based state persistence

### Development & Deployment

- **uv**: Fast Python package manager
- **Docker**: Containerization for consistent deployment
- **Langgraph API**: Server and deployment infrastructure
- **Frontend Frameworks**: Python-based chat interfaces

### Design Patterns

- **Agent Pattern**: Autonomous decision-making with tools
- **State Machine Pattern**: Conditional workflow routing
- **Tool Use Pattern**: LLM-guided function invocation
- **Message-based Architecture**: Conversational state management

### 7. Create a Render account (optional)

Render is used for deploying the LangGraph server. This is completely optional but highly recommended as it makes it easy to deploy your LangGraph applications. You can create a free account at [render.com](https://render.com/).

## Deployment

The deployment is going to leverage the Langgraph CLI which allows us to create a Dockerfile for our Langgraph server. This has already been done for you in the root directory. This Dockerfile will be used by the Render web service to build and deploy the Langgraph server. The web service will have a CI/CD pipeline that will automatically build and deploy the Langgraph server whenever you push to the main branch. To deploy your agent, first ensure you've published your project to Github and linked your Github to Render. Then you can simply follow along this [YouTube Episode](https://youtu.be/SGt786ne_Mk) where we take the agent that we've built here and deploy the fully-featured Langgraph Server API to serve your agent from anywhere!
