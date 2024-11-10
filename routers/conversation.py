from fastapi import APIRouter, Depends, HTTPException, status
from schemas import ConversationBase, ConversationDisplay
from sqlalchemy.orm import Session
from database.database import get_db
from database import db_conversation
from auth.oauth2 import get_current_user
from typing import List

router = APIRouter(
    prefix='/conversation',
    tags=['conversations']
)

@router.post('/', response_model=ConversationDisplay)
def start_conversation(
    request: ConversationBase,
    db: Session = Depends(get_db) #,
    #current_user = Depends(get_current_user)
):
   #  if request.buyer_id != current_user.user_id:
   #     raise HTTPException(
   #        status_code=status.HTTP_403_FORBIDDEN,
   #        detail = "You are not allowed to start this conversation"
   #     )
    return db_conversation.create_conversation(db, request)


@router.get('/',response_model=List[ConversationDisplay])
def get_all_conversations(db:Session =Depends(get_db)):#, current_user =Depends(get_current_user)
   conversations = db_conversation.get_all_conversations(db)
    
#     user_conversations = []
#     for conv_attemp in conversations:
#        if conv_attemp.buyer_id == current_user.user_id or conv_attemp.product.seller_id == current_user.user_id:#
#         user_conversations.append(conv_attemp)
   
   return conversations
    

@router.get('/{id}',response_model=ConversationDisplay)
def get_conversation(id:int, db:Session=Depends(get_db)):#, current_user =Depends(get_current_user)
  converstion = db_conversation.get_conversation_by_id(db,id) 
  
  if not converstion:
     raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Conversation not found')
  
#   if converstion.buyer_id != current_user.user_id and converstion.product.seller_id != current_user.user_id:
#      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You do not have access to this conversation")
  
  return converstion

@router.delete('/{id}')
def delete_conversation(id:int, db:Session=Depends(get_db)):#,current_user =Depends(get_current_user)
    
   return db_conversation.delete_conversation(id,db)
  

