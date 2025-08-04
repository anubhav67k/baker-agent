from typing import List
from kernel_agents.agent_utils import FunctionTool, Tool

async def process_claim(claim_id: str) -> str:
    return f"Claim {claim_id} processed."

async def provide_quote(policy_type: str) -> str:
    return f"Quote provided for {policy_type} insurance."

def get_insurance_tools() -> List[Tool]:
    return [
        FunctionTool(process_claim, description="Process an insurance claim.", name="process_claim"),
        FunctionTool(provide_quote, description="Provide an insurance quote.", name="provide_quote"),
    ]
