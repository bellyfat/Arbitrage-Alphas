from web3 import Web3

pairs = {
    'quickswap': {
        Web3.toChecksumAddress(i): {} for i in [
            '0x853ee4b2a13f8a742d64c8f088be7ba2131f670d', #usdc-weth
            '0x6e7a5fafcec6bb1e78bae2a1f0b612012bf14827', #matic-usdc
            '0xadbf1854e5883eb8aa7baf50705338739e558e5b', #matic-weth
            '0xf04adbf75cdfc5ed26eea4bbbb991db002036bdd', #usdc-dai
            '0xf6422b997c7f54d1c6a6e103bcb1499eea0a7046', #weth-usdt
            '0xf6a637525402643b0654a54bead2cb9a83c8b498', #wbtc-usdc
            '0xdc9232e2df177d7a12fdff6ecbab114e2231198d', #wbtc-weth
            '0x4a35582a710e1f4b2030a3f826da20bfb6703c09', #weth-dai
            '0x90bc3e68ba8393a3bf2d79309365089975341a43', #weth-aave
            '0x604229c960e5cacf2aaeac8be68ac07ba9df81c3', #matic-usdt
            '0x2cf7252e74036d1da831d11089d326296e64a728', #usdc-usdt
            
            '0xeef611894ceae652979c9d0dae1deb597790c6ee', #matic-dai
            '0x59153f27eefe07e5ece4f9304ebba1da6f53ca88', #dai-usdt
            '0x264e6bc3f95633725658e4d9640f7f7d9100f6ac', #wmatic-polydoge
            '0xbedee6a7c572aa855a0c84d2f504311d482862f4', #quick-polydoge
            '0x019ba0325f1988213d448b3472fa1cf8d07618d7', #wmatic-quick
            '0x1bd06b96dd42ada85fdd0795f3b4a79db914add5', #weth-quick
            '0xe88e24f49338f974b528ace10350ac4576c5c8a1', #quick-tel
            '0x160532d2536175d65c03b97b0630a9802c274dad', #usdc-miMatic
            '0x5ca6ca6c3709e1e6cfe74a50cf6b2b6ba2dadd67', #link-weth
            '0x289cf2b63c5edeeeab89663639674d9233e8668e', #wmatic-fish
            '0x38fe052f0ce76a2239115589098d2fb5aba01d80', #wmatic-dogira
            '0xa5bf14bb945297447fe96f6cd1b31b40d31175cb', #weth-addy
            '0xfc2fc983a411c4b1e238f7eb949308cf0218c750', #weth-tel
            '0x096c5ccb33cfc5732bcd1f3195c13dbefc4c82f4', #usdc-ghst
            '0xccb9d2100037f1253e6c1682adf7dc9944498aff', #wmatic-ghst
            '0x9a8b2601760814019b7e6ee0052e25f1c623d1e6', #wmatic-qi
            '0x8c1b40ea78081b70f661c3286c74e71b4602c9c0', #weth-qi
            '0x25d56e2416f20de1efb1f18fd06dd12efec3d3d0', #qi-quick
            '0x62052b489cb5bc72a9dc8eeae4b24fd50639921a', #polybunny-weth
            '0x976b7b7fe4293111cacd946c422a64f24a223564', #polybunny-quick
            '0x9e3880647c07ba13e65663de29783ecd96ec21de', #usdc-ice
            '0x9f03309a588e33a239bf49ed8d68b2d45c7a1f11', #dino-weth
        ]
    }
    ,
    'sushiswap':   {
        Web3.toChecksumAddress(i): {} for i in [
            '0x34965ba0ac2451a34a0471f04cca3f990b8dea27', #usdc-weth
            '0xcd353f79d9fade311fc3119b841e1f456b54e858', #matic-usdc
            '0xc4e595acdd7d12fec385e5da5d43160e8a0bac0e', #matic-weth
            '0xcd578f016888b57f1b1e3f887f392f0159e26747', #usdc-dai
            '0xc2755915a85c6f6c1c0f3a86ac8c058f11caa9c9', #weth-usdt
            '0x6ff62bfb8c12109e8000935a6de54dad83a4f39f', #weth-dai
            '0xe62ec2e799305e0d367b0cc3ee2cda135bf89816', #wbtc-weth
            '0x2813d43463c374a680f235c428fb1d7f08de0b69', #weth-aave
            '0xd02b870c556480491c70aaf98c297fddd93f6f5c', #wbtc-usdc
            '0x4b1f1e2435a9c96f7330faea190ef6a7c8d70001', #usdc-usdt
            
            '0x55ff76bffc3cdd9d5fdbbc2ece4528ecce45047e', #matic-usdt
            '0x8929d3fea77398f64448c85015633c2d6472fb29', #matic-dai
            '0x3b31bb4b6ba4f67f4ef54e78bcb0aaa4f53dc7ff', #dai-usdt
            '0xd04934d47cbc46c535cbbee9238a7cfd8c215115', #weth-polydoge
            '0xd6d1ec04a4c8f73c423438c8574bb0179a9e836b', #usdc-polydoge
            '0x47187193994550f53beeaf0538005b38122fb54a', #wmatic-polydoge
            '0xb5846453b67d0b4b4ce655930cf6e4129f4416d7', #sushi-weth
            '0x597a9bc3b24c2a578ccb3aa2c2c62c39427c6a49', #sushi-wmatic
            '0xe15e9d2a5af5c1d3524bbc594ddc4a7d80ad27cd', #sushi-usdc
            '0x8ceed6619aeffd5476315b90eb081485da2aebca', #usdc-miMatic
            '0x74d23f21f780ca26b47db16b0504f2e3832b9321', #link-weth
            '0xcbf6f78981e63ef813cb71852d72a060b583eecf', #wmatic-fish
            '0xd6887723e1e113ef1b43dbba2112e355c3cbda73', #wmatic-dogira
            '0x5fcb390b4422f4ff7940c23618a62bf5f69658a8', #usdc-addy
            '0xb6d9a4649c579b8768f1cb55e9dd6ba99581e4a9', #weth-addy
            '0x224dcacf75a4cebf1959dac1ae9761ba6753d87f', #usdc-ghst
            '0xf69e93771f11aecd8e554aa165c3fe7fd811530c', #wmatic-ghst
            '0xc5666d43f06c073e869bce02407569f578b2072d', #polybunny-weth
            '0xac1188fd1f97f163af6a614b6d456393a25d7a26', #hanu-wmatic
            '0xc8b265a3684145f76512f272b8b3d9c07102cd53', #hanu-weth
            '0x3324af8417844e70b81555a6d1568d78f4d4bf1f', #usdc-dino
        ]
    },
     'dfyn':  {Web3.toChecksumAddress(i): {} for i in  [
        '0x7d51bad48d253dae37cc82cad07f73849286deec', #usdc-eth
        '0xc3379226aeef21464d05676305dad1261d6f3fac', #wmatic-eth
        '0xb7bd6d48c9b1af7e126d0389c6970f157d974f33', #usdc-dai
        '0xbe40f7fff5a2235af9a8cb79a17373162efefa9c', #usdc-usdt
        '0x39eaa90a70e8fdc04e1f63db04e1c62c9ace0641', #wbtc-eth
        
        '0xdd228fdc8a41a02bdea72060f53c1f88a2fd48b6', #dai-usdt
        
        '0x9045b1762a0bc4badd08ee7b1a55c3871de9b7b4', #wmatic-usdt
        '0x7162c0acf32820920a741d8fa466b8e6d60d530d', #weth-aave
        '0x5d577d6cdc82d7b6cac7a101766b68f45bc3e34e', #weth-usdt
        '0x75b2f458e33922bea5572ee0ad9a9e24ddff5888', #usdc-aave

        '0x4f19ad546c66016042623b7ade88923c161e3a3a', #link-weth
        '0x9e2fbb31fbd68472f6cd54a1635b8cd64d78fc1c', #wmatic-fish
        '0x34832d9ac4127a232c1919d840f7aae0fcb7315b', #usdc-ice
        ]
    },
    'polycat':  {
        Web3.toChecksumAddress(i): {} for i in  [
            '0x273c39ebd4e0c49f8cc6e5a2b3c0e4ca355b5352', #usdc-weth
            #'0x8a4ceb4dffa238539c5d62ce424980e8fdb21ebc', #wmatic-usdc
            '0xc4e90ae0298e0e7be0102cce64089231e1e2d67c', #wmatic-weth
            '0xbbbd54c1cd649288d2e584917778eeccd8d8254d', #weth-wbtc
            '0xc8174d091c288ff78de98303c2973140cbcf3b23', #usdc-dai
            '0x3b02a89628a375faf4fc5ec83566801e9d9dce02', #wmatic-wbtc
            '0x97b4f2797cc903d76f9b8ff41a94286f0b16198e', #usdc-usdc
            '0x0509083749716b68f0fdb490a59ca62f2cffebb9', #wbtc-usdt
            '0xe27855cce2ddc3a2e44f1ad3cdc3ec6ce4903bba', #wbtc-dai
            '0x9ce65ae286e74f1268d19ab9b25f102c25dbdcb4', #wmatic-dai
            '0x8432e5c41c5c9fd2a4c0c7def017efb4f89c1327', #dai-usdt            
            '0x4db1087154cd5b33fa275a88b183619f1a6f6614', #wmatic-usdt
            '0x2b1b874cb749472b963a80c5214b3cb3fd7021a8', #weth-dai
            #'0xd534a6b00e45bde6f5fdd7f940491c998743329e', #weth-usdt
            '0x6b2d7c0cc9f75db8dd5228f329730bbc732fea05', #wmatic-fish
            '0xd011337d2a1b4acb59bfa182215036f16b6bdf8e', #wmatic-dogira
        ]
    },
    'ape':  {
        Web3.toChecksumAddress(i): {} for i in  [
            '0x84964d9f9480a1db644c2b2d1022765179a40f68', #usdc-weth
            '0x65d43b64e3b31965cd5ea367d4c2b94c03084797', #matic-usdc
            '0x6cf8654e85ab489ca7e70189046d507eba233613', #matic-weth
            '0x5b13b583d4317ab15186ed660a1e4c65c10da659', #usdc-dai
            '0xd32f3139a214034a0f9777c87ee0a064c1ff6ae2', #matic-dai
            '0xe82635a105c520fd58e597181cbf754961d51e3e', #matic-wbtc
            
            '0x9ec257c1862f1bdf0603a6c20ed6f3d6bae6deb0', #usdc-usdt
            '0x42ed6d85ccf43859cbc46f6efa1f21e21cc24030', #matic-aave
            '0x7b2dd4bab4487a303f716070b192543ea171d3b2', #weth-usdt
            
            '0x8b6631324d4bb1759f708dde77e93ba898bb58c4', #wbtc-weth
            '0xcdbcc1ac4d4e18fb1f2f2d604144fd33e77cda52', #wbtc-usdt
            '0x237ac473ac0ae4551019d9298a4118b3144f26a8', #wbtc-usdc
            '0xbff538ad7c1fd067f5529bbc7aa3b403f66d70cf', #weth-aave
            '0xede04e0cd393a076c49deb95d3686a52ccc49c71', #dai-usdt
        ]
    },
    'waultswap':  {
        Web3.toChecksumAddress(i): {} for i in [
            '0xd928ce1d0f2642e44615768761c0f00c23e0d588', #usdc-weth
            '0x8312a29a91d9fac706f4d2adeb1fa4540fad1673', #wmatic-usdc
            '0x679b8ab80f298bf802fb294137765c6386d43dca', #wmatic-weth
            '0x8e5c5ae2542116b5715b12bb2d391a770a607075', #usdc-dai
            '0x30eef213d4b9c809f5776ae56cc39f02f19f742f', #wbtc-usdc
            '0x7242e19a0937ac33472febd69462668a4cf5bbc5', #usdc-usdt
            '0x30adbcab9fbb4436109fcf3058d1af27e6e33f3f', #wbtc-weth
            '0xf7bc741b2086ca344e78225d06224ffdcd86d110', #wmatic-usdt
            '0xaef35d720c56ef3c259bccdb6931f331c7f15b3f', #weth-dai
            
            #'0x2f8fd97b6a26e0ffa87635c6527af1abf23457a2', #wmatic-dai
            '0x145e99a991a1594e76e2ac4f329bfd6ab84a95bb', #usdc-aave
            #'0x41ff54b8bc443b333ae0476458681ac95725c771', #weth-usdt
        ]
    },
    'polydex':  {
        Web3.toChecksumAddress(i): {} for i in  [
            '0xbdd5e7d186ec062cc46c0fb52a48f52827baf941', #usdc-weth
            '0xdef834ae4a1198bfec84544fb374ec7f1314a7c5', #wmatic-weth
            '0xb78906c8a461d6a39a57285c129843e1937c3278', #usdc-usdt
            '0x4fa5d5143394e52eeb834e46f34449aa0c5b9507', #usdc-dai
            '0xdea6d004c5a2b50d6e35c7b93014d03feaf03f62', #wbtc-weth
            
            
            '0x186bfd06df0bff94aa078912c3210b00f04ee577', #dai-usdt
            '0x737da5f520b47cb15af413fdf93f036d83113a1c', #weth-usdt
            '0x538a485de855e9239570aea1def9adbcbb6af1f8', #weth-dai
         ]
    }
    
}


choice_tokens = [
    Web3.toChecksumAddress(i) for i in
    [
        '0x8f3cf7ad23cd3cadbd9735aff958023239c6a063', #dai
        '0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270', #wmatic
        '0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619', #weth
        '0x2791bca1f2de4661ed88a30c99a7a9449aa84174', #usdc
        '0xc2132d05d31c914a87c6611c10748aeb04b58e8f', #usdt
        #'0x1bfd67037b42cf73acf2047067bd4f2c47d9bfd6', #wbtc
        '0xd6df932a45c0f255f85145f286ea0b292b21c90b', #aave
    ]
]

routers = {
    'quickswap': '0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff',
    'sushiswap': '0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506',
    'dfyn': '0xA102072A4C07F06EC3B4900FDC4C7B80b6c57429',
    'polycat': '0x94930a328162957FF1dd48900aF67B5439336cBD',
    'ape': '0xC0788A3aD43d79aa53B09c2EaCc313A787d1d607',
    'waultswap': '0x3a1D87f206D12415f5b0A33E786967680AAb4f6d',
    #'honeyswap': "0xaD340d0CD0B117B0140671E7cB39770e7675C848", ###'0x1C232F01118CB8B424793ae03F870aa7D0ac7f77'
    'kyberdmm': '0x546C79662E028B661dFB4767664d0273184E4dD1',
    #'firebird': Web3.toChecksumAddress('0xb31d1b1ea48ce4bf10ed697d44b747287e785ad4'),
    'polydex': '0xC60aE14F2568b102F8Ca6266e8799112846DD088',
}

factories = {
    'sushiswap': '0xc35DADB65012eC5796536bD9864eD8773aBc74C4',
    'quickswap': '0x5757371414417b8C6CAad45bAeF941aBc7d3Ab32',
    'dfyn': '0xE7Fb3e833eFE5F9c441105EB65Ef8b261266423B',
    'polycat':'0x477Ce834Ae6b7aB003cCe4BC4d8697763FF456FA',
    'ape': '0xCf083Be4164828f00cAE704EC15a36D711491284',
    'umbra' : '0x7Ff9B69a7b6F11780C3D5d7D04B078ae5e4c219A',
    'kyberdmm': '0x5f1fe642060b5b9658c15721ea22e982643c095c',
    'firebird': '0x5De74546d3B86C8Df7FEEc30253865e1149818C8',
    'polydex': '0xEAA98F7b5f7BfbcD1aF14D0efAa9d9e68D82f640'
}

WMATIC = '0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270'

WETH = '0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619'














