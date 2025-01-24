from typing import Any

from pydantic import BaseModel
import yamling

from llmling_agent import Agent
from llmling_agent.models.agents import AgentsManifest


class Result(BaseModel):
    """Simple structured response."""

    main_point: str
    is_positive: bool


AGENT_CONFIG = """
agents:
    summarizer:
        model: openai:gpt-4o-mini
        system_prompts:
            - Summarize text in a structured way.
"""


async def example_structured_response():
    # for manifests with uniform agents, the manifest itself can be typed.
    manifest = AgentsManifest[Any, Any].model_validate(yamling.load_yaml(AGENT_CONFIG))
    async with Agent[Any].open_agent(manifest, "summarizer", result_type=Result) as agent:
        result = await agent.run("I love this new feature!")
        summary = result.data
        print(f"Main point: {summary.main_point}")
        print(f"Is positive: {summary.is_positive}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(example_structured_response())
