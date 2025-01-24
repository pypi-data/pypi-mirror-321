import asyncio
import uuid
from typing import Callable, Dict, TypeVar

from mcp.server.fastmcp.tools import Tool as FastTool
from mcp.types import (
    CallToolResult,
    ListToolsResult,
    TextContent,
    Tool,
)

from mcp_agent.executor.executor import Executor, AsyncioExecutor
from mcp_agent.mcp.mcp_aggregator import MCPAggregator
from mcp_agent.human_input.types import (
    HumanInputCallback,
    HumanInputRequest,
    HumanInputResponse,
    HUMAN_INPUT_SIGNAL_NAME,
)
from mcp_agent.workflows.llm.augmented_llm import AugmentedLLM
from mcp_agent.context import get_current_context
from mcp_agent.logging.logger import get_logger

logger = get_logger(__name__)

# Define a TypeVar for AugmentedLLM and its subclasses
LLM = TypeVar("LLM", bound=AugmentedLLM)

HUMAN_INPUT_TOOL_NAME = "__human_input__"


class Agent(MCPAggregator):
    """
    An Agent is an entity that has access to a set of MCP servers and can interact with them.
    Each agent should have a purpose defined by its instruction.
    """

    name: str
    instruction: str | Callable[[Dict], str]

    def __init__(
        self,
        name: str,
        instruction: str | Callable[[Dict], str] = "You are a helpful agent.",
        server_names: list[str] = None,
        connection_persistence: bool = True,
        human_input_callback: HumanInputCallback = None,
        executor: Executor | None = None,
    ):
        super().__init__(
            server_names=server_names or [],
            connection_persistence=connection_persistence,
            name=name,
            instruction=instruction,
        )

        self.executor = executor or AsyncioExecutor()
        self.human_input_callback: HumanInputCallback | None = human_input_callback
        if not human_input_callback:
            ctx = get_current_context()
            if ctx.human_input_handler:
                self.human_input_callback = ctx.human_input_handler

    async def initialize(self):
        """
        Initialize the agent and connect to the MCP servers.
        NOTE: This method is called automatically when the agent is used as an async context manager.
        """
        await (
            self.__aenter__()
        )  # This initializes the connection manager and loads the servers

    async def attach_llm(self, llm_factory: Callable[..., LLM]) -> LLM:
        """
        Create an LLM instance for the agent.

         Args:
            llm_factory: A callable that constructs an AugmentedLLM or its subclass.
                        The factory should accept keyword arguments matching the
                        AugmentedLLM constructor parameters.

        Returns:
            An instance of AugmentedLLM or one of its subclasses.
        """
        return llm_factory(agent=self)

    async def shutdown(self):
        """
        Shutdown the agent and close all MCP server connections.
        NOTE: This method is called automatically when the agent is used as an async context manager.
        """
        await super().close()

    async def request_human_input(
        self,
        request: HumanInputRequest,
    ) -> str:
        """
        Request input from a human user. Pauses the workflow until input is received.

        Args:
            request: The human input request

        Returns:
            The input provided by the human

        Raises:
            TimeoutError: If the timeout is exceeded
        """
        if not self.human_input_callback:
            raise ValueError("Human input callback not set")

        # Generate a unique ID for this request to avoid signal collisions
        request_id = f"{HUMAN_INPUT_SIGNAL_NAME}_{self.name}_{uuid.uuid4()}"
        request.request_id = request_id

        logger.debug("Requesting human input:", data=request)

        async def call_callback_and_signal():
            try:
                user_input = await self.human_input_callback(request)
                logger.debug("Received human input:", data=user_input)
                await self.executor.signal(signal_name=request_id, payload=user_input)
            except Exception as e:
                await self.executor.signal(
                    request_id, payload=f"Error getting human input: {str(e)}"
                )

        asyncio.create_task(call_callback_and_signal())

        logger.debug("Waiting for human input signal")

        # Wait for signal (workflow is paused here)
        result = await self.executor.wait_for_signal(
            signal_name=request_id,
            request_id=request_id,
            workflow_id=request.workflow_id,
            signal_description=request.description or request.prompt,
            timeout_seconds=request.timeout_seconds,
            signal_type=HumanInputResponse,  # TODO: saqadri - should this be HumanInputResponse?
        )

        logger.debug("Received human input signal", data=result)
        return result

    async def list_tools(self) -> ListToolsResult:
        if not self.initialized:
            await self.initialize()

        result = await super().list_tools()

        if not self.human_input_callback:
            logger.debug("Human input callback not set")
            return result

        # Add a human_input_callback as a tool
        human_input_tool: FastTool = FastTool.from_function(self.request_human_input)
        result.tools.append(
            Tool(
                name=HUMAN_INPUT_TOOL_NAME,
                description=human_input_tool.description,
                inputSchema=human_input_tool.parameters,
            )
        )

        return result

    async def call_tool(
        self, name: str, arguments: dict | None = None
    ) -> CallToolResult:
        if name != HUMAN_INPUT_TOOL_NAME:
            return await super().call_tool(name, arguments)

        # Handle human input request
        try:
            request = HumanInputRequest(**arguments["request"])
            result: HumanInputResponse = await self.request_human_input(request=request)
            return CallToolResult(
                content=[
                    TextContent(
                        type="text", text=f"Human response: {result.model_dump_json()}"
                    )
                ]
            )
        except TimeoutError as e:
            return CallToolResult(
                isError=True,
                content=[
                    TextContent(
                        type="text",
                        text=f"Error: Human input request timed out: {str(e)}",
                    )
                ],
            )
        except Exception as e:
            return CallToolResult(
                isError=True,
                content=[
                    TextContent(
                        type="text", text=f"Error requesting human input: {str(e)}"
                    )
                ],
            )
