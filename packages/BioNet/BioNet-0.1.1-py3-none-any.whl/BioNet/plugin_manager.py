import os
import sys
import importlib
import importlib.util
import pkgutil
from .plugin_interface import PluginInterface
class PluginManager:
    def __init__(self, plugin_directory):
        print(f"Initializing PluginManager - plugin directory: {plugin_directory}" )
        self.plugin_directory = os.path.join(os.path.dirname(__file__), plugin_directory)
        self.plugins = []

    def load_plugins2(self):
        for _, module_name, _ in pkgutil.walk_packages(path=[self.plugin_directory], prefix=''):
            print(f"Found module: {module_name}")
            module_short_name = module_name.replace(self.plugin_pre, '').replace('.py', '')
            module = importlib.import_module(f"{self.plugin_directory}.{module_short_name}")
            for item_name in dir(module):
                print(f"item_name: {item_name}")
                item = getattr(module, item_name)
                if isinstance(item, type) and issubclass(item, PluginInterface) and item is not PluginInterface:
                    self.plugins.append(item())
    def load_plugins(self):
        for root, dirs, files in os.walk(self.plugin_directory):
            for file in files:
                if file.endswith(".py"):
                    print(f"Plugin filename: {file}")
                    plugin_name = file.replace('.py', '')
                    # You can add additional logic here to load the plugin
                    # For now, just print the name
                    print(f"Plugin name: {plugin_name}")
                    module = self.load_plugin(plugin_name)
                    #if isinstance(item, type) and issubclass(item, PluginInterface) and item is not PluginInterface:
                    self.plugins.append(module)

                    
    def load_plugin(self, plugin_name: str):
        print(f"Loading plugin: {plugin_name}")
        # Construct the full path to the plugin file</s>
        # plugin = self.plugin_pre+plugin_name
        plugin_path = os.path.join(self.plugin_directory, f"{plugin_name}.py")
        if not os.path.exists(plugin_path):
            return None
        spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
        if spec is None:
            raise ImportError(f"Cannot get module spec from file location: {plugin_path}")
        module = importlib.util.module_from_spec(spec)
        # Add the module to sys.modules
        sys.modules[plugin_name] = module
        spec.loader.exec_module(module)
        
        return module

    def run_plugin(plugin_name:str):
        data = request.json
        plugin_name = data.get(plugin_name)
        plugin = load_plugin(plugin_name)
        if plugin and hasattr(plugin, 'execute'):
            plugin.execute()
            return jsonify({"status": "success", "message": f"Plugin {plugin_name} executed."})
        return jsonify({"status": "error", "message": "Plugin not found or does not have a run method."})

    def execute_plugins(self, *args, **kwargs):
        for plugin in self.plugins:
            print(f"executing plugin: {plugin.__name__}")
            function = getattr(plugin, "execute")
            # if callable(function):
                # print(f"Executing plugin: {plugin.__name__}")
            # function(*args, **kwargs)
            plugin.execute()
