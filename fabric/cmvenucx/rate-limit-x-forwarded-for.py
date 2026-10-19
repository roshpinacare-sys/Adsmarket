import re
from functools import wraps
from flask import request, jsonify, g
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from ipaddress import ip_address, ip_network, AddressValueError, Networ

# Configuration for allowed internal networks
INTERNAL_NETWORKS = [
    ip_network('10.0.0.0/8'),
    ip_network('172.16.0.0/12'),
    ip_network('192.168.0.0/16'),
    ip_network('127.0.0.0/8')
]

# Session store (in production, use Redis or similar)
session_store = {}

def is_internal_ip(ip):
    """Check if an IP address is in the allowed internal networks."""
    try:
        ip_obj = ip_address(ip)
        return any(ip_obj in network for network in INTERNAL_NETWORKS)
    except AddressValueError:
        return False

def get_real_ip():
    """Get the real IP address, checking for spoofed X-Forwarded-For."""
    real_ip = get_remote_address()
    
    # Check if request claims to be internal but IP is not internal
    forwarded_for = request.headers.get('X-Forwarded-For')
    if forwarded_for:
        # If X-Forwarded-For is present, check if it's spoofing an internal IP
        for ip in forwarded_for.split(','):
            ip = ip.strip()
            if is_internal_ip(ip) and not is_internal_ip(real_ip):
                # Log the attempt (in production, use proper logging)
                print(f"Potential IP spoofing attempt: Real IP {real_ip} claiming internal IP {ip}")
                return real_ip
    
    return real_ip

def create_limiter(app):
    """Create and configure the rate limiter."""
    limiter = Limiter(
        app,
        key_func=get_real_ip,
        default_limits=["200 per day", "50 per hour"]
    )
    return limiter

def internal_rate_limit(limit):
    """Decorator for rate limiting internal requests."""
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            real_ip = get_real_ip()
            
            # Apply session-based rate limiting for internal requests
            if is_internal_ip(real_ip):
                session_id = request.headers.get('X-Session-ID') or real_ip
                
                if session_id not in session_store:
                    session_store[session_id] = {
                        'requests': 0,
                        'window_start': time.time()
                    }
                
                session_data = session_store[session_id]
                
                # Reset window if needed
                if time.time() - session_data['window_start'] > 3600:  # 1 hour window
                    session_data['requests'] = 0
                    session_data['window_start'] = time.time()
                
                # Check if limit exceeded
                if session_data['requests'] >= limit:
                    return jsonify({"error": "Rate limit exceeded for internal requests"}), 429
                
                # Increment request count
                session_data['requests'] += 1
            
            return f(*args, **kwargs)
        return wrapped
    return decorator

def validate_ip_header(f):
    """Decorator to validate IP headers and prevent spoofing."""
    @wraps(f)
    def wrapped(*args, **kwargs):
        real_ip = get_real_ip()
        
        # Check for spoofing attempts
        forwarded_for = request.headers.get('X-Forwarded-For')
        if forwarded_for:
            for ip in forwarded_for.split(','):
                ip = ip.strip()
                if is_internal_ip(ip) and not is_internal_ip(real_ip):
                    return jsonify({"error": "IP spoofing detected"}), 403
        
        return f(*args, **kwargs)
    return wrapped

# Example usage in Flask app
# from flask import Flask
# app = Flask(__name__)
# limiter = create_limiter(app)
# 
# @app.route('/api/internal')
# @limiter.limit("10 per minute")
# @internal_rate_limit(100)  # 100 requests per hour for internal
# @validate_ip_header
# def internal_api():
#     return jsonify({"message": "Internal API response"})
# 
# @app.route('/api/public')
# @limiter.limit("5 per minute")
# @validate_ip_header
# def public_api():
#     return jsonify({"message": "Public API response"})