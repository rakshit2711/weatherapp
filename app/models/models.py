from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Create the base class for models
Base = declarative_base()

# Define the City model
class City(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String, nullable=False)
    state_id = Column(Integer, ForeignKey("states.state_id"))  # Foreign key to State
    
    # Relationship with State
    state = relationship("State", back_populates="cities")


# Define the State model
class State(Base):
    __tablename__ = 'states'
    state_id = Column(Integer, primary_key=True, autoincrement=True)
    state_name = Column(String, nullable=False)
    state_code = Column(String, nullable=False)
    country_id = Column(Integer, ForeignKey("countries.country_id"))  # Foreign key to Country
    
    # Relationship with City
    cities = relationship("City", back_populates="state")
    
    # Relationship with Country
    country = relationship("Country", back_populates="states")


# Define the Country model
class Country(Base):
    __tablename__ = 'countries'
    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String, nullable=False)
    country_code = Column(String, nullable=False)
    capital = Column(String)
    region = Column(String)
    subregion = Column(String)
    
    # Relationship with State
    states = relationship("State", back_populates="country")
    