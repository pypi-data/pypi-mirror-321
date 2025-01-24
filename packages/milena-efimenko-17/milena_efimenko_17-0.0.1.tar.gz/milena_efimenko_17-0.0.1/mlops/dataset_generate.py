from dataclasses import dataclass
from pathlib import Path

import numpy as np
import typer
from rich import print
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

from mlops.config import Config, cfg_helper

app = typer.Typer()


@dataclass
class Dataset:
    """Класс для набора данных."""

    X_train: np.ndarray
    X_test: np.ndarray
    y_train: np.ndarray
    y_test: np.ndarray

    def save(self, path: Path, dataset_name: str) -> None:
        """Сохранить набор данных в указанном пути (path/dataset_name).

        Параметры
        ----------
        path : Path
            Путь для сохранения набора данных.
        dataset_name : str
            Название набора данных.
        """
        save_path = path / dataset_name
        save_path.mkdir(parents=True, exist_ok=True)

        np.save(save_path / "X_train.npy", self.X_train)
        np.save(save_path / "X_test.npy", self.X_test)
        np.save(save_path / "y_train.npy", self.y_train)
        np.save(save_path / "y_test.npy", self.y_test)

    @staticmethod
    def load(path: Path | str, dataset_name: str) -> "Dataset":
        """Загрузить набор данных из указанного пути (path/dataset_name).

        Параметры
        ----------
        path : Path | str
            Путь для загрузки набора данных.
        dataset_name : str
            Название набора данных.

        Возвращает
        -------
        Dataset
            Загруженный объект набора данных.
        """
        if isinstance(path, str):
            path = Path(path)
        load_path = path / dataset_name

        X_train = np.load(load_path / "X_train.npy")
        X_test = np.load(load_path / "X_test.npy")
        y_train = np.load(load_path / "y_train.npy")
        y_test = np.load(load_path / "y_test.npy")

        return Dataset(X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)


def generate_dataset(config: Config) -> Dataset:
    """Генерация синтетического набора данных.

    Параметры
    ----------
    config : Config
        Объект конфигурации.

    Возвращает
    -------
    Dataset
        Сгенерированный набор данных.
    """
    print(":gear: [bold green]Генерация набора данных...[/bold green]")
    n_features = config.data_params.n_features
    train_size = config.data_params.train_size
    n_samples = config.data_params.n_samples

    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=n_features - 1,
        n_redundant=1,
        random_state=42,
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=train_size, random_state=42
    )

    dataset = Dataset(X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)
    save_path = Path(cfg_helper.base_data_dir)
    save_path.mkdir(parents=True, exist_ok=True)
    dataset.save(save_path, config.data_params.dataset_name)

    print(
        f":floppy_disk: [bold blue]Набор данных сохранен в {save_path / config.data_params.dataset_name}[/bold blue]"
    )

    return dataset


@app.command()
def run():
    generate_dataset(cfg_helper)


if __name__ == "__main__":
    app()
