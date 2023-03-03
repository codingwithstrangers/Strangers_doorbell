# from flask import Flask
# from flask_sslify import SSLify

# app = Flask(__name__)
# sslify = SSLify(app)  # This enables HTTPS for all routes

# if __name__ == '__main__':
#     app.run(ssl_context=('path/to/cert.pem', 'path/to/key.pem'))


from OpenSSL import crypto, SSL

# Create a self-signed SSL certificate and private key
def generate_ssl_cert():
    # Generate a key pair
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 2048)

    # Create a self-signed certificate
    cert = crypto.X509()
    cert.get_subject().C = "US"
    cert.get_subject().ST = "New York"
    cert.get_subject().L = "New York"
    cert.get_subject().O = "My Company"
    cert.get_subject().OU = "IT"
    cert.get_subject().CN = "localhost"
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(315360000)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, "sha256")



    print('i am  trying ')
    # Write the certificate and private key to files
    with open("cert.pem", "wb") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    with open("key.pem", "wb") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
        print('i am  trying ')

generate_ssl_cert()