'''
C2) The Undo Machine
You're building a lightweight text editor for a startup. Every time a user types a character, it gets recorded When they press Ctrl+Z (Undo) the last action must be reversed. The editor must support.
type(char)-records a character
undo() removes the last typed character
getText()returns the current text

'''

class Que2:
    def __init__(self):
        self.stack=[]
    def type_char(self,c):
        self.stack.append(c)
        print(f"current data:{''.join(self.stack)}")
    def undo(self):
        self.stack.pop()
        print(f"current data:{''.join(self.stack)}")
    def getText(self):
        print(f"current data:{''.join(self.stack)}")

obj=Que2()
obj.type_char('a')
obj.type_char('b')
obj.type_char('c')
obj.type_char('d')
obj.type_char('e')
obj.undo()
obj.type_char('f')
obj.getText()