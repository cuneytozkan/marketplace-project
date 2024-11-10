from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

### User Schemas ###
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserDisplay(UserBase):
    user_id: int
    email:str
   
    
    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    product_name: str
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None
    product_category: Optional[str] = None
    product_status: str = "Available"

#class ProductCreate(ProductBase):
 #   seller_id: int

class ProductDisplay(ProductBase):
    id: int
    seller_id: int
    buyer_id: Optional[int] = None
    reservedBuyer_id: Optional[int] = None

    class Config:
        orm_mode = True

### Conversation Schemas ###

#class Sender(BaseModel):
 #   sender:str

 #   class Config:
 #       orm_mode = True

class ConversationBase(BaseModel):
    product_id: int
    buyer_id: int
   # sender :Sender

class ConversationDisplay(ConversationBase):
    id: int
    product_id:int
    buyer_id:int
    

    class Config:
        orm_mode = True


class MessageBase(BaseModel):
    conversation_id: int
    sender_id: int
    content: str

class MessageDisplay(MessageBase):
    id: int
    timestamp: datetime
    sender_id: int
    conversation_id: int
   # content:str
    
    class Config:
        orm_mode = True
