from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import *
from scripts.advanced_collectible.deploy_and_create import *
import pytest


def test_can_create_advanced_collectible():
    skip_unit_test()
    # Act
    advanced_collectible, creation_tx = deploy_and_create()
    requestId = creation_tx.events["requestedCollectible"]["requestId"]
    random_number = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_number, advanced_collectible.address, {"from": get_account()}
    )
    # Assert
    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible.tokenIdToBreed(0) == random_number % 3
