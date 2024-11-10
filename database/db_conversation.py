from schemas import ConversationBase
from sqlalchemy.orm.session import Session
import datetime
from database.models import DbConversation
from fastapi import HTTPException, status



def create_conversation(db:Session, request:ConversationBase):

 existing_conversation =db.query(DbConversation).filter(
  DbConversation.buyer_id ==request.buyer_id,
  DbConversation.product_id==request.product_id
 ).first()

 if existing_conversation:
  return existing_conversation
 
 new_conversation = DbConversation(
  buyer_id = request.buyer_id,
  product_id = request.product_id
 )

 db.add(new_conversation)
 db.commit()
 db.refresh(new_conversation)
 return new_conversation


def get_all_conversations(db:Session):
 return db.query(DbConversation).all()

def get_conversation_by_id(db:Session, id:int):
 conversation = db.query(DbConversation).filter(DbConversation.id==id).first()
 if not conversation:
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail ="Conversation not found")
 return conversation

def delete_conversation(id:int, db:Session):
 conversation = db.query(DbConversation).filter(DbConversation.id==id).first()
 if not conversation:
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f'conversation with id {id} not found')
 db.delete(conversation)
 db.commit()
 return "The conversation successfully deleted"
 
