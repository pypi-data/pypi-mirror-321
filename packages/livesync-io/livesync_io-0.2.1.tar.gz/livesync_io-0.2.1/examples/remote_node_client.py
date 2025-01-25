from livesync import Graph
from livesync.prebuilt import RemoteNode, WebcamNode
from livesync.prebuilt.callbacks import LoggingCallback

if __name__ == "__main__":
    # Remote node client
    #
    #   (X) -> (Y)
    #
    # Node X captures video frames from the webcam
    # Node Y drops frames to achieve a target FPS with a remote node

    workflow = Graph()

    node_x = WebcamNode(name="webcam", fps=30)
    node_y = RemoteNode(
        name="remote_node",
        endpoints=["localhost:50051"],
        settings={"resolution_node": {"target_height": "320"}},
    )

    workflow.add_node(node_x)
    workflow.add_node(node_y)

    workflow.add_edge(node_x, node_y)

    with workflow.compile() as runner:
        try:
            run = runner.run(callback=LoggingCallback())
            print(run)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt: Stopping runner.")
