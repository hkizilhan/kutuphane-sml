from bottle import Bottle, run, template, request, response, redirect, static_file
from datetime import datetime
import sqlite3, os, csv
import xlrd

users = list()
# ('hakan', 'hakan', 'Md. Yrd. Hakan'),


VERSION = 0.02
DB_FILE = 'db.sqlite'
XLS_FILE = 'liste.xls'
USERS_FILE = 'users.xls'
ADMIN = 'admin'
SECRET = 'secret key of hakan'
COOKIE_TIMEOUT = None


def upper_tr(in_str):
    upper_map = {
        ord('ı'): 'I',
        ord('i'): 'İ',}
    
    in_str = in_str.translate(upper_map).upper()
    return in_str


def alert_html(msg, alert_type="alert-success"):
    ALERT_HTML = """<html lang="tr">
              <head><link rel="stylesheet" href="/static/bootstrap.min.css"></head>
              <body><div class="alert {}" role="alert">{}</div>
              <a href="/" class="btn btn-primary" style="margin-left: 20px"> < GERİ DÖN</a></body></html>"""
    return ALERT_HTML.format(alert_type, msg)
    

def check_user(username, password):
    success = False
    
    for user in users:
        if username == user[0] and password == user[1]:
            success = True
            return success
    
    return success  #False, no login        

def login_user(username, password):
    response.set_cookie("logged_user", username, secret=SECRET, max_age=COOKIE_TIMEOUT)
    
def logout_user():
    response.delete_cookie("logged_user")
    
def get_user():
    user_name = request.get_cookie("logged_user", False, secret=SECRET) 
    
    if user_name == False: return False
    else:
        response.set_cookie("logged_user", user_name, secret=SECRET, max_age=COOKIE_TIMEOUT)
            
    return user_name
    
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
    if get_user() == False: return redirect("/")
        
    ogrenci_no = request.forms.get("ogr_no")
        
    # Set Connection
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # get student user name
    c.execute("SELECT * FROM ogrenci WHERE no=?", (ogrenci_no,) )
    cur_data = c.fetchone()
    
    # no student, stop
    if cur_data == None:
        return alert_html("ÖĞRENCİ NUMARASI YANLIŞ!", "alert-danger")
                
    # get student books
    c.execute("SELECT * FROM odunc WHERE no=? AND teslim_alan is NULL", (ogrenci_no,) )
    ogr_book = c.fetchone()
    
    has_book = not (ogr_book == None)

    return template('tpl/ogrenci.tpl', cur_data=cur_data, has_book=has_book, ogr_book=ogr_book, user=get_user(), user_full_name=get_user_full_name(), is_admin=is_admin())


@app.post('/ogrenci/oduncver')
def oduncver():
    if get_user() == False: return redirect("/")
    
    ogrenci_no = request.forms.get("ogr_no")
    ogrenci_sinif = request.forms.get("ogr_sinif")
    ogrenci_adsoyad = request.forms.get("ogr_adsoyad")

    kitap = request.forms.get("kitap")
    
    # Set Connection
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # get student books
    c.execute("SELECT * FROM odunc WHERE no=? AND teslim_alan is NULL", (ogrenci_no,) )
    ogr_book = c.fetchone()
    
    if (ogr_book != None):
        return alert_html("ÖĞRENCİDE ZATEN BİR KİTAP VAR!", "alert-danger")
    
    
    # insert record
    c.execute("INSERT INTO odunc (no, sinif, adsoyad, odunc_veren, odunc_verme_tarihi, kitap) VALUES(?, ?, ?, ?, ?, ?)", (ogrenci_no, ogrenci_sinif, ogrenci_adsoyad, get_user_full_name(), datetime.now(), upper_tr(kitap) ))
    conn.commit()
    
    return alert_html("KİTAP ÖDÜNÇ VERİLDİ.", "alert-success")


@app.post('/iade')
def iade():
    if get_user() == False: return redirect("/")

    odunc_id = request.forms.get("odunc_id")
    
    # Set Connection
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # update record
    c.execute("UPDATE odunc SET teslim_alan=?, teslim_alma_tarihi=? WHERE id=?", (get_user_full_name(), datetime.now(), odunc_id))
    cur_data = c.fetchone()
    conn.commit()

    return alert_html("KİTAP İADE EDİLDİ.", "alert-success")
    
@app.get('/logout')
def logout():
    logout_user()
    redirect("/")

@app.get('/odunctekiler')
def admin_loan_book_list():
    if is_admin() == False: return redirect("/")
    
    # Set Connection
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # update record
    c.execute("SELECT * FROM odunc WHERE teslim_alan is NULL ORDER BY sinif, no")
    cur_data = c.fetchall()
    
    counter = 1
    
    return template('tpl/odunctekiler.tpl', counter=counter, cur_data=cur_data, user=get_user(), user_full_name=get_user_full_name(), is_admin=is_admin())
    
@app.get('/odunctekiler/csv')
def admin_loan_book_list_csv():
    if is_admin() == False: return redirect("/")
    
    # Set Connection
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # update record
    c.execute("SELECT * FROM odunc WHERE teslim_alan is NULL ORDER BY sinif, no")
    cur_data = c.fetchall()
    
    from io import StringIO
    out = StringIO()
    csv_writer = csv.writer(out, delimiter=',')
    
    for row in cur_data:
        csv_writer.writerow([row[1], row[2], row[3], row[8], row[5].split(".", 1)[0], row[4] ])
    
    response.headers['Content-type'] = 'text/csv'
    response.headers['Content-Disposition'] = 'attachment; filename="liste.csv"'
    
    return out.getvalue()


@app.get('/update_users')
def admin_update_users():
    if is_admin() == False: return redirect("/")
    
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("delete from ogrenci where 1=1")
    
    book = xlrd.open_workbook(filename=XLS_FILE)
    sh = book.sheet_by_index(0)
    
    for rx in range(sh.nrows):
        no    = int( sh.cell_value(rowx=rx, colx=0) )
        
        sinif = str( sh.cell_value(rowx=rx, colx=1) )
        sinif = sinif.replace("/","-")
        
        ad    = str( sh.cell_value(rowx=rx, colx=2) )
        
        c.execute("INSERT INTO ogrenci (no, sinif, adsoyad) VALUES (?,?,?)", (no, sinif ,ad)  )
        
            
    conn.commit()
    return alert_html("KAYITLAR GÜNCELLENDİ...", "alert-success")
    

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')
    
@app.route('/static/eokul/<filename>')
def server_static(filename):
    # format filename as 001.jpg
    filename=filename.rjust(7, "0")
    # check for extension case, .jpg or .JPG
    if not os.path.isfile("./static/eokul/" + filename):
        filename=filename.upper()

    return static_file(filename, root='./static/eokul')


# Set db file if not exist
try:
    my_file = open(DB_FILE)
    my_file.close()
except IOError:
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('CREATE TABLE "ogrenci" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , "no" INTEGER NOT NULL , "sinif" VARCHAR NOT NULL , "adsoyad" VARCHAR NOT NULL )')
    c.execute('CREATE TABLE "odunc"   ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , "no" INTEGER NOT NULL , "sinif" VARCHAR NOT NULL , "adsoyad" VARCHAR NOT NULL , "odunc_veren" VARCHAR NOT NULL , "odunc_verme_tarihi" DATETIME NOT NULL , "teslim_alan" VARCHAR, "teslim_alma_tarihi" DATETIME, "kitap" VARCHAR NOT NULL )')
    conn.commit()
    



# Load Users
users_xls = xlrd.open_workbook(filename=USERS_FILE)
users_sh  = users_xls.sheet_by_index(0)
    
for rx in range(users_sh.nrows):
    
    cell = users_sh.cell(rx, 0)
    if cell.ctype == xlrd.XL_CELL_NUMBER:
        user_name = str(int(cell.value))
    else:
        user_name = str(cell.value)
    
    cell = users_sh.cell(rx, 1)
    if cell.ctype == xlrd.XL_CELL_NUMBER:
        password = str(int(cell.value))
    else:
        password = str(cell.value)
    
    cell = users_sh.cell(rx, 2)
    if cell.ctype == xlrd.XL_CELL_NUMBER:
        adsoyad = str(int(cell.value))
    else:
        adsoyad = str(cell.value)
    
    users.append([user_name, password, adsoyad])
    

run(app, host='0.0.0.0', port=8080, reloader=True, debug=True)








