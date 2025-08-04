from typing import List
from kernel_agents.agent_utils import FunctionTool, Tool

async def process_order(order_id: str) -> str:
    return f"Order {order_id} processed."

async def check_inventory(item: str) -> str:
    return f"Inventory checked for {item}."

def get_retail_tools() -> List[Tool]:
    return [
        FunctionTool(process_order, description="Process a retail order.", name="process_order"),
        FunctionTool(check_inventory, description="Check inventory for an item.", name="check_inventory"),
    ]
