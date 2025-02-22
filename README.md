# NEX Transfer Script  

A Python script to automate the transfer of NEX tokens to multiple recipient addresses. The script reads addresses from `addresses.txt`, selects a random amount within a user-specified range, and executes blockchain transactions with logging and confirmations.

---

## 📋 Features

- Sends NEX tokens to multiple addresses from `addresses.txt`  
- Allows users to specify a random range for transfer amounts  
- Automatically estimates gas fees for optimal transactions  
- Displays transaction details, including block confirmations 
- User-friendly console output with color indicators   

---

## Installation  

### 1. Clone the Repository  
```bash
git clone https://github.com/kelliark/Nexus-AutoTx.git
cd Nexus-AutoTx
```

### 2. Install Dependencies  
Install the required Python packages:  
```bash
pip install -r requirements.txt
```

## Configuration  

### **1. Set Up Your Environment**  
Before running the script, configure your private key in line *10*

```bash
PRIVATE_KEY = "PRIVATEKEYADDRESSHERE"
```

### **2. Prepare `addresses.txt`**  
Add recipient addresses (one per line) in `addresses.txt`:  
```
0xRecipientAddress1
0xRecipientAddress2
0xRecipientAddress3
```

## Usage  

Run the script with:  
```bash
python main.py
```

You will be prompted to:  
1. Enter the **minimum and maximum** NEX amount for transfers  
2. Specify the **number of loops**  

## Example Output  

```
INFO: Found 5 recipient addresses.
Enter minimum amount: 0.00004
Enter maximum amount: 0.00005
Enter the number of loops: 3

INFO: Loop 1/3
INFO: Sending 0.00004250 NEX to 0x1ED****BaB3
Transaction sent! Hash: 0xabc123...
Transaction confirmed in block: 12345678
Gas Used: 21000
```


## License  
This project is released under the MIT License.

## Disclaimer  
This script directly interacts with your wallet. **Use at your own risk** and never share your private key with anyone.
