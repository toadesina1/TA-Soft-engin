import unittest

from commands import AddBookmarkCommand, ListBookmarksCommand, DeleteBookmarkCommand
from database import DatabaseManager


Test to check if bookmark is added______

class AddBookmarkCommandTestCase(unittest.TestCase):
    def test_add_bookmark(self):
        data['date_added'] = datetime.utcnow().isoformat()
        db.add(commands.AddBookmarkCommand ("001" "Aje site" "www.local.com", "we work here", "2/22/2021"))
        assert db.add.bookmark("ww.local.com") is not None
        assert db.add.committed

#Test to check if bookmark was listed______


class ListBookmarksCommandTestCase(unittest.TestCase):
    def test_list_bookmarks(self):
 	db.select(commands.ListBookmarksCommand ("007" "Group work" "www.groupus.com", "we are here", "1/22/2021"))
        assert db.select.bookmark("ww.groupus.com") is not None
        assert db.select.committed


#Test to check if bookmark was deleted______

class DeleteBookmarkCommandTestCase(unittest.TestCase):
    def test_delete_bookmarks(self):
   	db.delete(commands.DeleteBookmarkCommand ("001" "Aje site" "www.local.com", "we work here", "2/22/2021"))
        assert db.delete.bookmark("www.local.com") is not None
        assert db.delete.committed

class QuitCommand:
    def execute(self):
        sys.exit()




