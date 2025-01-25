import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Literal

from xhm_config import conf
from xhm_log import info, error


class EmailError(Exception):
    """Base class for email-related errors"""
    pass


class RateLimitError(EmailError):
    """Raised when rate limit is exceeded"""
    pass


class SMTPConfigError(EmailError):
    """Raised when SMTP configuration is invalid"""
    pass


class EmailSender:
    # Enhanced email templates with modern design
    EMAIL_TEMPLATES = {
        'en': {
            'subject': 'Your Verification Code',
            'title': 'Verification Code',
            'greeting': 'Hi',
            'code_intro': 'Please use the following code to verify your account:',
            'validity': 'This code will expire in 5 minutes.',
            'warning': 'If you did not request this code, please ignore this email.',
            'security_note': 'For your security, never share this code with anyone.',
            'team': 'askkf.com',
            'footer': 'This is an automated message, please do not reply.'
        },
        'zh': {
            'subject': '您的验证码',
            'title': '验证码',
            'greeting': '您好',
            'code_intro': '请使用以下验证码验证您的账户：',
            'validity': '验证码将在5分钟后过期。',
            'warning': '如果您没有请求此验证码，请忽略此邮件。',
            'security_note': '为了您的账户安全，请勿将验证码分享给他人。',
            'team': 'askkf.com',
            'footer': '这是一封自动发送的邮件，请勿回复。'
        }
    }

    def __init__(self):
        """
        Initialize Gmail sender with rate limiting

        Args:
            gmail_address: Your Gmail address
            app_password: Google App Password
            rate_limit_attempts: Maximum attempts per time window
            rate_limit_window: Time window in seconds
        """
        self.sender_address = conf.get("xhm_smtp.sender_address")
        self.app_password = conf.get("xhm_smtp.sender_password")
        self.smtp_host = conf.get("xhm_smtp.host")
        self.ssl_port = conf.get("xhm_smtp.ssl_port")
        self.port = conf.get("xhm_smtp.port")

    def _get_html_template(self, username: str, code: str, lang: str) -> str:
        """Generate HTML email template with modern design"""
        template = self.EMAIL_TEMPLATES[lang]

        html = f"""
        <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body style="margin: 0; padding: 0; font-family: Arial, 'Helvetica Neue', sans-serif;">
                <div style="max-width: 600px; margin: 0 auto; padding: 40px 20px; background-color: #ffffff;">
                    <div style="text-align: center; margin-bottom: 30px;">
                        <h1 style="color: #333333; font-size: 24px; margin: 0;">{template['title']}</h1>
                    </div>

                    <div style="background-color: #f8f9fa; border-radius: 12px; padding: 30px; margin-bottom: 30px;">
                        <p style="margin: 0 0 20px 0; color: #666666;">{template['greeting']} {username},</p>
                        <p style="margin: 0 0 20px 0; color: #666666;">{template['code_intro']}</p>

                        <div style="
                            background-color: #ffffff;
                            padding: 20px;
                            margin: 20px 0;
                            font-size: 32px;
                            font-weight: bold;
                            text-align: center;
                            letter-spacing: 8px;
                            border-radius: 8px;
                            border: 2px solid #e9ecef;
                            color: #333333;">
                            {code}
                        </div>

                        <p style="margin: 0; color: #666666;">{template['validity']}</p>
                    </div>

                    <div style="margin-bottom: 30px;">
                        <p style="margin: 0 0 10px 0; color: #dc3545; font-size: 14px;">
                            ⚠️ {template['security_note']}
                        </p>
                        <p style="margin: 0; color: #666666; font-size: 14px;">
                            ℹ️ {template['warning']}
                        </p>
                    </div>

                    <div style="border-top: 1px solid #e9ecef; padding-top: 20px; text-align: center;">
                        <p style="margin: 0 0 10px 0; color: #666666; font-size:14px;">{template['team']}</p>
                        <p style="margin: 0; color: #999999; font-size: 12px;">{template['footer']}</p>
                    </div>
                </div>
            </body>
        </html>
        """
        return html

    def send_code(self, to_email: str, username: str, code: str, lang: Literal['en', 'zh'] = 'en') -> bool:
        """
        Generate and send verification code with rate limiting

        Args:
            to_email: Recipient's email address
            username: Username
            code:code
            lang: Email language ('en' for English, 'zh' for Chinese)

        Returns:
            tuple: (success: bool, code: str | None)

        Raises:
            RateLimitError: When rate limit is exceeded
            SMTPConfigError: When SMTP configuration is invalid
            EmailError: For other email-related errors
        """

        try:
            message = MIMEMultipart()
            message['From'] = f"AskKF Security Team <{self.sender_address}>"
            message['To'] = to_email
            message['Subject'] = Header(self.EMAIL_TEMPLATES[lang]['subject'])

            html_content = self._get_html_template(username, code, lang)
            message.attach(MIMEText(html_content, 'html', 'utf-8'))

            try:
                smtp_client = smtplib.SMTP_SSL(self.smtp_host, self.ssl_port)
                info('smtp_ssl----连接服务器成功，现在开始检查账号密码')
            except Exception as e1:
                smtp_client = smtplib.SMTP(self.smtp_host, self.port, timeout=5)
                error('smtp----连接服务器成功，现在开始检查账号密码')
            except Exception as e2:
                error('抱歉，连接服务超时')
                return False
            smtp_client.login(self.sender_address, self.app_password)
            smtp_client.send_message(message)

            info(f"Successfully sent verification code to {to_email}")
            return True

        except smtplib.SMTPAuthenticationError as e:
            error("authentication failed")
            raise SMTPConfigError("authentication failed. Please check your app password.") from e
        except smtplib.SMTPException as e:
            error(f"SMTP error occurred: {str(e)}")
            raise EmailError(f"Failed to send email: {str(e)}") from e
        except Exception as e:
            error(f"Unexpected error: {str(e)}")
            raise EmailError(f"Unexpected error occurred: {str(e)}") from e


emailer = EmailSender()
