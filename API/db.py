import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cambiar localhost por 'localhost' o los detalles de tu base de datos local
DATABASE_URL = os.getenv(
    "DATABASE_URL",  # Asegúrate de que esta variable esté configurada correctamente en tu entorno si es necesario
    "postgresql://postgres:3312@localhost:5432/Cash_hunter"  # Conexión a base de datos local
)

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear la sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Definir la base para las clases ORM
Base = declarative_base()

# Definir el modelo de la tabla Prediction
class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    account = Column(String, index=True)
    probability = Column(Float)
    deadline = Column(String)

# Crear la base de datos si no existe
def init_db():
    Base.metadata.create_all(bind=engine)

# Función para obtener la sesión de la base de datos
def get_session():
    return SessionLocal()


