from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"\n~Output~\n[+] Minimum fee: {entrance_fee}")
    print("[+] Funding now...")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    print("[+] Withdrawing now...")
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
