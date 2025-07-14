import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student1.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table 
ID INTEGER PRIMARY KEY, 
STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values(1,'Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values(2,'Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values(3,'Darius','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values(4,'Vikash','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values(5,'Dipesh','DEVOPS','A',35)''')
cursor.execute('''Insert Into STUDENT values(6,'Utkarsh','Security','C',86)''')
cursor.execute('''Insert Into STUDENT values(7,'Akash','Security','D',92)''')
cursor.execute('''Insert Into STUDENT values(8,'Rama','DEVOPS','B',75)''')
cursor.execute('''Insert Into STUDENT values(9,'Astha','DEVOPS','C',32)''')


## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()
