"""Main module"""
import requests

from flask import Blueprint, jsonify, request

main_bp = Blueprint("main", __name__)

@main_bp.route("/first", methods=["GET"])
def first():
    """First Endpoint"""
    name = request.args.get("name")
    data = {
        "name": f"Hello {name}"
    }
    return jsonify(data)

@main_bp.route("/parse_data", methods=["GET"])
def parse_data():
    """Parse data from API"""
    headers = {
        "apikey": "b0530240-68f3-11ed-833f-6d356bd82086"
    }

    params = (
        ("continent","Europe"),
    )

    response = requests.get(
        'https://app.sportdataapi.com/api/v1/soccer/countries',
        headers=headers,
        params=params
    )

    data = {
        "data": response.json()
    }

    return jsonify(data)
