# Introduction to Generative AI on Azure through sample notebooks

This repository contains a learning path for working with Azure AI Foundry services, focusing on Retrieval-Augmented Generation (RAG), Azure AI Agents, and other advanced AI capabilities.

## Overview

The learning path demonstrates building AI solutions using Azure AI Foundry services, progressing from setting up data stores and indices to creating intelligent agents with various capabilities. The notebooks are designed to be worked through sequentially, with each building upon the previous examples.

## Prerequisites

- Azure subscription
- Azure AI Foundry project created
- Python 3.10+ environment

## Setup Instructions

1. Clone the repository
2. Create a Python virtual environment:
   ```
   # Using conda
   conda create -n azure-ai-foundry python=3.10
   conda activate azure-ai-foundry
   
   # Or using venv
   python -m venv azure-ai-foundry
   # On Windows
   azure-ai-foundry\Scripts\activate
   # On Linux/macOS
   source azure-ai-foundry/bin/activate
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following configuration (replace with your own values):
   ```
   # Project configuration
   SUB_ID=<your-azure-subscription-id>
   RG_NAME=<your-resource-group-name>
   AZURE_PROJECT_NAME=<your-project-name>

   # Project connections
   PROJECT_CONNECTION_STRING=<your-project-connection-string>
   OAI_CONNECTION_NAME=<your-openai-connection-name>
   AI_CONNECTION_NAME=<your-ai-connection-name>
   SEARCH_CONNECTION_NAME=<your-search-connection-name>
   BING_CONNECTION_NAME=<your-bing-connection-name>

   # Azure OpenAI Service
   chatModel=gpt-4o
   embeddingModel=text-embedding-ada-002
   AZURE_OPENAI_API_VERSION=2025-01-01-preview
   TAVILY_API_KEY=<your-tavily-api-key>

   # Azure AI Search
   SEARCH_INDEX_NAME=test-index

   # Storage Account (for document storage)
   storage_container=test
   storage_base_url=<your-storage-base-url>
   storage_connection_string=<your-storage-connection-string>

   # Application Insights (for telemetry)
   APPLICATIONINSIGHTS_CONNECTION_STRING=<your-app-insights-connection-string>
   AZURE_SDK_TRACING_IMPLEMENTATION=opentelemetry
   ```

## Learning Path Structure

The notebooks are designed to be run in order:

1. **01-create-index.ipynb**: Creates a vector search index for storing document embeddings
   - Sets up document processing pipeline
   - Performs document chunking and embedding generation
   - Indexes data in Azure AI Search

2. **02-rag.ipynb**: Demonstrates Retrieval-Augmented Generation
   - Uses the search index to retrieve relevant information
   - Applies an intent-based search approach
   - Shows how to implement a complete RAG pattern with OpenAI

3. **03-azure-ai-agents-knowledge-tools.ipynb**: Shows integration with knowledge tools
   - Creates an agent with Bing knowledge grounding
   - Demonstrates managing agent threads and messages
   - Shows how to use knowledge tools for grounded responses

4. **04-azure-ai-agents-action-tools.ipynb**: Explores function-calling with agents
   - Implements custom function tools (web search, weather info)
   - Demonstrates the agent's ability to call external functions
   - Shows how to handle tool execution flow

5. **05-autogen-azure-ai-agents.ipynb**: Extends the agent capabilities with AutoGen
   - Advanced agent orchestration

## Dependencies

This project uses the following key libraries:
- Azure AI Projects SDK
- Azure AI Inference SDK
- LangChain and LangChain Components
- Azure AI Document Intelligence
- Azure AI Search
- Azure Monitor OpenTelemetry
- Tavily Python SDK
- Other supporting libraries for data processing and visualization

## References

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/)
- [Azure AI Agents Documentation](https://learn.microsoft.com/azure/ai-services/agents)
- [Azure AI Search Documentation](https://learn.microsoft.com/azure/search/)
- [Azure OpenAI Service Documentation](https://learn.microsoft.com/azure/ai-services/openai/)

## TODO
- In 01-create-index
    - Consolidate format_documents and convert_document
- Add Managed Identity to Notebooks
- Add Managed Identity to Foundry Connections