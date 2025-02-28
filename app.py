import requests
import json

url = "http://127.0.0.1:5000/text-to-speech"  # Replace with your VM's IP if needed
payload = {
    "text": "aap kaise he. humko hyderabad to delhi tak ticket book karna chahiye",
    "voice_name": "Kanika",
    "model": "eleven_turbo_v2"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(payload), headers=headers, stream=True)

if response.status_code == 200:
    content_type = response.headers.get("Content-Type")
    print(f"Content-Type: {content_type}")

    with open("output-law.ulaw", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print("Audio saved to output-law.ulaw")

else:
    print(f"Error: {response.status_code}, {response.text}")