import uuid
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field


class NomCommercialBase(BaseModel):
    nom_commercial: str
    fabricant: Optional[str] = None
    dosage_disponible: Optional[str] = None

class PosologieBase(BaseModel):
    type_population: str
    dose_standard: Optional[str] = None
    # ... autres champs de posologie possible

class AjustementRenalBase(BaseModel):
    dfg_min: int
    dfg_max: int
    ajustement: str
    # ... autres champs d'ajustement possible

class MedicamentBase(BaseModel):
    nom_scientifique: str = Field(..., max_length=255)
    classe_therapeutique: str = Field(..., max_length=100)
    sous_classe: Optional[str] = Field(None, max_length=100)
    mecanisme_action: Optional[str] = None
    indication_general: Optional[str] = None
    effets_indesirables: Optional[str] = None
    contre_indications: Optional[str] = None
    interaction_importantes: Optional[str] = None
    points_cles: Optional[str] = None
    forme_galenique: str = "N/A"
    voie_administration: str = "Orale"
    source_reference: str = "Paraselse Vol 1"
    updated_at: Optional[datetime] = None

    # Intégration des relations (Listes d'objets)
    noms_commerciaux: List[NomCommercialBase] = []
    posologies: List[PosologieBase] = []
    ajustements_renaux: List[AjustementRenalBase] = []

    # Configuration pour permettre la conversion depuis SQLAlchemy
    model_config = ConfigDict(from_attributes=True)

class MedicamentCreate(MedicamentBase):
    pass

class MedicamentInDB(MedicamentBase):
    id: uuid.UUID
    updated_at: datetime
    class Config:
        orm_mode = True # Active la compatibilité ORM

class MedicamentDetail(MedicamentInDB):
    noms_commerciaux: List[NomCommercialBase] = []
    posologies: List[PosologieBase] = []
    ajustements_renaux: List[AjustementRenalBase] = []
    # ... on va inclure contre-indications et effets indesirables le moment venu

