from p2pnetwork.node import Node
import time


def node_callback(event, node, connected_node, data):
    try:
        if event != 'node_request_to_stop': # node_request_to_stop does not have any connected_node, while it is the main_node that is stopping!
            print('Event: {} from main node {}: connected node {}: {}'.format(event, node.id, connected_node.id, data))

    except Exception as e:
        print(e)


node = Node("146.179.195.212", 8001, node_callback)
node.debug = True

node.start()
time.sleep(2)

node.connect_with_node('146.179.200.156', 8002)

node.send_to_nodes("hi from node 1")

time.sleep(100)

node.stop()