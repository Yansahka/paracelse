import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DECIMAL, Integer, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
# UTILISEZ UN SEUL BASE (celui de votre config de préférence)
from configs.db import Base 

class Medicament(Base):
    __tablename__ = "medicaments"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nom_scientifique = Column(String(255), unique=True, nullable=False)
    classe_therapeutique = Column(String(100), nullable=False)
    sous_classe = Column(String(100))
    mecanisme_action = Column(Text)
    indication_general = Column(Text)
    effets_indesirables = Column(Text)
    contre_indications = Column(Text)
    interaction_importantes = Column(Text)
    points_cles = Column(Text)
    forme_galenique = Column(String(50), nullable=False, default="N/A")
    voie_administration = Column(String(50), nullable=False, default="Orale")
    source_reference = Column(Text, nullable=False, default="Paraselse Vol 1")
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relations avec cascades pour maintenir l'intégrité de la BD
    noms_commerciaux = relationship("NomCommercial", back_populates="medicament", cascade="all, delete-orphan")
    posologies = relationship("Posologie", back_populates="medicament", cascade="all, delete-orphan")
    ajustements_renaux = relationship("AjustementRenal", back_populates="medicament", cascade="all, delete-orphan")

class NomCommercial(Base):
    __tablename__ = "noms_commerciaux"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    medicament_id = Column(UUID(as_uuid=True), ForeignKey("medicaments.id", ondelete="CASCADE"))
    nom_commercial = Column(String(255), nullable=False)
    
    medicament = relationship("Medicament", back_populates="noms_commerciaux")

class Posologie(Base):
    __tablename__ = "posologies"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    medicament_id = Column(UUID(as_uuid=True), ForeignKey("medicaments.id", ondelete="CASCADE"))
    type_population = Column(Enum("ADULTE", "PEDIATRIQUE", "GERIATRIQUE", name="type_population_enum"), nullable=False)
    dose_standard = Column(String(100), nullable=True)
    dose_par_kg = Column(DECIMAL(10,4), nullable=True)
    dose_maximale = Column(DECIMAL(10,2), nullable=True)
    frequence = Column(String(50), nullable=False)
    age_min = Column(Integer, nullable=True)
    age_max = Column(Integer, nullable=True)

    medicament = relationship("Medicament", back_populates="posologies")

class AjustementRenal(Base):
    __tablename__ = "ajustements_renaux"
    medicament_id = Column(UUID(as_uuid=True), ForeignKey("medicaments.id", ondelete="CASCADE"), primary_key=True)
    dfg_min = Column(Integer, nullable=False)
    dfg_max = Column(Integer, nullable=False)
    ajustement = Column(String(255), nullable=False)
    coefficient_reduction = Column(DECIMAL(3,2), nullable=True)
    
    medicament = relationship("Medicament", back_populates="ajustements_renaux")
