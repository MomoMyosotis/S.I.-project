# first line

from flask_mail import Mail, Message
from typing import Optional, Dict, Any
import secrets
from datetime import datetime, timedelta

# Global Mail instance
mail: Optional[Mail] = None

# Password reset tokens storage (in-memory with expiration)
# Format: {token: {"email": email, "expires_at": datetime}}
reset_tokens: Dict[str, Dict[str, Any]] = {}

# Default password for reset
DEFAULT_RESET_PASSWORD = "TempPassword123!"

def init_mail(app):
    """Initialize Flask-Mail with the given Flask app."""
    global mail
    mail = Mail(app)
    #print("[DEBUG][email_service] Flask-Mail initialized successfully")

def generate_reset_token(email: str, token_expiry_hours: int = 24) -> str:
    """
    Generate a password reset token for the given email.
    Token expires after token_expiry_hours.
    Returns the generated token.
    """
    token = secrets.token_urlsafe(32)
    expires_at = datetime.utcnow() + timedelta(hours=token_expiry_hours)
    reset_tokens[token] = {
        "email": email,
        "expires_at": expires_at
    }
    #print(f"[DEBUG][email_service] Generated reset token for {email}, expires at {expires_at}")
    return token

def validate_reset_token(token: str) -> Optional[str]:
    """
    Validate a reset token and return the associated email if valid.
    Returns None if token is invalid or expired.
    """
    if token not in reset_tokens:
        #print(f"[DEBUG][email_service] Invalid token: {token}")
        return None
    
    token_data = reset_tokens[token]
    expires_at = token_data.get("expires_at")
    
    if expires_at < datetime.utcnow():
        # Token expired, remove it
        del reset_tokens[token]
        #print(f"[DEBUG][email_service] Token expired: {token}")
        return None
    
    email = token_data.get("email")
    #print(f"[DEBUG][email_service] Token validated for {email}")
    return email

def consume_reset_token(token: str) -> Optional[str]:
    """
    Validate and consume a reset token (removes it after use).
    Returns the associated email if valid, None otherwise.
    """
    email = validate_reset_token(token)
    if email and token in reset_tokens:
        del reset_tokens[token]
        #print(f"[DEBUG][email_service] Token consumed for {email}")
    return email

def send_recovery_email(recipient_email: str, username: str, reset_link_base: str = "http://127.0.0.1:5000") -> Dict[str, Any]:
    """
    Send a password recovery email to the user.
    Generates a recovery token and sends it via email.
    """
    if mail is None:
        return {"status": "ERROR", "error_msg": "Mail service not initialized"}
    
    try:
        # Generate and store a password reset token
        recovery_token = generate_reset_token(recipient_email)
        reset_link = f"{reset_link_base}/auth/reset?token={recovery_token}"
        
        # Create email message
        subject = "Password Recovery Request"
        body = f"""
Hello {username},

We received a request to recover your password. If you didn't make this request, please ignore this email.

To reset your password, click the link below:
{reset_link}

This link will expire in 24 hours.

If you have any questions, please contact our support team.

Best regards,
The Support Team
"""
        
        msg = Message(
            subject=subject,
            recipients=[recipient_email],
            body=body,
            html=generate_recovery_html(username, recovery_token, reset_link)
        )
        
        # Send the email
        mail.send(msg)
        
        #print(f"[DEBUG][email_service.send_recovery_email] Recovery email sent to {recipient_email}")
        return {
            "status": "OK",
            "error_msg": None,
            "message": f"Recovery email sent to {recipient_email}"
        }
    
    except Exception as e:
        #print(f"[ERROR][email_service.send_recovery_email] Failed to send email: {str(e)}")
        return {
            "status": "ERROR",
            "error_msg": f"Failed to send recovery email: {str(e)}"
        }

def send_assistance_email(user_email: str, username: str, message: str, admin_email: Optional[str] = None) -> Dict[str, Any]:
    """
    Send an assistance request email.
    Notifies the user and optionally an admin about the assistance request.
    """
    if mail is None:
        return {"status": "ERROR", "error_msg": "Mail service not initialized"}
    
    try:
        # Send confirmation email to user
        user_subject = "Assistance Request Received"
        user_body = f"""
Hello {username},

Thank you for contacting us. We have received your assistance request and will get back to you as soon as possible.

Your message:
"{message}"

Support team will review your request and respond within 24-48 hours.

Best regards,
The Support Team
"""
        
        user_msg = Message(
            subject=user_subject,
            recipients=[user_email],
            body=user_body,
            html=generate_assistance_user_html(username, message)
        )
        
        mail.send(user_msg)
        
        # Optional: Send notification to admin
        if admin_email:
            admin_subject = f"New Assistance Request from {username}"
            admin_body = f"""
New assistance request received.

User: {username}
Email: {user_email}
Message: {message}

Please review and respond to the user as soon as possible.
"""
            
            admin_msg = Message(
                subject=admin_subject,
                recipients=[admin_email],
                body=admin_body,
                html=generate_assistance_admin_html(username, user_email, message)
            )
            
            mail.send(admin_msg)
        
        #print(f"[DEBUG][email_service.send_assistance_email] Assistance email sent to {user_email}")
        return {
            "status": "OK",
            "error_msg": None,
            "message": f"Assistance request received. Confirmation sent to {user_email}"
        }
    
    except Exception as e:
        #print(f"[ERROR][email_service.send_assistance_email] Failed to send email: {str(e)}")
        return {
            "status": "ERROR",
            "error_msg": f"Failed to send assistance email: {str(e)}"
        }

# =====================
# HTML EMAIL TEMPLATES
# =====================

def generate_recovery_html(username: str, recovery_token: str, reset_link: str) -> str:
    """Generate HTML email template for password recovery."""
    return f"""
    <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
                .header {{ background-color: #007bff; color: white; padding: 20px; text-align: center; border-radius: 5px 5px 0 0; }}
                .content {{ padding: 20px; }}
                .button {{ display: inline-block; padding: 12px 30px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px; margin: 20px 0; font-weight: bold; }}
                .button:hover {{ background-color: #0056b3; }}
                .footer {{ text-align: center; font-size: 12px; color: #666; margin-top: 20px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Password Recovery</h1>
                </div>
                <div class="content">
                    <p>Hello {username},</p>
                    <p>We received a request to recover your password. If you didn't make this request, please ignore this email.</p>
                    <p>Click the button below to reset your password:</p>
                    <center>
                        <a href="{reset_link}" class="button">Reset Password</a>
                    </center>
                    <p><small>Or copy and paste this link in your browser: {reset_link}</small></p>
                    <p>This link will expire in 24 hours.</p>
                    <p>If you have any questions, please contact our support team.</p>
                </div>
                <div class="footer">
                    <p>&copy; 2026 Support Team. All rights reserved.</p>
                </div>
            </div>
        </body>
    </html>
    """

def generate_assistance_user_html(username: str, message: str) -> str:
    """Generate HTML email template for user assistance confirmation."""
    return f"""
    <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
                .header {{ background-color: #28a745; color: white; padding: 20px; text-align: center; border-radius: 5px 5px 0 0; }}
                .content {{ padding: 20px; }}
                .message-box {{ background-color: #f8f9fa; padding: 15px; border-left: 4px solid #007bff; margin: 20px 0; }}
                .footer {{ text-align: center; font-size: 12px; color: #666; margin-top: 20px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Assistance Request Received</h1>
                </div>
                <div class="content">
                    <p>Hello {username},</p>
                    <p>Thank you for contacting us. We have received your assistance request and will get back to you as soon as possible.</p>
                    <div class="message-box">
                        <strong>Your message:</strong>
                        <p>{message}</p>
                    </div>
                    <p>Our support team will review your request and respond within 24-48 hours.</p>
                </div>
                <div class="footer">
                    <p>&copy; 2026 Support Team. All rights reserved.</p>
                </div>
            </div>
        </body>
    </html>
    """

def generate_assistance_admin_html(username: str, user_email: str, message: str) -> str:
    """Generate HTML email template for admin assistance notification."""
    return f"""
    <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
                .header {{ background-color: #dc3545; color: white; padding: 20px; text-align: center; border-radius: 5px 5px 0 0; }}
                .content {{ padding: 20px; }}
                .detail-box {{ background-color: #f8f9fa; padding: 15px; border-left: 4px solid #dc3545; margin: 20px 0; }}
                .footer {{ text-align: center; font-size: 12px; color: #666; margin-top: 20px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>New Assistance Request</h1>
                </div>
                <div class="content">
                    <p><strong>New assistance request received.</strong></p>
                    <div class="detail-box">
                        <p><strong>User:</strong> {username}</p>
                        <p><strong>Email:</strong> {user_email}</p>
                        <p><strong>Message:</strong><br/>{message}</p>
                    </div>
                    <p>Please review and respond to the user as soon as possible.</p>
                </div>
                <div class="footer">
                    <p>&copy; 2026 Support Team. All rights reserved.</p>
                </div>
            </div>
        </body>
    </html>
    """

# last line
