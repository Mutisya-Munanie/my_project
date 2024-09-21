import africastalking
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()  # Reads the .env file

class AfricaTalking:
    def __init__(self):
        self.username = env('AFRICASTALKING_USERNAME')
        self.api_key = env('AFRICASTALKING_API_KEY')
        self.initialize()

    def initialize(self):
        """
        Initialize Africa's Talking SDK with credentials from environment variables.
        """
        africastalking.initialize(username=self.username, api_key=self.api_key)

    def send_sms(self, phone_number, message):
        """
        Send an SMS to a specified phone number.
        """
        try:
            response = africastalking.SMS.send(message, [phone_number])
            print("SMS sent:", response)
            return response
        except Exception as e:
            print("Failed to send SMS:", e)
            return None

# Create a singleton instance for sending SMS
africa_talking_instance = AfricaTalking()




