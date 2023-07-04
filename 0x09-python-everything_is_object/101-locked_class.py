#!/usr/bin/python3
"""Class creating new instance and blockinf none stipulated"""
class LockedClass:
    
    def __setattr__(self, name, value):
        try :
            if hasattr(self, name):
                object.__setattr__(self, name, value)
            else:
                raise AttributeError("[AttributeError] 'LockedClass' object has no attribute 'last_name'")
        except AttributeError as e:
            print(e)
