# base_tool.py
from typing import Dict, Any
from pydantic import BaseModel, Field

class BaseTool(BaseModel):
    name: str = Field(..., description="The name of the tool.")
    description: str = Field(..., description="A brief description of the tool's functionality.")

    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the tool's functionality."""
        raise NotImplementedError("Subclasses must implement this method.")