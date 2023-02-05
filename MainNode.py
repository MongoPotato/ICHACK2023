from Node import SportNode
import time

hostip = ""
node = SportNode(hostip, 10001)

time.sleep(2)

node.start()
try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    node.stop()

