import urllib3
import argparse
from certsrv import get_ca_cert

def get_root_cert(server,username,password):
    print('Downloading CA cert')

    root_cert = get_ca_cert(server,username,password)

    f = open('root_cert.crt','wb+') #create empty root cert file
    f.write(root_cert)
    f.close()

    print('Done, see root_cert.crt in the current directory')

urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)

parser = argparse.ArgumentParser(
    description="Request root cert from CA")
parser.add_argument('server', help='CA Server FQDN')
parser.add_argument('username', help='CA login name')
parser.add_argument('password', help='CA password')
args = parser.parse_args()

server = args.server
username = args.username
password = args.password

get_root_cert(server,username,password)
