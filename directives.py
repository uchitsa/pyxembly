from add import Add
from addif import AddIf
from attr import Attr
from remove import Remove
from set import Set
from strict import Strict
from up import Up
from xpath import Xpath

class Directives:
    def __init__(self, text):
        self.array = [Directives.map(t) for t in self.parse_text(text)]
    
    def parse_text(self, text):
        return [t for t in text.strip().split(';') if t]
    
    def __iter__(self):
        return iter(self.array)
    
    def __len__(self):
        return len(self.array)
    
    @staticmethod
    def map(cmd):
        args = cmd.split(',')
        cmd_name = args.pop(0).strip().upper()
        if cmd_name == 'ADD':
            return Add(args[0].strip())
        elif cmd_name == 'ADDIF':
            return AddIf(args[0].strip())
        elif cmd_name == 'ATTR':
            return Attr(args[0].strip(), args[1].strip())
        elif cmd_name == 'CDATA':
            raise Exception('CDATA command is not supported yet, please contribute')
        elif cmd_name == 'NS':
            raise Exception('NS command is not supported yet, please contribute')
        elif cmd_name == 'PI':
            raise Exception('PI command is not supported yet, please contribute')
        elif cmd_name == 'POP':
            raise Exception('POP command is not supported yet, please contribute')
        elif cmd_name == 'PUSH':
            raise Exception('PUSH command is not supported yet, please contribute')
        elif cmd_name == 'REMOVE':
            return Remove()
        elif cmd_name == 'SET':
            return Set(args[0].strip())
        elif cmd_name == 'STRICT':
            return Strict(args[0].strip())
        elif cmd_name == 'UP':
            return Up()
        elif cmd_name == 'XPATH':
            return Xpath(args[0].strip())
        elif cmd_name == 'XSET':
            raise Exception('XSET command is not supported yet, please contribute')
        else:
            raise Exception(f'Unknown command "{cmd_name}"')

