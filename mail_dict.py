#Mohamed Ben Hammou
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="mohamed",
    password="asixstudent",
    database="my_base_datos"
)

# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM nombre_email")
# myresult = mycursor.fetchall()

NOTROBAT = "NOTROBAT"
AFEGIT = "AFEGIT"
MODIFICAT = "MODIFICAT"
JAEXISTEIX = "JAEXISTEIX"

#ditection de mail
def getmaildict(nom):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM nombre_email")
    myresult = mycursor.fetchall()
    for x in myresult:
        if nom == x[0]:
            email = x[1]
            return email
    return NOTROBAT

def addmaildict(nom, correu, modif=False):
    oldcorreu = getmaildict(nom)
    if oldcorreu == NOTROBAT:
        sql = "INSERT INTO nombre_email (nombre, email) VALUES (%s, %s)"
        val = (nom, correu)
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        return AFEGIT

    elif oldcorreu != correu and modif:
        sql = "UPDATE nombre_email SET email = %s WHERE nombre = %s"
        val = (correu, nom)

        mycursor.execute(sql, val)
        mydb.commit()
        return MODIFICAT

    return JAEXISTEIX
