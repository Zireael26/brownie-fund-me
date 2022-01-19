from brownie import MockV3Aggregator, accounts, config, network
from web3 import Web3

DECIMALS = 18
STARTING_PRICE = 3000


def get_account():
    # account = accounts[0]
    # account = accounts.load("abhishek-account")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print("the active network is: {}".format(network.show_active()))
    if len(MockV3Aggregator) <= 0:
        print("Deploying Mocks...")
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}
        )
        print("Mocks Deployed!")
