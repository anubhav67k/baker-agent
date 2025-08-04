from .agent_base import BaseAgent
from .insurance_tools import get_insurance_tools
from models.messages_kernel import AgentType

class InsuranceAgent(BaseAgent):
    def __init__(self, session_id, user_id, memory_store, tools=None, system_message=None, agent_name=AgentType.INSURANCE.value, client=None, definition=None):
        if not tools:
            tools = get_insurance_tools()
        if not system_message:
            system_message = self.default_system_message(agent_name)
        super().__init__(agent_name, session_id, user_id, memory_store, tools, system_message, client, definition)

    @staticmethod
    def default_system_message(agent_name=None):
        return "You are an AI Agent specialized in insurance tasks such as claims and policy management."

    @property
    def plugins(self):
        return get_insurance_tools()
