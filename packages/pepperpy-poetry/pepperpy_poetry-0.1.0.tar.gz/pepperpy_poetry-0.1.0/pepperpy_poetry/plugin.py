from pathlib import Path
from typing import Any, Dict

import toml
from poetry.plugins.plugin import Plugin
from poetry.poetry import Poetry
from poetry.console.io.io import IO


class SharedConfigPlugin(Plugin):
    def activate(self, poetry: Poetry, io: IO) -> None:
        """
        Activate the plugin and merge shared configurations.
        
        Args:
            poetry: The Poetry instance
            io: The IO instance for console output
        """
        shared_config_path = Path("shared-config.toml")
        
        if shared_config_path.exists():
            io.write_line("[pepperpy-poetry] Loading shared configurations...")
            try:
                shared_config = toml.load(shared_config_path)
                self._merge_configurations(poetry, shared_config)
                io.write_line("[pepperpy-poetry] Shared configurations loaded successfully")
            except Exception as e:
                io.write_error_line(f"[pepperpy-poetry] Error loading shared configurations: {str(e)}")
        else:
            io.write_line("[pepperpy-poetry] No shared-config.toml found. Skipping.")

    def _merge_configurations(self, poetry: Poetry, shared_config: Dict[str, Any]) -> None:
        """
        Merge shared configurations into the project's pyproject.toml
        
        Args:
            poetry: The Poetry instance
            shared_config: The shared configuration dictionary
        """
        for section, values in shared_config.items():
            if isinstance(values, dict):
                poetry.pyproject.data.setdefault(section, {}).update(values)
            else:
                poetry.pyproject.data[section] = values 