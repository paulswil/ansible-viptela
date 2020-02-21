import urllib3
import argparse
from certsrv import get_cert


def gen_cert(csr, server, template, username, password):
    print('Starting cert request')

    f = open(csr,'r') #open csr file
    request = f.read()
    f.close()

    cert_response = get_cert(server, request, template, username, password)

    f1 = open('newcert.crt','wb+') #create empty certificate file
    f1.write(cert_response)
    f1.close()

    print('Done, see newcert.crt in the current directory')


urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)

parser = argparse.ArgumentParser(
    description="Submit CSR to CA for signing")
parser.add_argument('server', help='CA Server FQDN')
parser.add_argument('username', help='CA login name')
parser.add_argument('password', help='CA password')
parser.add_argument('template', help='Certificate Template')
parser.add_argument('csr', help='/path/to/CSR/file')
args = parser.parse_args()

server = args.server
username = args.username
password = args.password
template = args.template
csr = args.csr 

    

gen_cert(csr, server, template, username, password)

