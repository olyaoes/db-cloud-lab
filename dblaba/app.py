from flask import Flask
from config import Config

# Controllers
from controllers.owner_controller import create_owner_controller
from controllers.household_owner_controller import create_household_owner_controller
from controllers.solar_station_controller import create_solar_station_controller
from controllers.panel_controller import create_panel_controller
from controllers.battery_controller import create_battery_controller
from controllers.hourly_production_controller import create_hourly_production_controller
from controllers.battery_charge_level_controller import create_battery_charge_level_controller
from controllers.panel_tilt_angle_controller import create_panel_tilt_angle_controller
from controllers.energy_sales_controller import create_energy_sales_controller
from controllers.owner_has_station_controller import create_owner_has_station_controller

from flask_mysqldb import MySQL
from flasgger import Swagger

# Create app
app = Flask(__name__)
swagger = Swagger(app)

# Load config
app.config.from_object(Config)

# Init MySQL
mysql = MySQL(app)

# Register controllers
app.register_blueprint(create_owner_controller(mysql))
app.register_blueprint(create_household_owner_controller(mysql))
app.register_blueprint(create_solar_station_controller(mysql))
app.register_blueprint(create_panel_controller(mysql))
app.register_blueprint(create_battery_controller(mysql))
app.register_blueprint(create_hourly_production_controller(mysql))
app.register_blueprint(create_battery_charge_level_controller(mysql))
app.register_blueprint(create_panel_tilt_angle_controller(mysql))
app.register_blueprint(create_energy_sales_controller(mysql))
app.register_blueprint(create_owner_has_station_controller(mysql))


# Health check
@app.route("/")
def index():
    return "API is running", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1401)
