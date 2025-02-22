import json
import random
from web3 import Web3
from colorama import Fore, Style, init

# Initialize colorama
init()

# Configuration
PRIVATE_KEY = "PRIVATEKEYADDRESSHERE"
RPC_URL = "https://rpc.nexus.xyz/http"
CHAIN_ID = 392

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(RPC_URL))
wallet_address = web3.eth.account.from_key(PRIVATE_KEY).address

def get_addresses():
    with open("addresses.txt", "r") as file:
        return [line.strip() for line in file if line.strip()]

def transfer_nex(to_address, amount_wei):
    nonce = web3.eth.get_transaction_count(wallet_address)
    
    fee_data = web3.eth.gas_price
    max_fee_per_gas = fee_data + Web3.to_wei(0.5, 'gwei')
    max_priority_fee_per_gas = Web3.to_wei(1, 'gwei')
    
    estimated_gas_limit = web3.eth.estimate_gas({
        'to': to_address,
        'value': amount_wei,
        'from': wallet_address
    })
    
    tx = {
        'nonce': nonce,
        'to': to_address,
        'value': amount_wei,
        'gas': estimated_gas_limit,
        'maxFeePerGas': max_fee_per_gas,
        'maxPriorityFeePerGas': max_priority_fee_per_gas,
        'chainId': CHAIN_ID,
        'type': 2
    }
    
    signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(f"{Fore.CYAN}Transaction sent! Hash: {tx_hash.hex()}{Style.RESET_ALL}")
    
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"{Fore.GREEN}Transaction confirmed in block: {receipt.blockNumber}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Gas Used: {receipt.gasUsed}{Style.RESET_ALL}")

def main():
    addresses = get_addresses()
    print(f"{Fore.BLUE}Found {len(addresses)} recipient addresses.{Style.RESET_ALL}")
    
    min_amount = float(input("Enter the minimum amount of NEX to send: "))
    max_amount = float(input("Enter the maximum amount of NEX to send: "))
    loops = int(input("Enter the number of loops: "))
    
    for loop in range(loops):
        print(f"\n{Fore.MAGENTA}INFO: Loop {loop + 1}/{loops}{Style.RESET_ALL}")
        for to_address in addresses:
            masked_address = to_address[:5] + "****" + to_address[-4:]
            amount_wei = Web3.to_wei(random.uniform(min_amount, max_amount), 'ether')
            print(f"{Fore.CYAN}INFO: Sending {amount_wei / 1e18:.8f} NEX to {masked_address}{Style.RESET_ALL}")
            transfer_nex(to_address, amount_wei)
    
    print(f"{Fore.GREEN}All transactions completed!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
