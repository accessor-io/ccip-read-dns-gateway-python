import dns.message, dns.query, dns.rdatatype
from aiohttp import web
import base64
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DNSProver:
    def __init__(self, send_query):
        self.send_query = send_query

    async def query_with_proof(self, qtype, decoded_name):
        return {
            "proofs": [
                {
                    "to_wire": lambda: b'wiredata',
                    "signature": {"data": {"signature": b'signaturedata'}}
                }
            ],
            "answer": {
                "to_wire": lambda: b'answerdata',
                "signature": {"data": {"signature": b'answersig'}}
            }
        }

class ServerInstance:
    def __init__(self, abi):
        self.app = web.Application()
        self.abi = abi
        self.add_routes()

    async def handle_resolve(self, request):
        try:
            data = await request.json()
            name = data['name']
            qtype = data['qtype']
            decoded_name = dns.name.from_text(name)
            result = await prover.query_with_proof(qtype, decoded_name)
            ret = [
                {
                    "rrset": base64.b64encode(entry["to_wire"]()).decode('utf-8'),
                    "sig": {
                        "data": {
                            "signature": base64.b64encode(entry["signature"]["data"]["signature"]).decode('utf-8')
                        }
                    }
                }
                for entry in result["proofs"] + [result["answer"]]
            ]
            return web.json_response(ret)
        except Exception as e:
            return web.json_response({'error': str(e)})

    def add_routes(self):
        self.app.router.add_post('/resolve', self.handle_resolve)

    def run(self):
        aiohttp_host = os.getenv('AIOHTTP_HOST', '0.0.0.0')
        aiohttp_port = int(os.getenv('AIOHTTP_PORT', 8081))
        web.run_app(self.app, host=aiohttp_host, port=aiohttp_port)

if __name__ == "__main__":
    send_query = lambda x: x  # Replace with actual query function
    prover = DNSProver(send_query)
    server_instance = ServerInstance(None)

    print("Server instance created and handler added")
    server_instance.run()
