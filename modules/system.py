"""System module"""
from flask import Blueprint, jsonify

system_bp = Blueprint('system', __name__)

@system_bp.route('/')
@system_bp.route('/health_check')
def health_check():
    """Health Check"""
    return jsonify(success=True)
