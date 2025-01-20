import os
import argparse
from app import create_app

from config.config_manager import get_config

parser = argparse.ArgumentParser()
parser.add_argument("-ENV", default="development")
args = parser.parse_args()

os.environ["ENV"] = args.ENV

app = create_app()
app.config.from_object(get_config())

if __name__ == "__main__":
    port = app.config["SERVER_PORT"]
    # print(f"Server is running at port {port}")
    app.run(
        host=app.config["SERVER_HOST"],
        port=port,
        debug=app.config["DEBUG"]
    )