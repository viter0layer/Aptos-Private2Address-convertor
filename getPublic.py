from aptos_sdk.account import Account

keys_list = []
with open("privates.txt", "r") as f:
    keys_list = [row.strip() for row in f if row.strip()]

with open("aptos_addresses.txt", "a", encoding='utf-8') as f:
    for i, private_key in enumerate(keys_list, start=1):
        current_account = Account.load_key(key=private_key)
        ad = current_account.address()
        print(ad)
        f.write(str(ad) + "\n")
