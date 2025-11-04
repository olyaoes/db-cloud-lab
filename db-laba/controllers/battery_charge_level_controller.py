from flask import Blueprint, request, jsonify
from services.battery_charge_level_service import BatteryChargeLevelService
from flasgger import swag_from

def create_battery_charge_level_controller(mysql):
    battery_charge_level_controller = Blueprint('battery_charge_level', __name__)
    service = BatteryChargeLevelService(mysql)

    @battery_charge_level_controller.route('/battery_charge_level', methods=['GET'])
    @swag_from({
        'responses': {
            200: {
                'description': 'List of battery charge levels',
                'schema': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'battery_id': {'type': 'integer'},
                            'charge_level': {'type': 'integer'},
                            'timestamp': {'type': 'string', 'format': 'date-time'}
                        }
                    }
                }
            }
        }
    })
    def get_charge_levels():
        charge_levels = service.get_charge_levels()
        return jsonify([charge_level.to_dict() for charge_level in charge_levels])

    @battery_charge_level_controller.route('/battery_charge_level', methods=['POST'])
    @swag_from({
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'battery_id': {'type': 'integer'},
                        'charge_level': {'type': 'integer'},
                        'timestamp': {'type': 'string', 'format': 'date-time'}
                    },
                    'required': ['battery_id', 'charge_level', 'timestamp']
                }
            }
        ],
        'responses': {
            201: {
                'description': 'Charge level created',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string'}
                    }
                }
            }
        }
    })
    def create_charge_level():
        data = request.json
        if not data or 'battery_id' not in data or 'charge_level' not in data or 'timestamp' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_charge_level(data)
            return jsonify({"message": "Charge level created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @battery_charge_level_controller.route('/battery_charge_level/<int:charge_level_id>', methods=['PUT'])
    @swag_from({
        'parameters': [
            {
                'name': 'charge_level_id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'ID of charge level to update'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'battery_id': {'type': 'integer'},
                        'charge_level': {'type': 'integer'},
                        'timestamp': {'type': 'string', 'format': 'date-time'}
                    },
                    'required': ['battery_id', 'charge_level', 'timestamp']
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Charge level updated',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string'}
                    }
                }
            }
        }
    })
    def update_charge_level(charge_level_id):
        data = request.json
        if not data or 'battery_id' not in data or 'charge_level' not in data or 'timestamp' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.modify_charge_level(charge_level_id, data)
            return jsonify({"message": "Charge level updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @battery_charge_level_controller.route('/battery_charge_level/<int:charge_level_id>', methods=['DELETE'])
    @swag_from({
        'parameters': [
            {
                'name': 'charge_level_id',
                'in': 'path',
                'type': 'integer',
                'required': True,
                'description': 'ID of charge level to delete'
            }
        ],
        'responses': {
            200: {
                'description': 'Charge level deleted',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string'}
                    }
                }
            }
        }
    })
    def delete_charge_level(charge_level_id):
        try:
            service.remove_charge_level(charge_level_id)
            return jsonify({"message": "Charge level deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return battery_charge_level_controller
