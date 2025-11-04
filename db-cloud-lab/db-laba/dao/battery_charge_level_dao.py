from models.battery_charge_level import BatteryChargeLevel
import MySQLdb.cursors

class BatteryChargeLevelDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_charge_levels(self):
        cur = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM battery_charge_level")
        charge_levels = cur.fetchall()
        cur.close()
       return [
    BatteryChargeLevel(
        id=row['id'],
        battery_id=row['battery_id'],
        charge_level=row['charge_level'],
        timestamp=row['timestamp']
    )
    for row in charge_levels
]

    def insert_charge_level(self, charge_level):
        cur = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("INSERT INTO battery_charge_level (battery_id, charge_level, timestamp) VALUES (%s, %s, %s)", 
                    (charge_level['battery_id'], charge_level['charge_level'], charge_level['timestamp']))
        self.mysql.connection.commit()
        cur.close()

    def update_charge_level(self, charge_level_id, charge_level):
        cur = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("UPDATE battery_charge_level SET battery_id = %s, charge_level = %s, timestamp = %s WHERE id = %s", 
                    (charge_level['battery_id'], charge_level['charge_level'], charge_level['timestamp'], charge_level_id))
        self.mysql.connection.commit()
        cur.close()

    def delete_charge_level(self, charge_level_id):
        cur = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("DELETE FROM battery_charge_level WHERE id = %s", (charge_level_id,))
        self.mysql.connection.commit()
        cur.close()
