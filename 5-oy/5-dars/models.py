class Week:
    days = [0,1,2,3,4,5,6]

    @classmethod
    def __getitem__(cls,index):
        return cls.days[index]

class Week:

    days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'] 
    
    def __init__(self):
        self.days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'] 
    
    def __getitem__(self,index):
        return self.days[index]

    # @classmethod
    # def get_item(cls,*args):

    #     if len(args) == 1:
    #         result = cls.days[args[0]]
    #     elif len(args) == 2:
    #         result = cls.days[args[0]:args[1]]
    #     elif len(args) == 3:
    #         result = cls.days[args[0]:args[1]:args[2]]
    #     else:
    #         raise TypeError
    #     return result
    
    @classmethod
    def get_item(cls,*args):
        match len(args):
            case 1:
                result = cls.days[args[0]]
            case 2:
                result = cls.days[args[0]:args[1]]
            case 3:
                result = cls.days[args[0]:args[1]:args[2]]
            case _:
                raise TypeError(f'range expected at most 3 arguments, got {len(args)}')
        
        return result

class Month:
    
    def __init__(self):
        self.month = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Now','Dec']
    
    def __getitem__(self,index):
        return self.days[index]
