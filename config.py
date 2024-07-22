import os
import base64

OPENIAI_API_KEY = os.environ.get("OPENIAI_API_KEY", "c2stcH**************************************************")
OPENIAI_API_KEY = base64.b64decode(OPENIAI_API_KEY).decode('utf-8')
DB_USER = base64.b64decode(os.environ.get("DB_USER", "ZG********==")).decode('utf-8')
DB_PASSWORD = base64.b64decode(os.environ.get("DB_PASSWORD", "QVZO********************")).decode('utf-8')
DB_HOST = os.environ.get("DB_HOST", "db-*****-****-*****-**-******-*.***.ondigitalocean.com")
DB_PORT = int(os.environ.get("DB_PORT", "24075"))
DATABASE_NAME = os.environ.get("DATABASE_NAME", "maindb")
