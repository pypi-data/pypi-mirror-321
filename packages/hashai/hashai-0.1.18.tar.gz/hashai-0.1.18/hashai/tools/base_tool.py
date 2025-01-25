from typing import Dict, Any
from pydantic import BaseModel

class BaseTool(BaseModel):
    name: str
    description: str

    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the tool's functionality."""
        raise NotImplementedError("Subclasses must implement this method.")