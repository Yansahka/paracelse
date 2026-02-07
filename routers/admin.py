# chemin du fichier : your_project_name/app/routers/admin.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import uuid
from typing import Any
from datetime import datetime

from models import models
from schemas import schemas
from configs.functions import get_db

router = APIRouter(
    prefix="/paracelse/api/v1/admin",
    tags=["Administration (Protégé)"],
    # dependencies=[Depends(get_current_user_dependency)] 
)

# Fonction factice pour simuler un utilisateur authentifié (à remplacer)
def get_current_user_dependency():
    """Logique d'auth JWT"""
    # Pour le test, on retourne un utilisateur valide
    return {"username": "admin_user", "role": "admin"}


@router.post("/medicaments", response_model=schemas.MedicamentInDB, status_code=status.HTTP_201_CREATED)
def create_medicament(
    medicament: schemas.MedicamentCreate,
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user_dependency)
):
    """
    Crée un nouveau médicament (Protégé).
    """
    db_medicament = models.Medicament(
        **medicament.dict(),
        id=uuid.uuid4(),
        updated_at=datetime.utcnow()
    )
    db.add(db_medicament)
    db.commit()
    db.refresh(db_medicament)

    return db_medicament

@router.delete("/medicaments/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medicament(
    id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user_dependency)
):
    """
    Supprime un médicament par ID (Protégé).
    """
    db_medicament = db.query(models.Medicament).filter(models.Medicament.id == id).first()
    if db_medicament is None:
        raise HTTPException(status_code=404, detail="Médicament non trouvé")
    
    db.delete(db_medicament)
    db.commit()
    return {"message": f"Médicament {id} supprimé"} 
# Note: 204 No Content ne retourne généralement pas de corps.
