"""LLMling integration with PydanticAI for AI-powered resource interaction."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Any, Self, get_type_hints, overload

from typing_extensions import TypeVar

from llmling_agent.log import get_logger
from llmling_agent.responses.models import BaseResponseDefinition, ResponseDefinition
from llmling_agent.responses.utils import to_type


if TYPE_CHECKING:
    from datetime import timedelta
    from types import TracebackType

    from llmling.config.models import Resource
    from toprompt import AnyPromptType

    from llmling_agent.agent import AnyAgent
    from llmling_agent.agent.agent import Agent
    from llmling_agent.agent.connection import Talk, TeamTalk
    from llmling_agent.common_types import ModelType
    from llmling_agent.delegation.agentgroup import Team
    from llmling_agent.delegation.execution import TeamRun
    from llmling_agent.models.context import AgentContext
    from llmling_agent.models.forward_targets import ConnectionType
    from llmling_agent.models.messages import ChatMessage
    from llmling_agent.models.task import AgentTask
    from llmling_agent.tools.manager import ToolManager
    from llmling_agent_providers.callback import ProcessorCallback


logger = get_logger(__name__)

TResult = TypeVar("TResult", default=str)
TDeps = TypeVar("TDeps", default=None)


class StructuredAgent[TDeps, TResult]:
    """Wrapper for Agent that enforces a specific result type.

    This wrapper ensures the agent always returns results of the specified type.
    The type can be provided as:
    - A Python type for validation
    - A response definition name from the manifest
    - A complete response definition instance
    """

    def __init__(
        self,
        agent: Agent[TDeps] | StructuredAgent[TDeps, TResult] | Callable[..., TResult],
        result_type: type[TResult] | str | ResponseDefinition,
        *,
        tool_name: str | None = None,
        tool_description: str | None = None,
    ):
        """Initialize structured agent wrapper.

        Args:
            agent: Base agent to wrap
            result_type: Expected result type:
                - BaseModel / dataclasses
                - Name of response definition in manifest
                - Complete response definition instance
            tool_name: Optional override for tool name
            tool_description: Optional override for tool description

        Raises:
            ValueError: If named response type not found in manifest
        """
        from llmling_agent.agent.agent import Agent

        logger.debug("StructuredAgent.run result_type = %s", result_type)
        match agent:
            case StructuredAgent():
                self._agent: Agent[TDeps] = agent._agent
            case Callable():
                self._agent = Agent[TDeps](provider=agent, name=agent.__name__)
            case Agent():
                self._agent = agent
            case _:
                msg = "Invalid agent type"
                raise ValueError(msg)

        self._result_type = to_type(result_type)
        agent.set_result_type(result_type)

        match result_type:
            case type() | str():
                # For types and named definitions, use overrides if provided
                self._agent.set_result_type(
                    result_type,
                    tool_name=tool_name,
                    tool_description=tool_description,
                )
            case BaseResponseDefinition():
                # For response definitions, use as-is
                # (overrides don't apply to complete definitions)
                self._agent.set_result_type(result_type)

    async def __aenter__(self) -> Self:
        """Enter async context and set up MCP servers.

        Called when agent enters its async context. Sets up any configured
        MCP servers and their tools.
        """
        await self._agent.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ):
        """Exit async context."""
        await self._agent.__aexit__(exc_type, exc_val, exc_tb)

    def __and__(
        self, other: AnyAgent[Any, Any] | Team[Any] | ProcessorCallback[TResult]
    ) -> Team[TDeps]:
        return self._agent.__and__(other)

    def __or__(self, other: Agent | ProcessorCallback | Team | TeamRun) -> TeamRun:
        return self._agent.__or__(other)

    async def run(
        self,
        *prompt: AnyPromptType | TResult,
        result_type: type[TResult] | None = None,
        deps: TDeps | None = None,
        model: ModelType = None,
        store_history: bool = True,
        wait_for_connections: bool = False,
    ) -> ChatMessage[TResult]:
        """Run with fixed result type.

        Args:
            prompt: Any prompt-compatible object or structured objects of type TResult
            result_type: Expected result type:
                - BaseModel / dataclasses
                - Name of response definition in manifest
                - Complete response definition instance
            deps: Optional dependencies for the agent
            model: Optional model override
            store_history: Whether the message exchange should be added to the
                           context window
            wait_for_connections: Whether to wait for all connections to complete
        """
        typ = result_type or self._result_type
        return await self._agent.run(
            *prompt,
            result_type=typ,
            model=model,
            store_history=store_history,
            wait_for_connections=wait_for_connections,
        )

    def __repr__(self) -> str:
        type_name = getattr(self._result_type, "__name__", str(self._result_type))
        return f"StructuredAgent({self._agent!r}, result_type={type_name})"

    def __prompt__(self) -> str:
        type_name = getattr(self._result_type, "__name__", str(self._result_type))
        base_info = self._agent.__prompt__()
        return f"{base_info}\nStructured output type: {type_name}"

    def __getattr__(self, name: str) -> Any:
        return getattr(self._agent, name)

    @property
    def context(self) -> AgentContext[TDeps]:
        return self._agent.context

    @context.setter
    def context(self, value: Any):
        self._agent.context = value

    @property
    def name(self) -> str:
        return self._agent.name

    @name.setter
    def name(self, value: str):
        self._agent.name = value

    @property
    def tools(self) -> ToolManager:
        return self._agent.tools

    @overload
    def to_structured(
        self,
        result_type: None,
        *,
        tool_name: str | None = None,
        tool_description: str | None = None,
    ) -> Agent[TDeps]: ...

    @overload
    def to_structured[TNewResult](
        self,
        result_type: type[TNewResult] | str | ResponseDefinition,
        *,
        tool_name: str | None = None,
        tool_description: str | None = None,
    ) -> StructuredAgent[TDeps, TNewResult]: ...

    def to_structured[TNewResult](
        self,
        result_type: type[TNewResult] | str | ResponseDefinition | None,
        *,
        tool_name: str | None = None,
        tool_description: str | None = None,
    ) -> Agent[TDeps] | StructuredAgent[TDeps, TNewResult]:
        if result_type is None:
            return self._agent

        return StructuredAgent(
            self._agent,
            result_type=result_type,
            tool_name=tool_name,
            tool_description=tool_description,
        )

    async def run_task(
        self,
        task: AgentTask[TDeps, TResult],
        *,
        store_history: bool = True,
        include_agent_tools: bool = True,
    ) -> ChatMessage[TResult]:
        """Execute a pre-defined task ensuring type compatibility.

        Args:
            task: Task configuration to execute
            store_history: Whether to add task execution to conversation history
            include_agent_tools: Whether to include agent's tools alongside task tools

        Returns:
            Task execution result

        Raises:
            TaskError: If task execution fails or types don't match
            ValueError: If task configuration is invalid
        """
        from llmling_agent.tasks import TaskError

        # Validate dependency requirement
        if task.required_dependency is not None:  # noqa: SIM102
            if not isinstance(self.context.data, task.required_dependency):
                msg = (
                    f"Agent dependencies ({type(self.context.data)}) "
                    f"don't match task requirement ({task.required_dependency})"
                )
                raise TaskError(msg)

        # Validate return type requirement
        if task.required_return_type != self._result_type:
            msg = (
                f"Agent result type ({self._result_type}) "
                f"doesn't match task requirement ({task.required_return_type})"
            )
            raise TaskError(msg)

        # Load task knowledge if provided
        if task.knowledge:
            # Add knowledge sources to context
            resources: list[Resource | str] = list(task.knowledge.paths) + list(
                task.knowledge.resources
            )
            for source in resources:
                await self.conversation.load_context_source(source)
            for prompt in task.knowledge.prompts:
                await self.conversation.load_context_source(prompt)

        try:
            # Register task tools temporarily
            tools = task.get_tools()

            # Use temporary tools
            with self._agent.tools.temporary_tools(
                tools, exclusive=not include_agent_tools
            ):
                # Execute task using StructuredAgent's run to maintain type safety
                return await self.run(
                    await task.get_prompt(), store_history=store_history
                )

        except Exception as e:
            msg = f"Task execution failed: {e}"
            logger.exception(msg)
            raise TaskError(msg) from e

    @classmethod
    def from_callback(
        cls,
        callback: ProcessorCallback[TResult],
        *,
        deps: TDeps | None = None,
        name: str | None = None,
        **kwargs: Any,
    ) -> StructuredAgent[TDeps, TResult]:
        """Create a structured agent from a processing callback.

        Args:
            callback: Function to process messages. Can be:
                - sync or async
                - with or without context
                - with explicit return type
            name: Optional name for the agent
            deps: Optional dependencies for the agent
            **kwargs: Additional arguments for agent

        Example:
            ```python
            class AnalysisResult(BaseModel):
                sentiment: float
                topics: list[str]

            def analyze(msg: str) -> AnalysisResult:
                return AnalysisResult(sentiment=0.8, topics=["tech"])

            analyzer = StructuredAgent.from_callback(analyze)
            ```
        """
        from llmling_agent.agent.agent import Agent
        from llmling_agent_providers.callback import CallbackProvider

        name = name or callback.__name__ or "processor"
        provider = CallbackProvider[TDeps](callback, name=name)
        agent = Agent[TDeps](provider=provider, name=name, **kwargs)
        if deps is not None:
            agent.context.data = deps
        # Get return type from signature for validation
        hints = get_type_hints(callback)
        return_type = hints.get("return")

        # If async, unwrap from Awaitable
        if return_type and hasattr(return_type, "__origin__"):
            from collections.abc import Awaitable

            if return_type.__origin__ is Awaitable:
                return_type = return_type.__args__[0]
        return cls(agent, return_type or str)  # type: ignore

    @overload
    def pass_results_to(
        self,
        other: AnyAgent[Any, Any] | str,
        prompt: str | None = None,
        connection_type: ConnectionType = "run",
        priority: int = 0,
        delay: timedelta | None = None,
    ) -> Talk[TResult]: ...

    @overload
    def pass_results_to(
        self,
        other: Team[Any],
        prompt: str | None = None,
        connection_type: ConnectionType = "run",
        priority: int = 0,
        delay: timedelta | None = None,
    ) -> TeamTalk: ...

    def pass_results_to(
        self,
        other: AnyAgent[Any, Any] | Team[Any] | str,
        prompt: str | None = None,
        connection_type: ConnectionType = "run",
        priority: int = 0,
        delay: timedelta | None = None,
    ) -> Talk[TResult] | TeamTalk:
        """Forward results to another agent or all agents in a team."""
        return self._agent.connections.connect_agent_to(
            other,
            connection_type=connection_type,
            priority=priority,
            delay=delay,
        )
