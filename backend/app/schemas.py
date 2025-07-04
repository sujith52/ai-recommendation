from pydantic import BaseModel
from enum import Enum
from datetime import datetime

# For user creation
class UserCreate(BaseModel):
    name: str

# For item creation
class ItemCreate(BaseModel):
    name: str

# Enum for interaction types
class InteractionType(str, Enum):
    view = "view"
    click = "click"
    search = "search"

# Input schema for interaction logging
class InteractionCreate(BaseModel):
    user_id: int
    item_id: int
    interaction_type: InteractionType

# Output schema for interaction response
class InteractionResponse(InteractionCreate):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True  # required for Pydantic v2 to support ORM models
