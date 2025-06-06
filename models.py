from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Paper(Base):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    abstract = Column(Text)
    authors = Column(String)
    publication_date = Column(DateTime)
    journal = Column(String)
    doi = Column(String, unique=True)
    keywords = Column(String)

    # Define relationship for citations
    citations = relationship("Citation", back_populates="paper")

class Citation(Base):
    __tablename__ = "citations"

    id = Column(Integer, primary_key=True, index=True)
    citing_paper_id = Column(Integer, ForeignKey("papers.id"))
    cited_paper_id = Column(Integer, ForeignKey("papers.id"))

    # Define relationships
    paper = relationship("Paper", foreign_keys=[citing_paper_id], back_populates="citations")
    cited_paper = relationship("Paper", foreign_keys=[cited_paper_id])