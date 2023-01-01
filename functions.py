import datetime
import math
import re
import string as st
def check_user(userid):
    accept =False
    with open("users.txt") as file:
        rf = file.readlines()
    rf = [r.rstrip() for r in rf]
    if userid in rf: accept=True
    return accept


def zapis(id, uname,com):
    with open("log.txt", 'a') as faylzapis:
        faylzapis.write(f"{datetime.datetime.now()}; {str(id)};  {uname};  {com} \n")

def chekadmin(id):
    accept =False
    with open("admins.txt") as file:
        rf = file.readlines()
    rf = [r.rstrip() for r in rf]
    if id in rf: accept=True
    return accept

def addUser(id):
    with open("users.txt", 'a') as idadd:
        idadd.write(f"\n{id}")

