from typing import List
from kernel_agents.agent_utils import FunctionTool, Tool  # Adjust import if needed

async def bake_cookies(cookie_type: str, quantity: int) -> str:
    return f"Baked {quantity} {cookie_type} cookies."

async def prepare_dough(dough_type: str) -> str:
    return f"Prepared {dough_type} dough."

def get_baker_tools() -> List[Tool]:
    return [
        FunctionTool(bake_cookies, description="Bake cookies of a specific type.", name="bake_cookies"),
        FunctionTool(prepare_dough, description="Prepare dough of a specific type.", name="prepare_dough"),
    ]
