# from sqlalchemy.orm import Session
# from fastapi import HTTPException, status
# from db.models import DbUser, DbMessage, DbProduct

# # Önce ilişkili mesajları sil
# def delete_user_messages(user_id: int, db: Session):
#     messages = db.query(DbMessage).filter(DbMessage.sender_id == user_id).all()
#     for message in messages:
#         db.delete(message)
#     db.commit()

# # Kullanıcıyı silmeden önce mesajlarını sil
# def delete_user(user_id: int, db: Session):
#     # İlk olarak ilişkili mesajları sil
#     delete_user_messages(user_id, db)
    
#     # Sonra kullanıcıyı sil
#     user = db.query(DbUser).filter(DbUser.user_id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#     db.delete(user)
#     db.commit()
#     return {"message": "User and related messages deleted successfully"}

# # Ürün için de aynı mantığı kullanarak önce ilişkili mesajları sil, ardından ürünü sil
# def delete_product_messages(product_id: int, db: Session):
#     # Ürünle ilişkili tüm mesajları bul ve sil
#     messages = db.query(DbMessage).join(DbConversation).filter(DbConversation.product_id == product_id).all()
#     for message in messages:
#         db.delete(message)
#     db.commit()

# def delete_product(product_id: int, db: Session):
#     # İlk olarak ürüne bağlı mesajları sil
#     delete_product_messages(product_id, db)
    
#     # Ardından ürünü sil
#     product = db.query(DbProduct).filter(DbProduct.id == product_id).first()
#     if not product:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
#     db.delete(product)
#     db.commit()
#     return {"message": "Product and related messages deleted successfully"}
