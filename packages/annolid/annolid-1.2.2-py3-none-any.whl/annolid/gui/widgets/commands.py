from PyQt5.QtWidgets import QUndoCommand

class FlagStateCommand(QUndoCommand):
    def __init__(self, checkbox, new_state):
        super().__init__()
        self.checkbox = checkbox
        self.new_state = new_state
        self.old_state = checkbox.isChecked()
        
    def redo(self):
        self.checkbox.setChecked(self.new_state)
        
    def undo(self):
        self.checkbox.setChecked(self.old_state)