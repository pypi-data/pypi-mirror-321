import unittest
import os
from clipthread.core.db import ClipboardHandler, JournalHandler

class TestDatabaseHandlers(unittest.TestCase):
    def setUp(self):
        self.test_db = "test.db"
        self.clipboard_handler = ClipboardHandler(self.test_db)
        self.journal_handler = JournalHandler(self.test_db)

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_clipboard_crud(self):
        # Create
        clip_id = self.clipboard_handler.create("test clip", pinned=False)
        self.assertIsNotNone(clip_id)

        # Read
        clip = self.clipboard_handler.read(clip_id)
        self.assertIsNotNone(clip)
        self.assertEqual(clip.text, "test clip")
        self.assertEqual(clip.pinned, False)

        # Update
        updated = self.clipboard_handler.update(clip_id, text="updated clip", pinned=True)
        self.assertTrue(updated)
        
        updated_clip = self.clipboard_handler.read(clip_id)
        self.assertEqual(updated_clip.text, "updated clip")
        self.assertEqual(updated_clip.pinned, True)

        # Delete
        deleted = self.clipboard_handler.delete(clip_id)
        self.assertTrue(deleted)
        self.assertIsNone(self.clipboard_handler.read(clip_id))

    def test_journal_crud(self):
        # Create
        session_id = "test_session"
        journal_id = self.journal_handler.create("test query", session_id)
        self.assertIsNotNone(journal_id)

        # Read
        journal = self.journal_handler.read(journal_id)
        self.assertIsNotNone(journal)
        self.assertEqual(journal["query"], "test query")
        self.assertEqual(journal["session_id"], session_id)

        # Update
        updated = self.journal_handler.update(journal_id, "updated query")
        self.assertTrue(updated)
        
        updated_journal = self.journal_handler.read(journal_id)
        self.assertEqual(updated_journal["query"], "updated query")

    def test_nonexistent_items(self):
        self.assertIsNone(self.clipboard_handler.read("nonexistent"))
        self.assertIsNone(self.journal_handler.read("nonexistent"))

if __name__ == '__main__':
    unittest.main()