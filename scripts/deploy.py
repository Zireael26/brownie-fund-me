from brownie import FundMe, MockV3Aggregator, accounts, config, network
from scripts.helpful_scripts import get_account
import os


def deploy_fund_me():
    account = get_account()

    # If we are on a persistent network like Rinkeby,use th associated values,
    # else deploy mocks
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print("the active network is: {}".format(network.show_active()))
        print("Deploying Mocks...")
        mock_aggregtor = MockV3Aggregator.deploy(
            18, 3000000000000000000000, {"from": account}
        )
        price_feed_address = mock_aggregtor.address
        print("Mocks Deployed!")

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print("Retrieving version of AggregatorV3Interface")
    aggregatorv3_version = fund_me.getVersion()
    print("Version: " + str(aggregatorv3_version))
    print("Retrieving the current USD Price of ETH")
    usd_exchange_rate = fund_me.getPrice()
    print(type(usd_exchange_rate))
    print("USD Exchange Rate: " + str(usd_exchange_rate))


def main():
    deploy_fund_me()
