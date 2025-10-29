from flask import Flask
from config import Config
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

app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)

owner_controller = create_owner_controller(mysql)
app.register_blueprint(owner_controller)

household_owner_controller = create_household_owner_controller(mysql)
app.register_blueprint(household_owner_controller)

solar_station_controller = create_solar_station_controller(mysql)
app.register_blueprint(solar_station_controller)

panel_controller = create_panel_controller(mysql)
app.register_blueprint(panel_controller)

battery_controller = create_battery_controller(mysql)
app.register_blueprint(battery_controller)

hourly_production_controller = create_hourly_production_controller(mysql)
app.register_blueprint(hourly_production_controller)

battery_charge_level_controller = create_battery_charge_level_controller(mysql)
app.register_blueprint(battery_charge_level_controller)

panel_tilt_angle_controller = create_panel_tilt_angle_controller(mysql)
app.register_blueprint(panel_tilt_angle_controller)

energy_sales_controller = create_energy_sales_controller(mysql)
app.register_blueprint(energy_sales_controller)

owner_has_station_controller = create_owner_has_station_controller(mysql)
app.register_blueprint(owner_has_station_controller)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1401, debug=True)

