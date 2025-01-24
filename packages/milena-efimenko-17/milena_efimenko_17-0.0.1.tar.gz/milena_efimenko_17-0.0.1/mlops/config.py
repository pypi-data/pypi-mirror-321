from enum import Enum
from typing import Any, Optional

import yaml
from pydantic import BaseModel, Field, model_validator


class ModelType(Enum):
    """Класс перечисления для типов моделей."""

    LOG_REG: str = "LogisticRegression"
    DECISION_TREE: str = "DecisionTreeClassifier"
    RANDOM_FOREST: str = "RandomForestClassifier"


class ModelConfig(BaseModel):
    """Класс конфигурации модели."""

    ml_model_type: ModelType

    validate_model: Optional[bool] = Field(
        default=True,
        description="Проводить ли валидацию модели после её обучения",
    )

    run_name: Optional[str] = Field(
        default="run",
        description="Название запуска обучения",
    )

    max_depth: Optional[int] = Field(
        None,
        description="Максимальная глубина дерева/деревьев.",
        ge=1,
        le=10,
    )

    n_estimators: Optional[int] = Field(
        None,
        description="Количество деревьев в лесу",
        ge=5,
        le=1000,
    )

    random_state: Optional[int] = Field(
        default=42, description="Состояние случайности для воспроизводимости", ge=0
    )
    C: Optional[float] = Field(None, description="Отвечает за силу регуляризации", gt=0.0)


class DataConfig(BaseModel):
    """Класс конфигурации данных."""

    dataset_name: str = Field(description="Название набора данных")

    n_features: int = Field(
        description="Количество признаков в синтетическом наборе данных",
        ge=1,
        default=10,
    )

    n_samples: int = Field(
        description="Количество объектов в синтетическом наборе данных",
        ge=1,
        default=1000,
    )

    train_size: float = Field(
        description="Размер обучающей выборки для синтетического набора данных",
        gt=0.0,
        lt=1.0,
        default=0.8,
    )


class Config(BaseModel):
    """Основной класс конфигурации."""

    ml_model_params: ModelConfig
    data_params: DataConfig
    base_data_dir: str = Field(default="data/processed", 
                               description="Путь для хранения наборов данных")
    base_models_dir: str = Field(default="models", description="Путь для хранения моделей")
    base_reports_dir: str = Field(default="reports", description="Путь для хранения отчетов")

    @classmethod
    def load_yaml(cls, file_path: str) -> "Config":
        """Загрузить конфигурацию из YAML файла.

        Параметры
        ----------
        file_path : str
            Путь к YAML файлу.

        Возвращает
        -------
        Config
            Объект конфигурации.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)

        return cls(**yaml_data)

    @model_validator(mode="before")
    @classmethod
    def check_cfg_before(cls, values: dict) -> Any:
        """Проверить конфигурацию перед загрузкой.

        Параметры
        ----------
        values : dict
            Значения конфигурации.

        Возвращает
        -------
        Any

        Исключения
        ----------
        ValueError
            Если конфигурация неверна.
        """
        ml_model_params = values.get("ml_model_params")

        ml_model_type = ml_model_params.get("ml_model_type")
        max_depth = ml_model_params.get("max_depth")
        n_estimators = ml_model_params.get("n_estimators")
        C = ml_model_params.get("C")

        if ml_model_type == ModelType.LOG_REG and C is None:
            raise ValueError("C должен быть указан для модели логистической регрессии.")
        if ml_model_type == ModelType.DECISION_TREE and max_depth is None:
            raise ValueError("max_depth должен быть указан для модели дерева решений.")
        if ml_model_type == ModelType.RANDOM_FOREST:
            if max_depth is None:
                raise ValueError("max_depth должен быть указан для модели случайного леса.")
            if n_estimators is None:
                raise ValueError("n_estimators должен быть указан для модели случайного леса.")

        return values
cfg_helper = Config.load_yaml("config.yaml")
