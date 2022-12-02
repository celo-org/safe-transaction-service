from gnosis.eth.ethereum_client import EthereumNetwork

CRYPTO_KITTIES_CONTRACT_ADDRESSES = {
    "0x06012c8cf97BEaD5deAe237070F9587f8E7A266d",  # Mainnet
    "0x16baF0dE678E52367adC69fD067E5eDd1D33e3bF",  # Rinkeby
}

ENS_CONTRACTS_WITH_TLD = {
    "0x57f1887a8BF19b14fC0dF6Fd9B2acc9Af147eA85": "eth",  # ENS .eth registrar (Every network)
}


CELO_NETWORKS = (
    EthereumNetwork.CELO,
    EthereumNetwork.CELO_ALFAJORES,
    EthereumNetwork.CELO_BAKLAVA,
)
