# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
import json

import requests


def index():
    return dict()


def find_finger():
    import serial
    ser = serial.Serial('/dev/ttyACM0', 9600)
    ser.write('5')
    #ser.write(b'5') #Prefixo b necessario se estiver utilizando Python 3.X
    while True:
        line = ser.readline()
        print line
        if "FINGERFOUND" in line:
            id= line.split(",")[1]
            ser.close()
            print id
            r = requests.get("http://174.138.34.125:8081/walletapi/customer/%s/" % id)
            return r.text


def billing():
    value = request.vars.value
    cardId = request.vars.cardId
    url = "http://174.138.34.125:8081/walletapi/creditCard/%s/transaction/%s" % (cardId,value)

    headers = {
        'merchantid': "872fbdc6-4ff7-441a-94ce-536c3f1500f8",
        'merchantkey': "XPIUJIUHHVSIQWBPUMXRZJBERBOIAIOZNRRWCHEY",
        'cache-control': "no-cache",
        'postman-token': "a921eb43-37dd-4bb0-f49f-1df0e660cd65"
    }

    response = requests.request("POST", url, headers=headers)

    return response.text


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
