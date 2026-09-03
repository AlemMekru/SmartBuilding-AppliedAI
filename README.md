# SmartBuilding-AppliedAI

Applied AI platform for smart building operations using AI agents, Amazon Bedrock, RAG, tool calling, and enterprise building data.

The project demonstrates how an AI agent can help building operators investigate HVAC, lighting, energy, and access-control issues by combining foundation models with operational data and enterprise tools.

## Architecture

<p align="center">
  <img src="app/assets/architecture.png" alt="SmartBuilding-AppliedAI Architecture" width="900">
</p>

## Example Use Cases

The platform is being designed to answer operational questions such as:

- Why is Meeting Room 204 unusually warm?
- Why is the third floor consuming unusually high energy?
- Show unusual after-hours access events.
- Are there active HVAC alarms affecting this zone?
- What maintenance history is relevant to this equipment?

## Current Implementation

The current implementation includes:

- Python 3.12 application environment
- FastAPI backend
- Health-check API
- Synthetic smart-building operational data
- Strands Agents integration
- Amazon Bedrock model integration
- Configurable Bedrock foundation-model selection
- AWS authentication using a local AWS profile
- Canada Central (`ca-central-1`) as the development region

No proprietary building or customer data is used. All operational data in this repository is synthetic.

## Planned Capabilities

Development will progressively add:

- HVAC and environmental sensor tools
- Alarm investigation
- Lighting and energy analysis
- Access-control event analysis
- Agent tool calling
- Retrieval-Augmented Generation (RAG)
- Equipment manuals and operational knowledge
- Role-based access controls
- AI guardrails
- Human approval for sensitive actions
- Audit logging
- Model usage and cost monitoring
- AI response evaluation and reliability testing

## Technology Stack

- Python
- FastAPI
- Strands Agents
- Amazon Bedrock
- AWS
- Pydantic

Additional AWS services will be introduced as the architecture evolves.

## Project Structure

```text
SmartBuilding-AppliedAI/
├── app/
│   ├── agents/
│   │   └── building_agent.py
│   ├── api/
│   ├── assets/
│   │   └── architecture.png
│   ├── data/
│   │   └── building_state.py
│   ├── models/
│   ├── monitoring/
│   ├── rag/
│   ├── security/
│   ├── services/
│   ├── tools/
│   ├── __init__.py
│   └── main.py
├── tests/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Development Status

🚧 **In active development**

The core FastAPI application and Strands/Amazon Bedrock agent integration are configured. The next milestone is connecting the agent to synthetic smart-building tools and operational data.

> Amazon Bedrock model invocation is pending completion of AWS account verification.