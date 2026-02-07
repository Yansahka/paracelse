from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid

from models import models
from schemas import schemas
from configs.functions import get_db

router = APIRouter(
    prefix="paracelse/api/v1/medicaments",
    tags=["Médicaments"]
)

@router.get("/search", response_model=List[schemas.MedicamentInDB])
def search_medicaments(query: str, db: Session = Depends(get_db)):
    # Logique de recherche full-text
    # Implémentation simplifiée : filtrage sur le nom scientifique.. d'autre champ seront ajoute au besoin
    results = db.query(models.Medicament).filter(models.Medicament.nom_scientifique.ilike(f"%{query}%")).all()
    # Une tolerance aux fautes plus complexe sera implemente plus tard
    return results

@router.get("/", response_model=List[schemas.MedicamentInDB])
def read_medicaments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Logique pour lister les médicaments (paginé)
    medicaments = db.query(models.Medicament).offset(skip).limit(limit).all()
    return medicaments


@router.get("/{id}", response_model=schemas.MedicamentDetail)
def read_medicament(id: uuid.UUID, db: Session = Depends(get_db)):
    # Logique pour obtenir les détails d'un médicament avec ses relations
    medicament = db.query(models.Medicament).filter(models.Medicament.id == id).first()
    if medicament is None:
        raise HTTPException(status_code=404, detail="Médicament non trouvé")
    return medicament