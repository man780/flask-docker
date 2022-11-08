"""Main module"""
from flask import Blueprint, jsonify, request

main_bp = Blueprint('main', __name__)

@main_bp.route('/first', methods=["GET"])
def first():
    """First Endpoint"""
    name = request.args.get("name")
    data = {
        "name": f"Hello {name}"
    }
    return jsonify(data)
