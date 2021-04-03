import mysql.connector
#Made by Abhay T, Aditya V, and Indrajith G
#MySQL Credentials and Structural Data.
DB_HOST = "johnny.heliohost.org"
DB_USER = "tommymmm_nullvoid"
DB_PASS = "-c=),$4]md${"
DB_NAME = "tommymmm_nullvoid_game"
GAME_TABLE = "nullvoid_scores"
#Function to update player score in MySQL Database.
def update_score(player_details):
    try:
        #Connecting to the MySQL Server.
        db_server = mysql.connector.connect(host = DB_HOST, user = DB_USER, password = DB_PASS, database = DB_NAME)
        db_manager = db_server.cursor()
        #Getting player details from player_details object which is passed to the function while calling the function.
        player_name = player_details[0]
        player_score = player_details[1]
        game_timestamp = player_details[2]
        #Adding player to MySQL Database.
        try:
            db_manager.execute("INSERT INTO " + GAME_TABLE + " VALUES('" + player_name + "', " + str(player_score) + ", " + str(game_timestamp) + ");")
        except:
            #Player already exists, hence overwriting player details with the latest ones in the MySQL Database.
            db_manager.execute("UPDATE " + GAME_TABLE + " SET Time_Taken = " + str(player_score) + ", Time = " + str(game_timestamp) + " WHERE Player_Name = '" + player_name + "';")       
        #Commiting player data to MySQL Database. 
        db_server.commit()
        #Closing the MySQL Server connection.
        try:
            db_manager.close()
            db_server.close()
        except:
            pass
        return True
    except Exception:
        #Just ensuring that the game does not hang while also informing that there is some problem with the MySQL Database.  
        try:
            db_manager.close()
            db_server.close()
        except:
            pass
        return False
def fetch_alldata():
    try:
        db_server = mysql.connector.connect(host = DB_HOST, user = DB_USER, password = DB_PASS, database = DB_NAME)
        db_manager = db_server.cursor()
        db_manager.execute("SELECT * FROM " + GAME_TABLE+ ";")
        pdet = db_manager.fetchall()
        print(pdet)
    except:
        print('err')
def fetch_score(player_name):
    try:
        #Connecting to the MySQL Server.
        db_server = mysql.connector.connect(host = DB_HOST, user = DB_USER, password = DB_PASS, database = DB_NAME)
        db_manager = db_server.cursor()

        #Fetching player's score from MySQL Database.
        db_manager.execute("SELECT Time_Taken, Time FROM " + GAME_TABLE + " WHERE Player_Name = '" + player_name + "';")
        player_details = db_manager.fetchall()
        if player_details == []:
            #Player does not exist in MySQL Database.
            return None
        else:
            #Getting player details tuple from player_details object.
            player = player_details[0]
            #Getting player details from player object.
            player_score = player[0]
            game_timestamp = player[1]
            #Closing the MySQL Server connection.
            try:
                db_manager.close()
                db_server.close()
            except:
                pass
            return [player_name, player_score, game_timestamp]
    except:
        #Just ensuring that the game does not hang while also informing that there is some problem with the MySQL Database.
        #Closing the MySQL Server connection.
        try:
            db_manager.close()
            db_server.close()
        except:
            pass
        return False

if __name__ == '__main__':
    print('Retrieving all Scores',end='\r')
    fetch_alldata()
    ioo=input('> ')
    if ioo=='clear':
        print('ok.')
        db_server = mysql.connector.connect(host = DB_HOST, user = DB_USER, password = DB_PASS, database = DB_NAME)
        db_manager = db_server.cursor()
        db_manager.execute("TRUNCATE TABLE " + GAME_TABLE+ ";")