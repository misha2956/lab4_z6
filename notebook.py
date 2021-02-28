"""
This module contains the Note and Notebook classes.
"""
import datetime

# The next available id for a new note
available_id = 0

class Note:
    """
    Represents a note in the notebook.
    Contains functionality for searching
    """

    def __init__(self, memo: str, tags: str=''):
        """
        Initialize a note from its memo and provided tags
        (space-separated, optional).
        The note's creation date and id are set automatically.
        """
        self.memo = memo
        self.tags = tags

        self.creation_date = datetime.date.today()

        global available_id
        available_id += 1
        self.id = available_id

    def match(self, filter_str: str) -> bool:
        """
        Check wheter the note or its tags
        match the filter query.
        Search is not case sensitive.
        """
        filter_str = filter_str.lower()
        return (
            filter_str in self.memo.lower() or
            filter_str in self.tags.lower()
        )
    
    def __repr__(self):
        """
        A representation function.
        """
        return (
            "<Note(" + ", ".join([
                elem.__repr__()
                for elem in [
                    self.memo, self.tags
                ]  # vars(self).values()
            ]) + ")" + f" id={self.id.__repr__()}" + ">"
        )

    def __str__(self):
        """
        This funciton returns a string representation of the note
        """
        return f"{self.id}: {self.tags}\n{self.memo}"


class Notebook:
    """
    This class represents a collection of notes
    that can be tagged, modified, and searched.
    """

    def __init__(self):
        """
        Initialize notebook's notes with an empty list.
        """
        self.notes = []

    def new_note(self, memo: str, tags: str=''):
        """
        Create a new note and append it to the memory.
        """
        self.notes.append(Note(memo, tags))

    def _find_note_by_id(self, note_id: int) -> Note:
        """
        Return the note with the given id.
        If not found, returns None.
        """
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self, note_id: int, new_memo: str) -> bool:
        """
        Find the note with the given id
        and change its memo to the given value.
        Returns True if the memo was found,
        False otherwise.
        """
        note = self._find_note_by_id(note_id)
        if note is not None:
            note.memo = new_memo
            return True
        else:
            return False

    def modify_tags(self, note_id: int, new_tags: str) -> bool:
        """
        Find the note with the given id
        and change its tags to the given value.
        Returns True if the memo was found,
        False otherwise.
        """
        note = self._find_note_by_id(note_id)
        if note is not None:
            note.tags = new_tags
            return True
        else:
            return False

    def search(self, filter_str: str):
        '''
        Returns all notes that match
        the given filter query.
        Search is not case sensitive.
        '''
        return [
            note
            for note in self.notes
            if note.match(filter_str)
        ]