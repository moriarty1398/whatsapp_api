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

    def send_whatsapp_reply(self, recipient_number, message_id, reply_content):
        request_body = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient_number,
            "context": {
                "message_id": message_id
            },
            "type": "text",
            "text": {
                "preview_url": False,
                "body": reply_content
            }
        }
        self.send_request(request_body)

# Example usage
if __name__ == '__main__':
    api_endpoint = 'https://graph.facebook.com/v17.0/116655001319676/messages'  # Replace with the actual Meta Cloud API endpoint
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer EAAMJgVQNkgoBAK936MwSkP9G0mkagcuyj8O10H4ZCb0EshQrJxDmPupXo36hdhjLzIgif4htw95RpIM4ZBw5FS71w88Tyraqxn9goOMSfL9NdUipcLa2PHmSAYuWesonGCUZCzcaotdNqyXPRQrR2K3oiqVZAp2Q92LgPsezFZANRORFe9mIWrWx2iBrkjHq78lHBQeNp6D8DRFIeMOq06YEQmZB3KvukZD'  # Replace with the actual user access token
    }

    sender = WhatsAppSender(api_endpoint, headers)

    recipient_number = "917073059101"  # Replace with the recipient's phone number
    message_id = input('previous message ID::')  # Replace with the message ID to which you are replying
    reply_content = "yes of course"  # Replace with the reply message content
    sender.send_whatsapp_reply(recipient_number, message_id, reply_content)