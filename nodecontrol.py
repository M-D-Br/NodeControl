from telethon import TelegramClient, events
import time, sys, telethon.sync, pyqrcode, os
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from pyqrcode import QRCode

api_hash = "[api_hash GOES HERE]"
api_id = "[api_id GOES HERE]"
auth_username = "[USERNAME OF AUTHORISED USER – THE ACCOUNT YOU'LL CONNECT FROM]"

#Bitcoin RPC stuff
rpc_user = "[RPC USERNAME - FOUND IN BITCOIN.CONF]"
rpc_password = "[RPC PASSWORD - FOUND IN BITCOIN.CONF]"
rpc_port = [BITCOIN PORT - 8332 FOR MAINNET, 18332 FOR TESTNET]
nodeip = "[NODE'S IP]"

def btc_generate():
   print("trying RPC")
   try:
    rpc_connect = AuthServiceProxy("http://{}:{}@{}:{}".format(rpc_user,rpc_password,nodeip,rpc_port))
    newaddress = rpc_connect.getnewaddress()
    packqraddr = pyqrcode.create(newaddress)
    packqraddr.png("newaddress.png", scale=8)
    return newaddress
   except:
    return "Something went wrong. Check your node is properly connected."


def sync():
   print("trying sync")
   try:
    rpc_connect = AuthServiceProxy("http://{}:{}@{}:{}".format(rpc_user,rpc_password,nodeip,rpc_port))
    blocks = rpc_connect.getblockcount()
    peers = rpc_connect.getconnectioncount()
    sync_prog = str(round(rpc_connect.getblockchaininfo()['verificationprogress']*100, 2)) + "%"
    return f"👥 Peers: {peers}\n\n⏹ Block Height: {blocks}\n\n🔄 Sync Progress: {sync_prog}"
   except:
    return "Something went wrong. Check your node is properly connected."


def shutdown():
    sys.exit()

def help():
    return "Commands:\n\n'genbtc' to generate a Bitcoin receive address.\n\n'sync' for sync stats.\n\n'KILL' to shut down this client." 




if __name__ == '__main__':

    client = TelegramClient('noded', api_id, api_hash, sequential_updates=True)
    try:
     os.remove('newaddress.png')
    except:
     pass
    print('Session starting...')

    packqraddr = pyqrcode.create("hello")
    packqraddr.png("newaddress.png", scale=8)

    @client.on(events.NewMessage(from_users=auth_username, pattern='h|H|Help|help'))
    async def help_msg(event):
     await event.reply(help())

    @client.on(events.NewMessage(from_users=auth_username, pattern='Genbtc|GENBTC|genbtc'))
    async def receive_msg(event):
      await event.respond("🏦 Retrieving address...")
      await event.reply(btc_generate())
      await client.send_file(auth_username, 'newaddress.png')

    @client.on(events.NewMessage(from_users=auth_username, pattern='sync|SYNC|Sync'))
    async def receive_msg(event):
      await event.respond("Getting node info...")
      await event.reply(sync())


    @client.on(events.NewMessage(from_users=auth_username, pattern='KILL'))
    async def shutdown_msg(event):
      await event.reply('Shutting down...')
      shutdown()



    client.start()
    client.send_message(auth_username, 'Hello! Type "help" for commands.')
    client.run_until_disconnected()

