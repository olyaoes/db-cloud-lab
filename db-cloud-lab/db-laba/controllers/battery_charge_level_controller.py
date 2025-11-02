from flask import Blueprint, request, jsonify
from services.battery_charge_level_service import BatteryChargeLevelService

def create_battery_charge_level_controller(mysql):
    battery_charge_level_controller = Blueprint('battery_charge_level', __name__)
    service = BatteryChargeLevelService(mysql)

    @battery_charge_level_controller.route('/battery_charge_level', methods=['GET'])
    def get_charge_levels():
        """
        Get all battery charge levels
        ---
        responses:
          200:
            description: List of battery charge levels
            schema:
              type: array
              items:
                properties:
                  id:
                    type: integer
                  battery_id:
                    type: integer
                  charge_level:
                    type: number
                  timestamp:
                    type: string
        """
        charge_levels = service.get_charge_levels()
        return jsonify([charge_level.to_dict() for charge_level in charge_levels])

    @battery_charge_level_controller.route('/battery_charge_level', methods=['POST'])
    def create_charge_level():
        """
        Create a new battery charge level
        ---
        parameters:
          - in: body
            name: body
            schema:
              required:
                - battery_id
                - charge_level
                - timestamp
              properties:
                battery_id:
                  type: integer
                charge_level:
                  type: number
                timestamp:
                  type: string
        responses:
          201:
            description: Charge level created
          400:
            description: Invalid input
          500:
            description: Server error
        """
        data = request.json
        if not data or 'battery_id' not in data or 'charge_level' not in data or 'timestamp' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_charge_level(data)
            return jsonify({"message": "Charge level created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @battery_charge_level_controller.route('/battery_charge_level/<int:charge_level_id>', methods=['PUT'])
    def update_charge_level(charge_level_id):
        """
        Update a battery charge level
        ---
        parameters:
          - in: path
            name: charge_level_id
            type: integer
            required: true
          - in: body
            name: body
            schema:
              required:
                - battery_id
                - charge_level
                - timestamp
              properties:
                battery_id:
                  type: integer
                charge_level:
                  type: number
                timestamp:
                  type: string
        responses:
          200:
            description: Charge level updated
          400:
            description: Invalid input
          500:
            description: Server error
        """
        data = request.json
        if not data or 'battery_id' not in data or 'charge_level' not in data or 'timestamp' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.modify_charge_level(charge_level_id, data)
            return jsonify({"message": "Charge level updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @battery_charge_level_controller.route('/battery_charge_level/<int:charge_level_id>', methods=['DELETE'])
    def delete_charge_level(charge_level_id):
        """
        Delete a battery charge level
        ---
        parameters:
          - in: path
            name: charge_level_id
            type: integer
            required: true
        responses:
          200:
            description: Charge level deleted
          500:
            description: Server error
        """
        try:
            service.remove_charge_level(charge_level_id)
            return jsonify({"message": "Charge level deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return battery_charge_level_controller
