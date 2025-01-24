"""Plugin module."""

import importlib.util
import inspect
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional, TypeVar

from .core import PepperpyError
from .module import BaseModule, ModuleConfig
from .resources import ResourceError, ResourceInfo, ResourceManager


class PluginError(PepperpyError):
    """Plugin-related errors."""

    def __init__(
        self,
        message: str,
        cause: Optional[Exception] = None,
        plugin_name: Optional[str] = None,
    ) -> None:
        """Initialize plugin error.

        Args:
            message: Error message
            cause: Optional cause of the error
            plugin_name: Optional name of the plugin that caused the error
        """
        super().__init__(message, cause)
        self.plugin_name = plugin_name


@dataclass
class PluginConfig(ModuleConfig):
    """Plugin manager configuration."""

    plugin_dir: str | Path = "plugins"
    enabled: bool = True

    def __post_init__(self) -> None:
        """Validate configuration after initialization.

        Raises:
            ValueError: If name is empty or invalid
        """
        super().__post_init__()
        if not isinstance(self.plugin_dir, (str, Path)):
            raise ValueError("Plugin directory must be a string or Path")


def plugin(name: str) -> Callable[[Any], Any]:
    """Plugin decorator.

    Args:
        name: Plugin name

    Returns:
        Decorated plugin class
    """

    def decorator(cls: Any) -> Any:
        """Plugin decorator implementation.

        Args:
            cls: Plugin class

        Returns:
            Decorated plugin class
        """
        cls.__plugin_name__ = name
        return cls

    return decorator


def is_plugin(obj: Any) -> bool:
    """Check if object is a plugin.

    Args:
        obj: Object to check

    Returns:
        True if object is a plugin
    """
    return hasattr(obj, "__plugin_name__")


@dataclass
class ResourcePluginConfig(PluginConfig):
    """Resource plugin configuration."""

    resource_dir: str | Path = "resources"


@plugin("resource_manager")
class ResourcePlugin:
    """Resource management plugin implementation."""

    def __init__(self, config: ResourcePluginConfig | None = None) -> None:
        """Initialize resource plugin.

        Args:
            config: Resource plugin configuration
        """
        self.config = config or ResourcePluginConfig(
            name="resource_manager", resource_dir="resources"
        )
        self._manager = ResourceManager()
        self._initialized = False

    async def initialize(self) -> None:
        """Initialize resource plugin."""
        if self._initialized:
            return
        self._manager.initialize()
        self._initialized = True

    async def cleanup(self) -> None:
        """Cleanup resource plugin."""
        if not self._initialized:
            return
        self._manager.cleanup()
        self._initialized = False

    def _ensure_initialized(self) -> None:
        """Ensure plugin is initialized."""
        if not self._initialized:
            raise ResourceError("Resource plugin not initialized")

    async def create_resource(
        self, name: str, path: str | Path, metadata: Optional[dict[str, Any]] = None
    ) -> ResourceInfo:
        """Create a new resource.

        Args:
            name: Resource name
            path: Resource path
            metadata: Optional resource metadata

        Returns:
            Resource information

        Raises:
            ResourceError: If resource creation fails
        """
        self._ensure_initialized()
        return self._manager.add_resource(name, path, metadata)

    async def get_resource(self, name: str) -> Optional[ResourceInfo]:
        """Get resource by name.

        Args:
            name: Resource name

        Returns:
            Resource information if found, None otherwise

        Raises:
            ResourceError: If plugin not initialized
        """
        self._ensure_initialized()
        return self._manager.get_resource(name)

    async def list_resources(self) -> list[ResourceInfo]:
        """List all resources.

        Returns:
            List of resource information

        Raises:
            ResourceError: If plugin not initialized
        """
        self._ensure_initialized()
        return self._manager.list_resources()

    async def update_resource(
        self, name: str, metadata: dict[str, Any]
    ) -> ResourceInfo:
        """Update resource metadata.

        Args:
            name: Resource name
            metadata: New resource metadata

        Returns:
            Updated resource information

        Raises:
            ResourceError: If plugin not initialized or resource not found
        """
        self._ensure_initialized()
        resource = self._manager.get_resource(name)
        if not resource:
            raise ResourceError(f"Resource {name} not found")

        resource.metadata.update(metadata)
        return resource

    async def delete_resource(self, name: str) -> None:
        """Delete resource.

        Args:
            name: Resource name

        Raises:
            ResourceError: If plugin not initialized or resource not found
        """
        self._ensure_initialized()
        self._manager.remove_resource(name)


T = TypeVar("T")


class PluginManager(BaseModule[PluginConfig]):
    """Plugin manager implementation."""

    def __init__(self, config: PluginConfig | None = None) -> None:
        """Initialize plugin manager.

        Args:
            config: Plugin manager configuration
        """
        super().__init__(
            config or PluginConfig(name="plugin_manager", plugin_dir="plugins")
        )
        self._plugins: dict[str, Any] = {}

    async def _setup(self) -> None:
        """Setup plugin manager."""
        self._plugins.clear()

    async def _teardown(self) -> None:
        """Cleanup plugin manager."""
        self._plugins.clear()

    async def get_stats(self) -> dict[str, Any]:
        """Get plugin manager statistics.

        Returns:
            Plugin manager statistics
        """
        if not self.is_initialized:
            await self.initialize()

        return {
            "name": self.config.name,
            "plugin_dir": str(self.config.plugin_dir),
            "enabled": self.config.enabled,
            "total_plugins": len(self._plugins),
            "plugin_names": list(self._plugins.keys()),
        }

    def load_plugin(self, path: str | Path) -> None:
        """Load plugin from path.

        Args:
            path: Plugin path

        Raises:
            PluginError: If plugin loading fails
        """
        try:
            spec = importlib.util.spec_from_file_location("plugin", path)
            if not spec or not spec.loader:
                raise PluginError(f"Failed to load plugin from {path}")

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            for _, obj in inspect.getmembers(module):
                if is_plugin(obj):
                    plugin_name = obj.__plugin_name__
                    self._plugins[plugin_name] = obj()

        except Exception as e:
            raise PluginError(f"Failed to load plugin from {path}") from e

    def get_plugin(self, name: str) -> Any:
        """Get plugin by name.

        Args:
            name: Plugin name

        Returns:
            Plugin instance

        Raises:
            PluginError: If plugin not found
        """
        if name not in self._plugins:
            raise PluginError(f"Plugin {name} not found")
        return self._plugins[name]

    def get_plugins(self) -> list[Any]:
        """Get all plugins.

        Returns:
            List of plugin instances
        """
        return list(self._plugins.values())
