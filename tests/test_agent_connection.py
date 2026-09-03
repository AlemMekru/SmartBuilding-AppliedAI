from app.agents.building_agent import create_building_agent


def test_agent_connection():
    agent = create_building_agent()
    response = agent("Reply with exactly: Smart Building AI connected")

    assert "Smart Building AI connected" in str(response)