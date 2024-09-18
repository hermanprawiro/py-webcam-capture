from pygrabber.dshow_graph import FilterGraph

def list_video_capture_devices():
    """
    List all available video capture devices on a Windows system.

    Returns:
        devices (list of tuples): List of available devices and their names.
    """
    graph = FilterGraph()
    devices = [(i, name) for i, name in enumerate(graph.get_input_devices())]
    return devices

if __name__ == "__main__":
    # List and print available video capture devices
    devices = list_video_capture_devices()
    for device_index, device_name in devices:
        print(f"Device Index: {device_index}, Device Name: {device_name}")