# chemin du fichier : your_project_name/app/routers/sync.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Dict

from configs.functions import get_db

router = APIRouter(
    prefix="/paracelse/api/v1/sync",
    tags=["Synchronisation"]
)

@router.get("/delta")
def get_delta_updates(since_date: datetime, db: Session = Depends(get_db)):
    """
    Recupere les modifications (delta) depuis une date donnée.
    Utilise le champ 'updated_at' des modèles.
    """
    # Implementation : interroger toutes les tables (medicaments, noms_commerciaux, etc.)
    # pour les enregistrements où updated_at > since_date
    return {"message": f"Recupération des modifications depuis {since_date}. Logique non implémentee pour le moment."}

@router.get("/full")
def get_full_export(db: Session = Depends(get_db)):
    """
    Export complet de la base de donnees pour le premier telechargement.
    """
    # Implémentation : retourner toutes les données nécessaires, possiblement en JSON compressé
    return {"message": "Export complet de la base. Logique non implementee."}

@router.get("/version", response_model=Dict[str, str])
def get_database_version(db: Session = Depends(get_db)):
    """
    Retourne la version actuelle de la base de donnees (date de dernière mise à jour serveur).
    """
    # Implémentation : lire la dernière date de mise à jour depuis une table de metadata
    # ou calculer le max(updated_at) de toutes les tables
    return {"version": datetime.now().isoformat()}
