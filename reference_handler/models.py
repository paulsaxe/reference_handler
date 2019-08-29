from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Index, DateTime
from sqlalchemy.orm import relationship
# import datetime


Base = declarative_base()

class Citation(Base):
    __tablename__ = 'citation'

    id = Column(Integer, primary_key=True)
    # date = Column(DateTime, default=datetime.datetime.utcnow)
    alias = Column(String, nullable=False, unique=True)
    raw = Column(String, nullable=False, unique=True)  # TODO: is this unique??
    doi = Column(String, unique=True)

    __table_args__ = (
        Index('ix_citation_alias', 'alias'),
        Index('ix_citation_doi', 'doi'),
        Index('ix_citation_raw', 'raw')
    )

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Context(Base):
    __tablename__ = 'context'

    id = Column(Integer, primary_key=True)
    module = Column(String, nullable=False)
    note = Column(String, nullable=True)
    count = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False)

    # TODO: better to call this column citation_id
    # no need to create an index for FK, it's auto created
    reference_id = Column(Integer, ForeignKey('citation.id'))

    # Optional:

    __table_args__ = (
        Index('ix_context_moldule', 'module'),
        Index('ix_context_count', 'count'),
        Index('ix_context_level', 'level')
    )