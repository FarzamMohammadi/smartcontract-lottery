from brownie import Lottery
from helpful_scripts import get_account, get_contract


def deploy_lottery():
    account = get_account(id="farzam-account")
    lottery = Lottery.Deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator"),
        {"from": account},
    )


def main():
    deploy_lottery()
