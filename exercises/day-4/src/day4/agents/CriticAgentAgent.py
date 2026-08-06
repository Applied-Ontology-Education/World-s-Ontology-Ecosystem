from __future__ import annotations

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.tools import BaseTool, tool
from naas_abi_core.models.Model import ChatModel
from naas_abi_core.services.agent.Agent import (
    Agent,
    AgentConfiguration,
    AgentSharedState,
)

from day4.agents.FeedbackModels import CriticFeedback


class CriticAgentAgent(Agent):
    name: str = "CriticAgent"
    description: str = "Checks a Zebra-owner hypothesis against active axioms."
    system_prompt: str = """You are the Critic Agent.

Use only the supplied ontology. Review cited axioms, numbered reasoning steps,
alternatives, confidence, status, and assumptions. Make corrections specific
and actionable, then call `submit_critic_feedback` exactly once.

Do not use prior Zebra Puzzle knowledge or claim entailment without a supplied
formal reasoner result.
"""

    @staticmethod
    def feedback_tool() -> BaseTool:
        @tool(
            "submit_critic_feedback",
            args_schema=CriticFeedback,
            return_direct=True,
        )
        def submit_critic_feedback(**feedback) -> str:
            """Submit the final structured critique."""
            return CriticFeedback(**feedback).model_dump_json()

        return submit_critic_feedback

    @classmethod
    def New(
        cls,
        agent_shared_state: AgentSharedState | None = None,
        agent_configuration: AgentConfiguration | None = None,
        chat_model: BaseChatModel | ChatModel | None = None,
    ) -> CriticAgentAgent:
        from naas_abi_core.engine.context import get_default_model_registry

        registry = get_default_model_registry()
        assert registry is not None, "Model registry is not initialized"

        if agent_configuration is None:
            agent_configuration = AgentConfiguration(system_prompt=cls.system_prompt)

        return cls(
            name=cls.name,
            description=cls.description,
            chat_model=chat_model or registry.get_default_chat_model(),
            tools=[cls.feedback_tool()],
            agents=[],
            memory=None,
            state=agent_shared_state or AgentSharedState(thread_id="0"),
            configuration=agent_configuration,
            enable_default_tools=False,
        )
