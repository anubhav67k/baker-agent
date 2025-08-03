from .agent_base import BaseAgent
from .baker_tools import get_baker_tools
from models.messages_kernel import AgentType

class BakerAgent(BaseAgent):
    def __init__(self, session_id, user_id, memory_store, tools=None, system_message=None, agent_name=AgentType.BAKER.value, client=None, definition=None):
        if not tools:
            tools = get_baker_tools()
        if not system_message:
            system_message = self.default_system_message(agent_name)
        super().__init__(agent_name, session_id, user_id, memory_store, tools, system_message, client, definition)

    @staticmethod
    def default_system_message(agent_name=None):
        return "You are an AI Agent specialized in baking tasks, such as baking cookies and preparing dough."

    @property
    def plugins(self):
        return get_baker_tools()
