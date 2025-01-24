from fastapi import APIRouter, HTTPException

from clipthread.core.models import JournalCreate, JournalUpdate, Journal
from clipthread.core.db import JournalHandler

router = APIRouter()
journal_handler = JournalHandler("database.db")

@router.post("/", response_model=Journal)
def create_journal(journal: JournalCreate):
    journal_id = journal_handler.create(query=journal.query, session_id=journal.session_id)
    return journal_handler.read(journal_id)

@router.get("/{journal_id}", response_model=Journal)
def read_journal(journal_id: str):
    result = journal_handler.read(journal_id)
    if not result:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    return result

@router.put("/{journal_id}", response_model=Journal)
def update_journal(journal_id: str, journal: JournalUpdate):
    success = journal_handler.update(journal_id, query=journal.query)
    if not success:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    return journal_handler.read(journal_id)

@router.delete("/{journal_id}")
def delete_journal(journal_id: str):
    success = journal_handler.delete(journal_id)
    if not success:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    return {"message": "Journal entry deleted"}