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

## Example Agent Interaction

The following example demonstrates the agent using Strands tool calling to investigate a smart-building issue using synthetic operational data.

### User Prompt

```text
Why is meeting_room_204 unusually warm? Use the available building data.
```

### Agent Tool Call

```text
Tool: get_zone_status
Zone: meeting_room_204
```

The tool retrieves the current operational state:

```text
Temperature:    26.8°C
Setpoint:       22.0°C
Occupancy:      6
HVAC Status:    fault
Active Alarm:   VAV-204 airflow fault
Lighting:       on
Access Status:  normal
```

### Grounded AI Response

```text
meeting_room_204 is unusually warm due to an HVAC fault.

The current temperature is 26.8°C compared with a 22.0°C setpoint,
which is 4.8°C above target.

The HVAC system reports an active "VAV-204 airflow fault." This indicates
that the VAV unit is not properly delivering conditioned air to the room,
preventing the zone from reaching its target temperature.

The recommended next step is to have HVAC maintenance investigate
VAV-204 and verify airflow after the fault is resolved.
```

This demonstrates the core agent workflow:

```text
User Question
     ↓
Strands Agent
     ↓
get_zone_status Tool
     ↓
Synthetic Building Data
     ↓
Amazon Bedrock Foundation Model
     ↓
Grounded Operational Response
```

> All building data shown in this example is synthetic and created specifically for this project.

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
- Strands tool-calling integration
- Synthetic smart-building zone-status tool
- Agent reasoning over live tool results
- Automated tests for Bedrock connectivity and tool-grounded responses

No proprietary building or customer data is used. All operational data in this repository is synthetic.

## Planned Capabilities

Development will progressively add:

- HVAC and environmental sensor tools
- Alarm investigation
- Lighting and energy analysis
- Access-control event analysis
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
│   │   └── building_tools.py
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── test_agent_connection.py
│   └── test_building_tool_agent.py
├── .env.example
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```

## Testing

The project includes automated integration tests covering:

- Strands → Amazon Bedrock model connectivity
- Agent tool calling against synthetic smart-building operational data
- Grounding AI responses in retrieved zone status, HVAC fault, and alarm data

Run the complete test suite with:

```bash
AWS_PROFILE=smartbuilding pytest tests/ -v
```

### Latest Verified Test Run

```text
platform darwin -- Python 3.12.10, pytest-9.1.1
collected 2 items

tests/test_agent_connection.py::test_agent_connection PASSED             [ 50%]
tests/test_building_tool_agent.py::test_agent_uses_building_data PASSED  [100%]

2 passed in 6.52s
```

The successful test run verifies that the application can:

1. Authenticate with AWS and invoke an Amazon Bedrock foundation model through a Strands agent.
2. Allow the agent to autonomously call the `get_zone_status` tool.
3. Retrieve synthetic operational building data.
4. Ground its response in actual retrieved values, including temperature, setpoint, and the `VAV-204 airflow fault`.

A successful test confirms that the application can authenticate with AWS, initialize the Strands agent, invoke the configured Bedrock foundation model, and receive a response.

## Development Status

🚧 **In active development**

The core FastAPI application, Strands agent framework, Amazon Bedrock model integration, AWS authentication, smart-building tool calling, and automated tests are operational.

The next milestone is expanding the building toolset with alarms, energy, maintenance history, and access-control data.