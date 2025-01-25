from pydantic import BaseModel


class Model(BaseModel):
  name: str
  version: str
  description: str
  model_path: str


class ModelList(BaseModel):
  description: str
  models: list[Model]

  def get_params(self, name: str, version: str) -> Model:
    """Get the model params by name or version."""
    for model in self.models:
      if model.name == name or model.version == version:
        return model
    raise ValueError(f"Model {name} not found")