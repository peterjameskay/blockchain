from flask import Flask, request
from blockchain import Blockchain
import json

app =  Flask(__name__)

blockchain = Blockchain()

blockchain.add_new_transaction('$14.34')
blockchain.mine()
blockchain.add_new_transaction('$20.23')
blockchain.mine()
blockchain.add_new_transaction('$100.65')
blockchain.mine()

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})

app.run(debug=True, port=8000)