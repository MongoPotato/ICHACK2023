from BlockNode import SportNode
import time

hostip = "146.179.200.156"
node = SportNode(hostip, 10001)

time.sleep(2)

node.start()
try:
    while True:
        time.sleep(2)
        node.pooling_check_new_node()
except KeyboardInterrupt:
    node.stop()

