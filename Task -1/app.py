from flask import Flask, render_template, request, jsonify, send_file
import socket
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    
    print(f"Contact Form Submission:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")
    
    return jsonify({'status': 'success', 'message': 'Thank you for your message!'})

@app.route('/download-cv')
def download_cv():
    resume_path = os.path.join(os.path.dirname(__file__), 'Arjun_Tomar_Resume.pdf')
    
    if os.path.exists(resume_path):
        return send_file(resume_path, as_attachment=True, download_name='Arjun_Tomar_Resume.pdf')
    else:
        return jsonify({'error': 'Resume not found'}), 404

def get_local_ip():
    """Get the local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1"

if __name__ == '__main__':
    local_ip = get_local_ip()
    port = 5000
    
    print("\n" + "="*50)
    print("🚀 Flask Server Starting...")
    print("="*50)
    print(f"📍 Local Access: http://localhost:{port}")
    print(f"🌐 Network Access: http://{local_ip}:{port}")
    print("="*50 + "\n")
    
    app.run(host='0.0.0.0', port=port, debug=True)