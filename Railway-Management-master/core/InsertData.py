import csv
import mysql.connector as con

def InsertDataTrain():
    mn = con.connect(host="localhost",
                     user='root',
                     password='root',
                     database="railway")

    cur = mn.cursor()
    try:
        with open("C:\\Users\\unqki\\Downloads\\Railway-Management-master\\Railway-Management-master\\Assets\\Train_details.csv") as csv_data:
            csv_reader = csv.reader(csv_data, delimiter=",")
            for row in csv_reader:
                cur.execute(
                    'INSERT INTO train_info VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
    except FileNotFoundError:
        print("Please check whether the file is in the Assets Folder or not and try changing the Location in InsertData.py")
    finally:
        mn.commit()
        cur.close()
        mn.close()
