"""
This module contains the menu inteface.
"""
import sys
from notebook import Notebook, Note

class Menu:
    """
    This module displays a menu and
    responds to user actions.
    """
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_and_show_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        """
        Print the menu options.
        """
        print((
            "\nNotebook Menu\n" +
            "1. Show all Notes\n" +
            "2. Search Notes\n" +
            "3. Add Note\n" +
            "4. Modify Note\n" +
            "5. Quit\n"
        ), end='')

    def run(self):
        """
        Run the intereative menu in the terminal.
        """
        while True:
            self.display_menu()
            choice = input("Enter option's number: ")
            action = self.choices.get(choice)
            if action:
                print()
                action()
            else:
                print(f"{choice} is not a valid choice")

    def show_notes(self, notes=None):
        """
        This function displays the search results
        if available, otherwise all the notes.
        """
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(note)

    def search_and_show_notes(self):
        """
        Prompt the user to enter the search
        query and find the notes.
        """
        filter_str = input("Search for: ")
        notes = self.notebook.search(filter_str)
        print("Resuts:")
        self.show_notes(notes)
    
    def add_note(self):
        """
        This function adds a new note to the Notebook.
        """
        memo = input("Enter a note: ")
        self.notebook.new_note(memo)
        print("Your note has been saved.")
    
    def modify_note(self):
        """
        This fucntion modifies the note by id.
        """
        print("You can simply enter nothing to abort modification.")
        while True:
            note_id = ""
            while not note_id.isnumeric():
                note_id = input("Enter a note id: ")
                if note_id == "":
                    return
            note_id = int(note_id)
            memo = input("Enter a new memo: ")
            if memo:
                if self.notebook.modify_memo(note_id, memo):
                    print("New memo saved.")
                else:
                    print(
                        "Modification failed!\nMemo was not found (wrong id)."
                    )
                    continue
            tags = input("Enter tags: ")
            if tags:
                if self.notebook.modify_tags(note_id, tags):
                    print("Tags modified.")
                else:
                    print(
                        "Modification failed!\nMemo was not found (wrong id)."
                    )
                    continue
            return

    def quit(self):
        """
        Thank the user and quit
        """
        print("Thanks for using the notebook!")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
