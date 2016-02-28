from bottle import Bottle, run, template, request, response, redirect, static_file
from datetime import datetime
import sqlite3, csv

users = (('hakan', 'hakan', 'Md. Yrd. Hakan'),
         ('deneme1', 'deneme1', 'DENEME 1'),
         ('deneme2', 'deneme2', 'DENEME 2'),
         ('deneme3', 'deneme3', 'DENEME 3'),
         ('deneme4', 'deneme4', 'DENEME 4')
            )

DB_FILE = 'db.sqlite'
CSV_FILE = 'db.csv'
ADMIN = 'hakan'
SECRET = 'secret key of hakan'

ALERT_HTML = """<html lang="tr">
              <head><link rel="stylesheet" href="/static/bootstrap.min.css"></head>
              <body><div class="alert {}" role="alert">{}</div>
              &nbsp;&nbsp;&nbsp;&nbsp;<a href="/" class="btn btn-primary"> < GERİ DÖN</a></body></html>"""


def check_user(username, password):
    success = False
    
    for user in users:
        if username == user[0] and password == user[1]:
            success = True
            return success
    
    return success  #False, no login        

def login_user(username, password):
    response.set_cookie("logged_user", username, secret=SECRET)
    
def logout_user():
    response.delete_cookie("logged_user")
    
def get_user():
    return request.get_cookie("logged_user", False, secret=SECRET)
    
def get_user_full_name():
    username = request.get_cookie("logged_user", False, secret=SECRET)
    for user in users:
        if username == user[0]:
            return user[2]

def is_admin():
    return ADMIN == request.get_cookie("logged_user", False, secret=SECRET)
    

app = Bottle()

@app.route('/test')
def hello():
    data = ""
    return data

@app.post('/')
def index():
    
    username = request.forms.get("username")
    password = request.forms.get("password")
    
    if check_user(username, password) == True:
        login_user(username, password)
        redirect("/")
    else:
        err_msg = "HATALI KULLANICI ADI VEYA ŞİFRE!"
        return template('tpl/login.tpl', err_msg=err_msg)
    
    return


@app.get('/')
def index():
    
    if get_user() == False:
        return template('tpl/login.tpl')
    else:
        return template('tpl/main.tpl', user=get_user(), user_full_name=get_user_full_name(), is_admin=is_admin())


@app.post('/ogrenci')
def ogrenci():
    if get_user() == False: return "KULLANICI HATASI"
        
    ogrenci_no = request.forms.get("ogr_no")
        
    # Set Connection
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # get student user name
    c.execute("select * from ogrenci where no=?", (ogrenci_no,) )
    cur_data = c.fetchone()
    
    # no student, stop
    if cur_data == None:
        return ALERT_HTML.format("alert-danger", "ÖĞRENCİ NUMARASI YANLIŞ!")
                
    # get student books
    c.execute("select * from odunc where no=? AND alan is NULL", (ogrenci_no,) )
    ogr_book = c.fetchone()
    
    has_book = not (ogr_book == None)

    info = {'msg1': '', 'msg2': '', 'msg3': '' }
    return template('tpl/ogrenci.tpl', cur_data=cur_data, has_book=has_book, ogr_book=ogr_book, info=info, user=get_user(), user_full_name=get_user_full_name(), is_admin=is_admin())


@app.post('/ogrenci/oduncver')
def oduncver():
    if get_user() == False: return "KULLANICI HATASI"
    
    ogrenci_no = request.forms.get("ogr_no")
    ogrenci_sinif = request.forms.get("ogr_sinif")
    ogrenci_adsoyad = request.forms.get("ogr_adsoyad")

    kitap = request.forms.get("kitap")
    
    # Set Connection
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # insert record
    c.execute("INSERT INTO odunc (no, sinif, adsoyad, veren, verme_tarihi, kitap) VALUES(?, ?, ?, ?, ?, ?)", (ogrenci_no, ogrenci_sinif, ogrenci_adsoyad, get_user_full_name(), datetime.now(), kitap) )
    conn.commit()
    
    return ALERT_HTML.format("alert-success", "KİTAP ÖDÜNÇ VERİLDİ.")


@app.post('/iade')
def iade():
    if get_user() == False: return "KULLANICI HATASI"

    odunc_id = request.forms.get("odunc_id")
    
    # Set Connection
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # update record
    c.execute("UPDATE odunc SET alan=?, alma_tarihi=? WHERE id=?", (get_user_full_name(), datetime.now(), odunc_id))
    cur_data = c.fetchone()
    conn.commit()

    return ALERT_HTML.format("alert-success", "KİTAP İADE EDİLDİ.")
    
@app.get('/logout')
def logout():
    logout_user()
    redirect("/")

@app.get('/update_users')
def admin_update_users():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("delete from ogrenci where 1=1")
    
    with open(CSV_FILE, encoding="utf-8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            c.execute("INSERT INTO ogrenci (no, sinif, adsoyad) VALUES (?,?,?)", (row[0], row[1] ,row[2])  )
    
    conn.commit()
    return ALERT_HTML.format("alert-success", "KAYITLAR GÜNCELLENDİ...")
    

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')


run(app, host='0.0.0.0', port=8080, reloader=True)








