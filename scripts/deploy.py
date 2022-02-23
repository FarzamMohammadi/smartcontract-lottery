from brownie import Lottery, network
from helpful_scripts import get_account


def deploy_lottery():
    account = get_account(id="farzam-account")


def main():
    deploy_lottery()
