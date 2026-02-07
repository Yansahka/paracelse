from fastapi import FastAPI, Depends
from fastapi import FastAPI
from configs.db import Base, engine
from routers import medicaments, sync, admin

#import pour testr acces a la BD PG
from sqlalchemy.orm import Session
from configs.functions import get_db

app = FastAPI(root_path="")


# Créer les tables dans la base BD au demarrage en dev/tests
# En production, vais utiliser Alembic pour les migrations
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PARACELSE API",
    description="API d'Aide Médicamenteuse",
    version="1.0"
)

# Inclusion des routes definies dans routers/*.py
app.include_router(medicaments.router)
app.include_router(sync.router)
app.include_router(admin.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Paracelse"}


@app.get("/api/v1")
def welcome_msg():
    return {"msg":"Welcome to paracelse API"}

#Test d'acces a la BDs
@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    return {"DB":"Connection successful"}