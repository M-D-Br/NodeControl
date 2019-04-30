# NodeControl
Telegram bot for generating Bitcoin addresses from full node. This can be run on a separate device, but if you intend to use the lightning invoice generator (coming soon), it will need to be set up on the same device as your node.

Fire up your terminal and clone the repo into a directory of your choosing.

`git clone https://github.com/M-D-Br/NodeControl.git`

`cd NodeControl`

Install and set up a new virtual environment.

`sudo apt install virtualenv`

`virtualenv telegram`

Now we'll download the necessary Python packages.

`pip install telethon`

`pip install python-bitcoinrpc`

`pip install pyqrcode`

`pip install pypng` 

You'll want to create a new Telegram account (I'd recommend <a href="https://hushed.com/pricing/">Hushed</a> if you need a disposable number). From there, log in to <a href="https://my.telegram.org/">Telegram core</a>, select 'API development tools'  and pull your _api_id_ and _api_hash_.

Fill in the necessary parameters in _nodecontrol.py_, then run using:

`python3 nodecontrol.py`
