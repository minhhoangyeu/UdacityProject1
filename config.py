import os
import urllib.parse

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'hoangnm22'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'fjdNQg/dG8QyGU9NR2MrTtXDJtoeVR95AfklagmiKYtZte9B3Qi2dmZFFGJ6MIiuvDrsYd4Y58K++ASt9GP/Dw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
    BLOB_URL=os.environ.get('BLOB_URL') or 'DefaultEndpointsProtocol=https;AccountName=hoangnm22;AccountKey=fjdNQg/dG8QyGU9NR2MrTtXDJtoeVR95AfklagmiKYtZte9B3Qi2dmZFFGJ6MIiuvDrsYd4Y58K++ASt9GP/Dw==;EndpointSuffix=core.windows.net'
    
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'hoangnm22project1.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'CMSProject1'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'hoangnm22'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Minhhoang123#'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    
    #SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect={}".format(
        urllib.parse.quote_plus(
            "DRIVER={ODBC Driver 17 for SQL Server};"+"SERVER={};DATABASE={};UID={};PWD={};".format(SQL_SERVER, SQL_DATABASE, SQL_USER_NAME, SQL_PASSWORD)
        )
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "UtW8Q~O4qu~E9CAUbvsWHGh49FkwlHBDZeDAVcY0"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/2065faea-016c-40f4-9ddc-51bf72c388f1"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "5c25c497-c03f-4d7a-bcdb-043826f2db67"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
