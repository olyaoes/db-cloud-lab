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
                'examples': {
                    'application/json': [
                        {
                            'id': 1,
                            'battery_id': 2,
                            'charge_level': 85,
                            'timestamp': '2025-10-01T12:00:00'
                        }
                    ]
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
                    'example': {
                        'battery_id': 1,
                        'charge_level': 75,
                        'timestamp': '2025-11-01T08:30:00'
                    }
                }
            }
        ],
        'responses': {
            201: {
                'description': 'Charge level created',
                'examples': {
                    'application/json': {
                        'message': 'Charge level created'
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
                    'example': {
                        'battery_id': 1,
                        'charge_level': 80,
                        'timestamp': '2025-11-02T09:00:00'
                    }
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Charge level updated',
                'examples': {
                    'application/json': {
                        'message': 'Charge level updated'
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
                'examples': {
                    'application/json': {
                        'message': 'Charge level deleted'
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
