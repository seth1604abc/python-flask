import os
import argparse
from app import create_app
from dotenv import load_dotenv
from app.model.db import init_db

parser = argparse.ArgumentParser()
parser.add_argument("-ENV", default="")
args = parser.parse_args()

# 建立flask
app = create_app()

#載入env
dotenv_file = f".env.{args.ENV}"
# print(f"dotenv_file is {dotenv_file}")
if os.path.exists(dotenv_file):
    print(f"Loading Enviroment From {dotenv_file}")
    load_dotenv(dotenv_file)
else:
    print(f"Loading Enviroment From .env")
    load_dotenv()

#初始化mysql
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
init_db(app)

if __name__ == "__main__":
    debug_env = os.getenv("DEBUG")
    debug = debug_env == "True"

    # print(f"port is {os.getenv("SERVER_PORT")}")

    app.run(
        host=os.getenv("SERVER_HOST"),
        port=os.getenv("SERVER_PORT"),
        debug=debug
    )