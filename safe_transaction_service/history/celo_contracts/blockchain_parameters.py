import json

blockchain_parameters_proxy_address = "0x6E10a8864C65434A721d82e424d727326F9d5Bfa"
blockchain_parameters_abi = json.loads(
    '[{"type":"constructor","stateMutability":"nonpayable","payable":false,"inputs":[{"type":"bool","name":"test","internalType":"bool"}]},{"type":"event","name":"BlockGasLimitSet","inputs":[{"type":"uint256","name":"limit","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"IntrinsicGasForAlternativeFeeCurrencySet","inputs":[{"type":"uint256","name":"gas","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"MinimumClientVersionSet","inputs":[{"type":"uint256","name":"major","internalType":"uint256","indexed":false},{"type":"uint256","name":"minor","internalType":"uint256","indexed":false},{"type":"uint256","name":"patch","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"OwnershipTransferred","inputs":[{"type":"address","name":"previousOwner","internalType":"address","indexed":true},{"type":"address","name":"newOwner","internalType":"address","indexed":true}],"anonymous":false},{"type":"event","name":"UptimeLookbackWindowSet","inputs":[{"type":"uint256","name":"window","internalType":"uint256","indexed":false},{"type":"uint256","name":"activationEpoch","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"blockGasLimit","inputs":[],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"checkProofOfPossession","inputs":[{"type":"address","name":"sender","internalType":"address"},{"type":"bytes","name":"blsKey","internalType":"bytes"},{"type":"bytes","name":"blsPop","internalType":"bytes"}],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"uint256","name":"","internalType":"uint256"},{"type":"uint256","name":"","internalType":"uint256"}],"name":"fractionMulExp","inputs":[{"type":"uint256","name":"aNumerator","internalType":"uint256"},{"type":"uint256","name":"aDenominator","internalType":"uint256"},{"type":"uint256","name":"bNumerator","internalType":"uint256"},{"type":"uint256","name":"bDenominator","internalType":"uint256"},{"type":"uint256","name":"exponent","internalType":"uint256"},{"type":"uint256","name":"_decimals","internalType":"uint256"}],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"getBlockNumberFromHeader","inputs":[{"type":"bytes","name":"header","internalType":"bytes"}],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"getEpochNumber","inputs":[],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"getEpochNumberOfBlock","inputs":[{"type":"uint256","name":"blockNumber","internalType":"uint256"}],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"getEpochSize","inputs":[],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"uint256","name":"major","internalType":"uint256"},{"type":"uint256","name":"minor","internalType":"uint256"},{"type":"uint256","name":"patch","internalType":"uint256"}],"name":"getMinimumClientVersion","inputs":[],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"bytes32","name":"","internalType":"bytes32"}],"name":"getParentSealBitmap","inputs":[{"type":"uint256","name":"blockNumber","internalType":"uint256"}],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"uint256","name":"lookbackWindow","internalType":"uint256"}],"name":"getUptimeLookbackWindow","inputs":[],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"bytes32","name":"","internalType":"bytes32"}],"name":"getVerifiedSealBitmapFromHeader","inputs":[{"type":"bytes","name":"header","internalType":"bytes"}],"constant":true},{"type":"function","stateMutability":"pure","payable":false,"outputs":[{"type":"uint256","name":"","internalType":"uint256"},{"type":"uint256","name":"","internalType":"uint256"},{"type":"uint256","name":"","internalType":"uint256"},{"type":"uint256","name":"","internalType":"uint256"}],"name":"getVersionNumber","inputs":[],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"bytes32","name":"","internalType":"bytes32"}],"name":"hashHeader","inputs":[{"type":"bytes","name":"header","internalType":"bytes"}],"constant":true},{"type":"function","stateMutability":"nonpayable","payable":false,"outputs":[],"name":"initialize","inputs":[{"type":"uint256","name":"major","internalType":"uint256"},{"type":"uint256","name":"minor","internalType":"uint256"},{"type":"uint256","name":"patch","internalType":"uint256"},{"type":"uint256","name":"_gasForNonGoldCurrencies","internalType":"uint256"},{"type":"uint256","name":"gasLimit","internalType":"uint256"},{"type":"uint256","name":"lookbackWindow","internalType":"uint256"}],"constant":false},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"initialized","inputs":[],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"intrinsicGasForAlternativeFeeCurrency","inputs":[],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"isOwner","inputs":[],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"minQuorumSize","inputs":[{"type":"uint256","name":"blockNumber","internalType":"uint256"}],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"minQuorumSizeInCurrentSet","inputs":[],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"numberValidatorsInCurrentSet","inputs":[],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"numberValidatorsInSet","inputs":[{"type":"uint256","name":"blockNumber","internalType":"uint256"}],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"address","name":"","internalType":"address"}],"name":"owner","inputs":[],"constant":true},{"type":"function","stateMutability":"nonpayable","payable":false,"outputs":[],"name":"renounceOwnership","inputs":[],"constant":false},{"type":"function","stateMutability":"nonpayable","payable":false,"outputs":[],"name":"setBlockGasLimit","inputs":[{"type":"uint256","name":"gasLimit","internalType":"uint256"}],"constant":false},{"type":"function","stateMutability":"nonpayable","payable":false,"outputs":[],"name":"setIntrinsicGasForAlternativeFeeCurrency","inputs":[{"type":"uint256","name":"gas","internalType":"uint256"}],"constant":false},{"type":"function","stateMutability":"nonpayable","payable":false,"outputs":[],"name":"setMinimumClientVersion","inputs":[{"type":"uint256","name":"major","internalType":"uint256"},{"type":"uint256","name":"minor","internalType":"uint256"},{"type":"uint256","name":"patch","internalType":"uint256"}],"constant":false},{"type":"function","stateMutability":"nonpayable","payable":false,"outputs":[],"name":"setUptimeLookbackWindow","inputs":[{"type":"uint256","name":"window","internalType":"uint256"}],"constant":false},{"type":"function","stateMutability":"nonpayable","payable":false,"outputs":[],"name":"transferOwnership","inputs":[{"type":"address","name":"newOwner","internalType":"address"}],"constant":false},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"uint256","name":"oldValue","internalType":"uint256"},{"type":"uint256","name":"nextValue","internalType":"uint256"},{"type":"uint256","name":"nextValueActivationEpoch","internalType":"uint256"}],"name":"uptimeLookbackWindow","inputs":[],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"address","name":"","internalType":"address"}],"name":"validatorSignerAddressFromCurrentSet","inputs":[{"type":"uint256","name":"index","internalType":"uint256"}],"constant":true},{"type":"function","stateMutability":"view","payable":false,"outputs":[{"type":"address","name":"","internalType":"address"}],"name":"validatorSignerAddressFromSet","inputs":[{"type":"uint256","name":"index","internalType":"uint256"},{"type":"uint256","name":"blockNumber","internalType":"uint256"}],"constant":true}]'
)
