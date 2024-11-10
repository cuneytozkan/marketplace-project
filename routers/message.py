from fastapi import APIRouter, Depends, HTTPException, status
from schemas import MessageBase, MessageDisplay
from sqlalchemy.orm import Session
from database.database import get_db
from database import db_message
from auth.oauth2 import get_current_user
from typing import List
from database.db_conversation import get_conversation_by_id


router = APIRouter(
 prefix='/messages',
 tags=['messages']
)

@router.post('/', response_model=MessageDisplay)
def create_message(
 request:MessageBase,
  db:Session =Depends(get_db)#,
#  current_user = Depends(get_current_user)
):
 conversation = get_conversation_by_id(db, request.conversation_id)
 if not conversation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")
 
#  if conversation.buyer_id!= current_user.user_id and conversation.product.seller_id != current_user.user_id:
#      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail ="You are not allowed to start this conversation")
 
 return db_message.create_message(db, request) #, current_user.user_id


@router.get('/{conversation_id}', response_model=List[MessageDisplay])
def get_messages_by_conversation(
    conversation_id:int,
    db:Session= Depends(get_db)#,
    # current_user = Depends(get_current_user)
):
    conversation = get_conversation_by_id(db, conversation_id)
    if not conversation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")
    # if conversation.buyer_id != current_user.user_id and conversation.product.seller_id != current_user.user_id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You do not have access to this conversation's messages")
    
    return db_message.get_messages_by_conversation_id(db, conversation_id)


@router.delete('/{message_id}')
def delete_message(
    message_id: int,
    db: Session = Depends(get_db)#,
    # current_user = Depends(get_current_user)
):
    # message = db_message.get_message_by_id(db, message_id)
    # if not message:
    #    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
    
    # if message.sender_id != current_user.user_id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not allowed to delete this message")

    return db_message.delete_message(db, message_id)
