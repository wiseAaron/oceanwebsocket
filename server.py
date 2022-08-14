# coding=utf-8
from oceanwebsocket.oceanwebsocket import *
from utils.oceanlogger import OceanLogger
from message.message_pull_redis import *
import asyncio

class Server:
    def __init__(self):
      # 初始化logger 配置
      OceanLogger()

    async def start(self):
      await asyncio.gather(
        MessagePullRedis().read_message_from_redis())

        # OceanWebSocketServer().start()


if __name__ == "__main__":
    server = Server()
    asyncio.run(server.start())