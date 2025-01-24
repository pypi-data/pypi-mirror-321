from abc import ABC, abstractmethod
import BioNet as bionet

class PluginInterface(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplementedError("Plugins must implement the execute method.")
    def get_version(self):
        print(f"BioNet Version: {bionet.getVersion()}")
