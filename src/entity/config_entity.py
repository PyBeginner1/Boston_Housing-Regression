from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
  root_dir: Path
  raw_data_path: Path
  train_data_path: Path
  test_data_path: Path
  

@dataclass(frozen=True)
class DataTransformationConfig:
     preprocessed_obj_file_path: Path
     scaled_train_path : Path
     scaled_test_path : Path