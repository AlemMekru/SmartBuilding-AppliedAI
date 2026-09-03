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
- Amazon Bedrock foundation-model integration
- Configurable Bedrock model selection
- Successful end-to-end Strands → Amazon Bedrock model invocation
- Automated Bedrock agent connectivity testing with pytest
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

- Python 3.12
- FastAPI
- Strands Agents
- Amazon Bedrock
- AWS
- Pydantic
- pytest

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
│   └── test_agent_connection.py
├── .env.example
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```

## Testing

The project includes an integration test that verifies connectivity between the Strands agent and Amazon Bedrock.

Run the test using:

```bash
AWS_PROFILE=smartbuilding pytest tests/test_agent_connection.py -v
```

A successful test confirms that the application can authenticate with AWS, initialize the Strands agent, invoke the configured Bedrock foundation model, and receive a response.

## Development Status

🚧 **In active development**

The core FastAPI application, Strands agent framework, Amazon Bedrock model integration, AWS authentication, and automated connectivity test are operational.

The next milestone is to give the agent its first smart-building tool, allowing it to retrieve and reason over synthetic operational data.