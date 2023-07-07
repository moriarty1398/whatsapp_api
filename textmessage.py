import requests

class MetaCloudAPI:
    def __init__(self, api_endpoint, headers):
        self.api_endpoint = api_endpoint
        self.headers = headers

    def send_request(self, request_body):
        try:
            response = requests.post(self.api_endpoint, headers=self.headers, json=request_body)
            response.raise_for_status()
            print("WhatsApp message sent successfully!")
        except requests.exceptions.RequestException as e:
            print("Failed to send the WhatsApp message:", e)

class WhatsAppSender(MetaCloudAPI):
    def __init__(self, api_endpoint, headers):
        super().__init__(api_endpoint, headers)

    def send_whatsapp_message(self, recipient_number, message_content):
        request_body = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient_number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": message_content
            }
        }
        self.send_request(request_body)

# Example usage
if __name__ == '__main__':
    import config

    api_endpoint = config.api_endpoint
    headers = config.headers

    sender = WhatsAppSender(api_endpoint, headers)

    recipient_number = config.recipient_number
    message_content = input('enter your message here::')  # Replace with the desired text message content
    sender.send_whatsapp_message(recipient_number, message_content)

