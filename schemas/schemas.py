import uuid
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

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
    nom_scientifique: str
    classe_therapeutique: str
    forme_galenique: str
    voie_administration: str
    source_reference: str

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

