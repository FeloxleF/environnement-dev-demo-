from http.client import HTTPException
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

################ config ################

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@mariadb:3306/test"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Création d'une session pour interagir avec la base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Ajouter ceci à votre application FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


###########################################

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Phrase(Base):
    __tablename__ = "phrase"
    id = Column(Integer, primary_key=True, index=True)
    mot = Column(String(50))
    
@app.get("/")
def read_root():
    return {"message": "Hello, World"}

@app.get("/phrases")
def read_root(db: Session = Depends(get_db)):
    phrase = db.query(Phrase).all()
    if not phrase:
        raise HTTPException(status_code=404, detail="Aucune phrase trouvée")
    return phrase



