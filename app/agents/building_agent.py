import os

import boto3
from strands import Agent
from strands.models import BedrockModel


def create_building_agent() -> Agent:
    session = boto3.Session(
        profile_name=os.getenv("AWS_PROFILE", "smartbuilding"),
        region_name=os.getenv("AWS_REGION", "ca-central-1"),
    )

    model = BedrockModel(
        boto_session=session,
        model_id=os.getenv(
            "BEDROCK_MODEL_ID",
            "global.anthropic.claude-haiku-4-5-20251001-v1:0",
        ),
        temperature=0.2,
    )

    return Agent(
        model=model,
        system_prompt=(
            "You are an AI assistant for smart building operations. "
            "You help operators investigate HVAC, lighting, energy, "
            "and access-control issues using approved building data and tools."
        ),
    )