import pyodbc
import pandas as pd
import time
import socket
import ctypes
import os
from sqlalchemy import create_engine, text
import urllib.parse


class ATIBotLog:
    def __init__(self, config,db_params):
        """
        Initialize the BotAutomation object with configuration and DB connection parameters.
        :param config: Dictionary containing bot details and parameters like Bot_File_Name, Bot_Version, etc.
        :param db_params: Dictionary containing database connection parameters like server, user, password, etc.
        """
        self.config = config
        self.start_time = time.strftime("%m/%d/%y %H:%M:%S")
        self.today = pd.to_datetime('today')
        self.portal_id = os.getlogin()  # Replace with actual logic to get portal ID
        self.full_name = self.get_user_name()  # Replace with actual logic to get full name
        self.domain = self.get_domain_name()
        self.db_params=db_params
        # Create SQLAlchemy engine connection
        self.engine = self.create_engine_connection()
        self.insert_and_log_bot_data()



    def get_user_name(self):
        """Fetch the full name of the user."""
        GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
        NameDisplay = 3
        size = ctypes.pointer(ctypes.c_ulong(0))
        GetUserNameEx(NameDisplay, None, size)

        nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
        GetUserNameEx(NameDisplay, nameBuffer, size)
        return nameBuffer.value

    def get_domain_name(self):
        """Determine if the domain is valid (e.g., nttdata or keane)."""
        domain_name = socket.getfqdn(socket.gethostbyname(socket.gethostname())).lower()
        return 'YES' if ('nttdata' in domain_name) or ('keane.com' in domain_name) else 'NO'

    def create_engine_connection(self):
        """Establish the connection to SQL Server using SQLAlchemy."""
        try:
            params = urllib.parse.quote_plus(
                f'Driver={self.db_params["driver"]};'
                f'Server={self.db_params["server"]};'
                f'Database={self.db_params["database"]};'
                f'UID={self.db_params["username"]};'
                f'PWD={self.db_params["password"]};'
            )
            engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}", fast_executemany=True)
            return engine
        except Exception as e:
            raise e

    def insert_and_log_bot_data(self):
        try:
            bot_file_name = self.config['Bot_File_Name']
            bot_version = self.config['Bot_Version']
            updated_key = self.config['BOT_Updated_Key']

            # Check if data exists for the bot file
            check_query = """SELECT COUNT(1) FROM tbl_ATI_BOT_Owner_Details WHERE Bot_File_Name =:bot_file_name and Bot_Version=:bot_version"""
            with self.engine.connect() as conn:
                result = conn.execute(text(check_query), {'bot_file_name': bot_file_name, 'bot_version': bot_version}).fetchone()
           
            if result and result[0] > 0:
                print(f"Data for {bot_file_name} version {bot_version} already exists. Skipping insertion into Owner Table.")
            else:
                # Insert bot owner data if not already present
                owner_data = [
                    self.config['Bot_File_Name'],
                    self.config['BOT_Updated_Key'],
                    self.config['Bot_Version'],
                    self.config['BoT_Type'],
                    self.config['BoT_Description'],
                    self.config['Deployed_Date'],
                    self.config['ClientDomain'],
                    self.config['ClientName'],
                    self.config['DeliverTo'],
                    self.config['Bot_Owner'],
                    self.config['ManualTimeSaving_PerTransation_in_Mins'],
                    self.config['OffShoreOrOnShore'],
                    self.config['Remarks']
                ]
                conn = pyodbc.connect(f"Driver={{SQL Server}};Server={self.db_params['server']};"
                                      f"Database={self.db_params['database']};UID={self.db_params['username']};"
                                      f"PWD={self.db_params['password']};")
                cursor = conn.cursor()

                cursor.execute("""
                    INSERT INTO tbl_ATI_BOT_Owner_Details
                    (Bot_File_Name, Bot_Updated_Key, Bot_Version, BoT_Type, BoT_Description, Deployed_Date, ClientDomain, ClientName, DeliverTo, Bot_Owner, ManualTimeSaving_PerTransation_in_Mins,OffShoreOrOnShore,Remarks)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, owner_data)
                conn.commit()
                cursor.close()
                print("Owner data inserted successfully.")

            # Check if the Bot_Updated_Key is valid
            key = pd.read_sql_query(f"SELECT * FROM tbl_ATI_BOT_Owner_Details "
                                    f"WHERE Bot_File_Name = '{bot_file_name}' AND Bot_Version = '{bot_version}'", self.engine)['BOT_Updated_Key'][0]

            if key == updated_key:
                print("Key matched. Proceeding with bot transaction logging...")
                self.log_bot_transaction(bot_file_name, bot_version)
            else:
                print("Please use the updated version or contact the developer.")
                exit()

        except Exception as e:
            print(f"Error during insert and log process: {e}")

    def log_bot_transaction(self, bot_file_name, bot_version):
        try:
            end_time = time.strftime("%b/%d/%Y %H:%M:%S")
            bot_log_data = pd.DataFrame({
                'Bot_File_Name': [bot_file_name],
                'Bot_Type': [bot_version],
                'BoT_StartDateTimeStamp': [self.start_time],
                'BoT_EndDateTimeStamp': [pd.to_datetime(end_time)],
                'No_ofTransaction_Count': [self.config['Transaction_count']],
                'UserPortalID': [self.portal_id],
                'UserName': [self.full_name],
                'ISNTTDomain': [self.domain],
                'Remarks': ["Success"],
                'TransactionDate': [self.today.strftime('%Y-%m-%d')],
                'BoTStatus': ['Completed'],
                'DomainName': [socket.getfqdn(socket.gethostbyname(socket.gethostname())).lower()]
            })

            bot_log_data.to_sql('tbl_ATI_BOT_Log_Capture', con=self.engine, if_exists='append', index=False)
            print("Bot transaction logged successfully.")
        except Exception as e:
            print(f"Error logging bot transaction: {e}")
