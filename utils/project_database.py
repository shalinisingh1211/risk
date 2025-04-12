import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables
load_dotenv()

# Use environment variable or fallback
DATABASE_URL = os.getenv("DATABASE_URL") or "sqlite:///data/project_risks.db"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True)
    name = Column(String)
    status = Column(String)
    risk_score = Column(Float)
    start_date = Column(String)
    end_date = Column(String)
    schedule_risk = Column(Float)
    budget_risk = Column(Float)
    resource_risk = Column(Float)
    market_risk = Column(Float)
    spent = Column(Float)
    budget = Column(Float)
    team_size = Column(Integer)
    risk_delta = Column(Float)

def initialize_database():
    Base.metadata.create_all(engine)

def get_projects():
    session = Session()
    return session.query(Project).all()

def get_project(project_id):
    session = Session()
    return session.query(Project).filter(Project.id == project_id).first()

def search_similar_risks(risk_query):
    return [{"name": "Delayed Payment", "description": "Customer payments are delayed beyond the expected schedule."}]
