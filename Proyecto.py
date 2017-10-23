import psycopg2.extensions



conn = psycopg2.connect(database="byron", user="postgres", password="1234", host="192.168.149.131")# el host se debe cambiar dependiendo de la base de datos.

#print "correcto"

conn.autocommit = True
cur = conn.cursor()

def Create_Database():

    try:

        name = raw_input('Write the Data Base name: ')
        User = raw_input('Write the owner of the new databse')

        cur.execute("CREATE DATABASE " + name + " WITH OWNER '" + User + "';")

    except:

        print "DateBase not created"

def Create_New_Table():

    try:

        name = raw_input('Write the table name: ')
        Atributos = raw_input('Insert name, type y characteristics of the attributes:')

        cur.execute("CREATE TABLE " + name + "(" + Atributos + ");")

    except:

        print "Table not created"

def Insert_data():

    try:

        name = raw_input('table name: ')
        #Attribute_name = raw_input('Write the attribute name separated by a , : ')
        Values = raw_input('Write the values of the attribute :')

        cur.execute("INSERT INTO " + name + " VALUES (" + Values + ");")

    except:

        print "Data not inserted"

def Erase_table():

    try:

        name = raw_input(' Write the table name that you want to erase: ')

        cur.execute("DROP TABLE " + name + ";")

    except:

        print "table not droped"

def Modify_table():

    try:

        name = raw_input(' Write the table name you want to make an alter ')
        Attribute_name = raw_input('Write the attribute you want to change : ')
        New_Attribute = raw_input('Write de new name of the old attribute')

        cur.execute("ALTER TABLE " + name + " RENAME COLUMN " + Attribute_name + " TO " +  New_Attribute + ";")

    except:

        print "Alter wasn't made"

def Erase_info():

    try:

        name = raw_input(' Write the table name you want to erase info ')
        Attribute_name = raw_input('Write the attribute : ')

        cur.execute("Delete from " + name + " where column =  " + Attribute_name + ";")



    except:

        print "Delete not made"

def Modify_data():

    try:

        name = raw_input(' Write the table name ')
        Attribute_name = raw_input('Write the attribute : ')
        Values = raw_input('Write the values of the attribute separated by a , :')

        cur.execute("Update " + name + " set " + Attribute_name +  " = " + Values + ";")

    except:

        print "Update not made"


def Modify_Role ():

    try:

        Role_Name = raw_input(' Write the Role Name: ')

        cur.execute("ALTER ROLE " + Role_Name + "WITH SUPERUSER;")

    except:

        print "Alter Role name not made"

def Modify_Role_Password ():
    try:

        Role_Name = raw_input(' Write the Role Name: ')
        New_Password = raw_input('Write the new password')

        cur.execute("ALTER ROLE " + Role_Name + "WITH PASSWORD " + New_Password + ";")

    except:

        print "Alter Role Password not made"

def Create_index():

    try:

        name = raw_input('Write the index name: ')
        Table_name = raw_input('Write table name')
        Colum_Name = raw_input('Write the colum name')

        cur.execute("CREATE Unique index  " + name + "on" + Table_name + (Colum_Name) + ";")

    except:

        print "Index not created1"


def Menu ():

    try:

        while True:

            OpcionMenu = raw_input("Choose: "
                          "\n1. Create data base"
                          "\n2. Create table"
                          "\n3. Insert data"
                          "\n4. Erase table"
                          "\n5. Modify table"
                          "\n6. Erase tabla data"
                          "\n7. Modify data"
                          "\n8. Modify role"
                          "\n9. Modify role password"
                          "\n10. Create index"
                          "\n.11 Exit"
                          "\n")

            if OpcionMenu == "1":

                print ("")

                raw_input("You enter on the data base " + Create_Database())

            elif OpcionMenu == "2":

                print ("")

                raw_input("You enter on the table " + Create_New_Table())

            elif OpcionMenu == "3":

                print("")

                raw_input("insert the informacion " + Insert_data())

            elif OpcionMenu == "4":

                print("")

                raw_input("You can erade a table " + Erase_table())

            elif OpcionMenu == "5":

                print("")

                raw_input("Modify " + Modify_table())

            elif OpcionMenu == "6":

                print("")

                raw_input("Erase information " + Erase_info())

            elif OpcionMenu == "7":

                print("")

                raw_input("Modify the data " + Modify_data())

            elif OpcionMenu =="8":

                print("")

                raw_input("Modify the role " + Modify_Role())

            elif OpcionMenu == "9":

                print("Modify the role password ")

                raw_input("Modify the role password " + Modify_Role_Password())

            elif OpcionMenu == "10":

                print("")

                raw_input("Modify the role password " + Create_index())

            elif OpcionMenu == "11":

                print ("")

                input("Exit")

            else:

                print ("")

                raw_input("You don't choose a correct opcion please try again, press any botton to retunr to the menu")

    except:

        print "Seleccion of the menu was wrong"

print Menu()

cur.close

