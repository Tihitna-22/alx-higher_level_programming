#!/usr/bin/python3
class LockedClass:
    """LockedClass with no class or object attribute cexcept if the new instance attribute is called first_name"""
    __slots__ = ['first_name']
