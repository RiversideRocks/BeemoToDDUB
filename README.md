# BeemoToDDUB
Its never been easier to transfer Beemo reports to DDUB

## Installation

Clone the repo and install Python packages.

```
pip3 install -r requirements.txt
```

Sign into [discod.riverside.rocks](https://discord.riverside.rocks) and grab your token (it should be on the bottom of the dashboard). Paste that in the .env file. For example, if your token was `abc123`, you would add the following to your .env file:

```
key="abc123"
```

Once you are done setting up, run the following command and follow the prompts.

```
python3 import.py
```
