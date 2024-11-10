from sqlalchemy import Column, Integer, String, Boolean, Text, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime, timezone

class DbUser(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    
    products_selling = relationship("DbProduct", foreign_keys="[DbProduct.seller_id]", back_populates="seller")
    products_bought = relationship("DbProduct", foreign_keys="[DbProduct.buyer_id]", back_populates="buyer")
    reserved_products = relationship("DbProduct", foreign_keys="[DbProduct.reservedBuyer_id]", back_populates="reserved_buyer")
    
    conversations = relationship("DbConversation", foreign_keys="[DbConversation.buyer_id]", back_populates="buyer")
    message_sending = relationship("DbMessage", back_populates="sender")

class DbProduct(Base):
    __tablename__ = "products"
    
   
    id = Column(Integer, primary_key=True, index=True)
    
    
    product_name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    image_url = Column(String, nullable=True)
    product_category = Column(String, nullable=True)
    product_status = Column(String, nullable=False, default="Available")
    
    
    seller_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    buyer_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    reservedBuyer_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    
    
    seller = relationship("DbUser", foreign_keys=[seller_id], back_populates="products_selling")
    buyer = relationship("DbUser", foreign_keys=[buyer_id], back_populates="products_bought")
    reserved_buyer = relationship("DbUser", foreign_keys=[reservedBuyer_id], back_populates="reserved_products")
    
    
    product_conversation = relationship("DbConversation", back_populates="product")

class DbConversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)  
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False) 
  

    buyer = relationship("DbUser", back_populates="conversations")  
    product = relationship("DbProduct", back_populates="product_conversation") 
    messages = relationship("DbMessage", back_populates="conversation")  

    @property
    def seller_id(self):
        return self.product.seller_id  

class DbMessage(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"), nullable=False)
    sender_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    # Relationships
    conversation = relationship("DbConversation", back_populates="messages")  
    sender = relationship("DbUser",foreign_keys=[sender_id], back_populates="message_sending")  


# class DbMessage(Base):
#     __tablename__ = "messages"
#     id = Column(Integer, primary_key=True, index=True)
#     conversation_id = Column(Integer, ForeignKey("conversations.id"), nullable=False)
#     sender_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
#     content = Column(Text, nullable=False)
#     timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
#     # Relationships
#     conversation = relationship("DbConversation", back_populates="messages")  
#     sender = relationship("DbUser",foreign_keys=[sender_id], back_populates="message_sending")  

# class DbMessage(Base):
#     __tablename__ = "messages"
#     id = Column(Integer, primary_key=True, index=True)
#     conversation_id = Column(Integer, ForeignKey("conversations.id"), nullable=False)
#     sender_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
#     content = Column(Text, nullable=False)
#     timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
#     # Relationships
#     conversation = relationship("DbConversation", back_populates="messages")  
#     sender = relationship("DbUser",foreign_keys=[sender_id], back_populates="message_sending")  