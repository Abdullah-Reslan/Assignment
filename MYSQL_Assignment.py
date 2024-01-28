# Q1
'''
- Database is an Enviroment , where we can store diffrent Types and amount of Data.
To use this Databse i have to connect with this Enviroment. 

- SQL (Structerd Query Language) such as Tables

- NoSQL (not only Stuctured Query Language) auch as Images , vidoes , ... etc.


'''

# Q2 
'''
- DDL means Data Definition Language

- CREATE : is used to creat  Tables , databases , schema, etc.

- DROP : is used to drop/remove tables and other database objects.

- ALTER : is used to alter or change the definiton of Database objects

- TRUNCATE : is used to remove tables , procedures, and other database
'''








import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE Table if not exists test1.assignment (c1 INT , c2 VARCHAR(40), c3 FLOAT)")
#mydb.close()
#mycursor.execute("DROP Table test1.assignment")

#mycursor.execute("CREATE Table if not exists test1.assignment (c1 INT , c2 VARCHAR(40), c3 FLOAT)")
#mydb.close()
#mycursor.execute('''
#ALTER Table test1.assignment
#ADD COLUMN c4 INT  
#''')
#mydb.commit()
#mydb.close()

#mycursor.execute("TRUNCATE TABLE test1.assignment")
#mydb.commit()
#mydb.close()


# Q3 

'''
DML : is Data Manipulation Language

- INSERT : is used to add data to a spesicif Column or a Table

- UPDATE : is used to change the value of a row 

- DELETE :is used to delete the value of a row 

'''
 
#mycursor.execute("insert into test1.assignment values(545, 'Query', 54.5, 45)")
#mydb.commit()
#mydb.close()

#mycursor.execute(''' 
#update test1.assignment 
#set c2 = 'Data', c3 = 10000
# ''')
#mydb.commit()
#mydb.close()

#mycursor.execute("select * from test1.assignment")
#for i in mycursor.fetchall():
  #print(i)
  
#mycursor.execute('''
 # DELETE FROM test1.assignment
  #WHERE c1 = '545'
  #''')
#mydb.commit()
#mydb.close()


# Q4

'''
DQL : is Data Query Language 

mycursor.execute("select * from test1.assignment")
for i in mycursor.fetchall():
  print(i)
'''


# Q6 

'''
impor tmysql.connector

mydb = mysql.connector.connect(
  host = "localhost"
  user = "abc"
  password = "password"
)
mycursor = mydb.cursor()
mycursor.execute("")
'''

''' 
- cursor() method is used to creat a cursor object assiciated with the database connection and its like a pointer
to the result set of SQL query. It allowes you to exceute sql commands and retrieve data from the database.


- execute() Methode is used to execute sql commands or queries using the cursor object
'''



# Q7

'''
1. FROM
2. JOIN
3. WHERE
4. GROUP BY
5. HAVING
6. SELECT
7. DISTINCT
8. ORDER BY
9. LIMIT/OFFSET 
'''