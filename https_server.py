#!/usr/bin/env python3
"""
HTTPS Server for MindAR Image Tracking
Creates a local HTTPS server with self-signed certificates
"""

import http.server
import ssl
import socketserver
import os
import subprocess
import sys
import socket

PORT = 8443

def get_local_ip():
    """Get the local network IP address"""
    try:
        # Connect to a remote address to determine local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        s.connect(('10.254.254.254', 1))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        try:
            # Fallback: use ifconfig/ipconfig output
            import platform
            if platform.system() == 'Darwin':  # macOS
                result = subprocess.run(['ifconfig'], capture_output=True, text=True)
                for line in result.stdout.split('\n'):
                    if 'inet ' in line and '127.0.0.1' not in line:
                        parts = line.strip().split()
                        for i, part in enumerate(parts):
                            if part == 'inet':
                                return parts[i+1]
            else:  # Linux
                result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
                return result.stdout.split()[0]
        except:
            return 'localhost'

def create_ssl_context(local_ip):
    """Create SSL context with self-signed certificate"""
    cert_file = 'server.pem'
    cert_key_file = 'server.key'
    cert_csr_file = 'server.csr'
    
    # Check if certificate already exists
    if not os.path.exists(cert_file):
        print("Creating self-signed certificate...")
        # Create config file for openssl with SAN (Subject Alternative Names)
        config_content = f"""[req]
distinguished_name = req_distinguished_name
req_extensions = v3_req
prompt = no

[req_distinguished_name]
C = US
ST = State
L = City
O = MindAR
CN = localhost

[v3_req]
keyUsage = keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost
DNS.2 = *.local
IP.1 = 127.0.0.1
IP.2 = {local_ip}
"""
        config_file = 'cert.conf'
        with open(config_file, 'w') as f:
            f.write(config_content)
        
        try:
            # Generate private key
            subprocess.run([
                'openssl', 'genrsa', '-out', cert_key_file, '2048'
            ], check=True, capture_output=True)
            
            # Generate certificate with SAN
            subprocess.run([
                'openssl', 'req', '-new', '-x509', '-key', cert_key_file,
                '-out', cert_file, '-days', '365', '-extensions', 'v3_req',
                '-config', config_file
            ], check=True, capture_output=True)
            
            # Combine key and cert into pem file (for easier use)
            with open(cert_file, 'rb') as cert:
                cert_data = cert.read()
            with open(cert_key_file, 'rb') as key:
                key_data = key.read()
            with open(cert_file, 'wb') as pem:
                pem.write(key_data)
                pem.write(cert_data)
            
            # Clean up
            if os.path.exists(cert_key_file):
                os.remove(cert_key_file)
            if os.path.exists(config_file):
                os.remove(config_file)
            if os.path.exists(cert_csr_file):
                os.remove(cert_csr_file)
                
            print(f"✓ Certificate created: {cert_file}")
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print("❌ Error: openssl not found or certificate creation failed.")
            print(f"   Details: {e}")
            print("\nPlease install openssl:")
            print("  macOS: brew install openssl")
            print("  Linux: sudo apt-get install openssl")
            sys.exit(1)
    
    # Create SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(cert_file)
    return context

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

def main():
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Get local IP address
    local_ip = get_local_ip()
    
    # Create SSL context with local IP
    ssl_context = create_ssl_context(local_ip)
    
    # Create server - bind to all interfaces (0.0.0.0)
    with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPRequestHandler) as httpd:
        httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)
        
        print("=" * 60)
        print("🚀 MindAR HTTPS Server Running!")
        print("=" * 60)
        print(f"📍 Local access: https://localhost:{PORT}")
        print(f"📍 Local access: https://127.0.0.1:{PORT}")
        print(f"📍 Network access: https://{local_ip}:{PORT}")
        print("\n📱 To access from your phone:")
        print(f"   1. Make sure your phone is on the same WiFi network")
        print(f"   2. Open: https://{local_ip}:{PORT}")
        print(f"   3. Accept the security warning (self-signed certificate)")
        print("\n⚠️  Your browser will show a security warning.")
        print("   This is normal for self-signed certificates.")
        print("   Click 'Advanced' → 'Proceed' (or similar)")
        print("\n" + "=" * 60)
        print("Press Ctrl+C to stop the server")
        print("=" * 60 + "\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped.")

if __name__ == '__main__':
    main()
