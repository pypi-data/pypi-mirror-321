import os

import psutil
import yaml

from .schema import ModelList


class ModelManager:
  """cache the models."""

  def __init__(
    self,
    base_path: str,
  ):
    self.base_path = base_path
    config_file = os.path.join(self.base_path, "model.yml")
    if not os.path.exists(self.base_path):
      raise ValueError(f"Base path {self.base_path} does not exist")

    if not os.path.exists(config_file):
      raise ValueError(f"Config file {config_file} does not exist")

    self.model_list = self.load_model_list(config_file)
    self.model_map = {}

  def load_model_list(self, path: str) -> ModelList:
    """Load the model list from the config file."""
    with open(path, "r") as f:
      return ModelList.model_validate(yaml.load(f, Loader=yaml.FullLoader))

  def check_memory(self):
    """Check if the memory is enough."""

    memory_info = psutil.virtual_memory()
    # 1024 * 1024 * 1024 = 1GB
    if memory_info.available < 1024 * 1024 * 1024:
      raise ValueError("Memory is not enough")

  def get_model_path(self, name: str, version: str) -> str:
    """Get the model path by name or version."""
    return os.path.join(
      self.base_path,
      self.model_list.get_params(name, version).model_path,
    )
