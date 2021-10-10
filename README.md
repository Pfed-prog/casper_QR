# Casper_QR

The repository generates QR codes for transactions on Casper local nodes, [casper.live](https://cspr.live) and [testnet.casper.live](https://testnet.cspr.live)

The app is hosted on AWS and can be accessed via http://sample-env.eba-wb9b6xgh.us-east-2.elasticbeanstalk.com/

![](https://i.imgur.com/KYyfJIl.jpg?1)

For testing on the desktop computer online qr code reader can be used https://4qrcode.com/scan-qr-code.php

For obtaining testnet funds use [faucet](https://testnet.cspr.live/tools/faucet)

## Local Installation

`pip install -r requirements.txt`

`python3 application.py`

Go to http://127.0.0.1:5000/

## Further Development

We intend to connect to Casper Signer Extension in the near future. Develop further app functionality such as staking which is also available at https://casperholders.io/.

To do so we will add ReactJS to the flask application.
