#!/usr/bin/env python3

from provisioner_shared.components.remote.domain.config import RemoteConfig
from provisioner_shared.components.runtime.domain.serialize import SerializationBase

PLUGIN_NAME = "installers_plugin"

"""
    Configuration structure -
"""


class InstallersConfig(SerializationBase):
    remote: RemoteConfig = RemoteConfig({})

    def __init__(self, dict_obj: dict) -> None:
        super().__init__(dict_obj)

    def merge(self, other: "InstallersConfig") -> SerializationBase:
        if hasattr(other, "remote"):
            self.remote = self.remote if self.remote is not None else RemoteConfig()
            self.remote.merge(other.remote)
        return self

    def _try_parse_config(self, dict_obj: dict):
        if "remote" in dict_obj:
            self.remote = RemoteConfig(dict_obj["remote"])
