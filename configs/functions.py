from .db import SessionLocal

#Gerer creation et fermeture de session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
