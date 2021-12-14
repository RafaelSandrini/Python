# SLEEP IN

#  The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

from typing import Text


def sleep_in(weekday, vacation):
    # 1st solution
    #  if not (weekday==True and vacation==False):
    #     return True
    # else:
    #     return False

    # 2nd solution
    return (not weekday or vacation)
    

print (sleep_in(True,False))

