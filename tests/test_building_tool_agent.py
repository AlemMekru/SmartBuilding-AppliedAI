from app.agents.building_agent import create_building_agent


def test_agent_uses_building_data():
    agent = create_building_agent()

    response = agent(
        "Why is meeting_room_204 unusually warm? "
        "Use the available building data."
    )

    text = str(response).lower()

    assert "26.8" in text
    assert "22.0" in text or "22" in text
    assert "vav-204" in text
    assert "airflow fault" in text