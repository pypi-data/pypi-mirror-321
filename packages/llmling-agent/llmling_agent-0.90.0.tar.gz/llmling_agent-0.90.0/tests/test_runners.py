"""Tests for AgentPool functionality."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pytest

from llmling_agent.delegation import AgentPool
from llmling_agent.models import AgentConfig, AgentsManifest
from llmling_agent.responses import InlineResponseDefinition, ResponseField


if TYPE_CHECKING:
    from llmling_agent.agent.agent import Agent

MODEL = "openai:gpt-4o-mini"


@pytest.mark.asyncio
async def test_agent_pool_conversation_flow(test_model):
    """Test conversation flow maintaining history between messages."""
    fields = {"message": ResponseField(type="str", description="Test message")}
    defn = InlineResponseDefinition(description="Basic test result", fields=fields)
    cfg = AgentConfig(name="Test Agent", model=test_model, result_type="BasicResult")
    agents = {"test_agent": cfg}
    agent_def = AgentsManifest[Any, Any](responses={"BasicResult": defn}, agents=agents)

    async with AgentPool(agent_def, agents_to_load=["test_agent"]) as pool:
        # Get agent directly for conversation
        agent: Agent[Any] = pool.get_agent("test_agent")

        # Run multiple prompts in sequence
        responses = []

        for prompt in ["Hello!", "How are you?"]:
            result = await agent.run(prompt)
            responses.append(result)

        assert len(responses) == 2  # noqa: PLR2004
        assert all(str(r.data) == "Test response" for r in responses)


@pytest.mark.asyncio
async def test_agent_pool_validation():
    """Test AgentPool validation and error handling."""
    fields = {"message": ResponseField(type="str", description="Test message")}
    defn = InlineResponseDefinition(description="Basic test result", fields=fields)
    cfg = AgentConfig(name="Test Agent", model=MODEL, result_type="BasicResult")
    agents = {"test_agent": cfg}
    agent_def = AgentsManifest[Any, Any](responses={"BasicResult": defn}, agents=agents)

    # Test initialization with non-existent agent
    with pytest.raises(ValueError, match="Unknown agents"):
        AgentPool(agent_def, agents_to_load=["nonexistent"])

    # Test getting non-existent agent
    async with AgentPool(agent_def) as pool:
        with pytest.raises(KeyError, match="nonexistent"):
            pool.get_agent("nonexistent")


@pytest.mark.asyncio
async def test_agent_pool_team_errors(test_model):
    """Test error handling in team tasks."""
    fields = {"message": ResponseField(type="str", description="Test message")}
    defn = InlineResponseDefinition(description="Basic test result", fields=fields)
    cfg = AgentConfig(name="Test Agent", model=test_model, result_type="BasicResult")
    agents = {"test_agent": cfg}
    agent_def = AgentsManifest[Any, Any](responses={"BasicResult": defn}, agents=agents)

    async with AgentPool(agent_def, agents_to_load=["test_agent"]) as pool:
        # Test with non-existent team member
        with pytest.raises(KeyError, match="nonexistent"):
            pool.create_group(["test_agent", "nonexistent"])


@pytest.mark.asyncio
async def test_agent_pool_cleanup():
    """Test proper cleanup of agent resources."""
    fields = {"message": ResponseField(type="str", description="Test message")}
    defn = InlineResponseDefinition(description="Basic test result", fields=fields)
    cfg = AgentConfig(name="Test Agent", model=MODEL, result_type="BasicResult")
    agents = {"test_agent": cfg}
    agent_def = AgentsManifest[Any, Any](responses={"BasicResult": defn}, agents=agents)

    # Use context manager to ensure proper cleanup
    async with AgentPool(agent_def) as pool:
        # Add some agents
        agent: Agent[Any] = pool.get_agent("test_agent")
        assert "test_agent" in pool.agents

        # Get runtime reference to check cleanup
        runtime = agent.runtime
        assert runtime is not None

        # Test manual cleanup
        await pool.cleanup()
        assert not pool.agents  # Should be empty after cleanup
        # assert runtime._client is None  # Runtime should be shut down

    # Test context manager cleanup
    assert not pool.agents  # Should still be empty after context exit


@pytest.mark.asyncio
async def test_agent_pool_context_cleanup():
    """Test cleanup through context manager."""
    fields = {"message": ResponseField(type="str", description="Test message")}
    defn = InlineResponseDefinition(description="Basic test result", fields=fields)
    cfg = AgentConfig(name="Test Agent", model=MODEL, result_type="BasicResult")
    agents = {"test_agent": cfg}
    agent_def = AgentsManifest[Any, Any](responses={"BasicResult": defn}, agents=agents)

    runtime_ref = None

    async with AgentPool(agent_def) as pool:
        agent: Agent[Any] = pool.get_agent("test_agent")
        runtime_ref = agent.runtime
        assert "test_agent" in pool.agents
        assert runtime_ref is not None

    # After context exit
    assert not pool.agents
    # assert runtime_ref._client is None  # Runtime should be shut down
