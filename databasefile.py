import mysql.connector


# connection = mysql.connector.connect(
#     host="localhost",
#     user="yekta",
#     password="Yekta-5310",
#     database="qc"
# )



# def retrieve_standards():
   

#     cursor = connection.cursor()


#     query = "SELECT standardname FROM standard"
#     cursor.execute(query)
#     items = cursor.fetchall()

#     cursor.close()
#     connection.close()

#     if items:
#         return items
#     else:
#         return None
    




def retrieve_standardss():
   
    connection = mysql.connector.connect(
        host="85.185.84.197",
        user="yekta",
        password="Yekta-5310",
        database="qc2"
    )

    cursor = connection.cursor()


    query = "SELECT standardname FROM standard"
    cursor.execute(query)
    items = [row[0] for row in cursor.fetchall()]


    cursor.close()
    connection.close()

    if items:
        return items
    else:
        return None



def retrieve_standardparam(selected_name):


    connection = mysql.connector.connect(
    host="85.185.84.197",
    user="yekta",
    password="Yekta-5310",
    database="qc2"
    )

    cursor = connection.cursor()

    query = f"SELECT * FROM standard WHERE standardname = %s"
    # query = f"SELECT testtime, intervaltemp, durationamperage, intervalamperage, gastype, tolerancepercent, sensorstat1, sensorstat2, sensorstat3, sensorstat4, sensorstat5, sensorstat6, sensorstat7, sensorstat8, ampstat, voltstat, averagetemperature1, averagetemperature2, averagetemperature3, averagetemperature4, averagetemperature5, averagetemperature6, averagepressure_min, averagepressure_max, averageamp, averagevolt FROM standard WHERE standardname = %s"
    cursor.execute(query, (selected_name,))
    result = cursor.fetchone()



    cursor.close()
    connection.close()
    return result



