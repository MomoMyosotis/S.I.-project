
class Config:
    """Base configuration for the Flask client application."""
    
    # Flask settings
    DEBUG = True
    TESTING = False
    SECRET_KEY = "your-secret-key-change-me-in-production"
    
    # Server host and port
    FLASK_HOST = "127.0.0.1"
    FLASK_PORT = 5000
    
    # Session configuration
    SESSION_COOKIE_SECURE = False  # Set to True in production with HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    PERMANENT_SESSION_LIFETIME = 3600  # 1 hour in seconds
    
    # API Server configuration
    API_SERVER_HOST = "127.0.0.1"
    API_SERVER_PORT = 5001
