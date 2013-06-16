# installed_plugins_list.py

def installed_plugins_list(plugin_path=None):
    """Function to get a list of plugins from plugin_path
    """
    import os

    path = os.path.dirname(__file__)
    path = os.path.join(path, plugin_path)

    installed_plugins = []
    for module in os.listdir(path):
        if os.path.isdir(path + '/' + module) == True:
            installed_plugins.append(module)
    return installed_plugins