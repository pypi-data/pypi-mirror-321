import os
from typing import Optional

import cv2
import scipy
from torch.utils.data import Dataset
from torchvision import transforms

from pyvisim._config import *

setup_logging()

__all__ = ['OxfordFlowerDataset']

class OxfordFlowerDataset(Dataset):
    """
    Oxford Flower Dataset. It can be found at: https://www.robots.ox.ac.uk/~vgg/data/flowers/102/index.html

    Organize the data like this:

    ```
    oxford_flower_dataset/
    ├── images
    │   ├── image_00001.jpg
    │   ├── image_00002.jpg
    │   └── ...
    │   ├── image_08189.jpg
    ├── imagelabels.mat
    └── setid.mat
    ```
    In the original dataset, number of train images ('trnid') is 1020,
    number of validation images ('valid') is 1020, and number of test images ('tstid') is 6149. Since
    it makes more sense to have more images for training for this project, the train and test
    splits have been swapped.
    
    :param image_dir: Directory containing image files.
    :param image_labels_file: Path to the file containing image labels.
    :param set_id_file: Path to the file containing set IDs (train/test/val splits).
    :param transform: Transformations to apply to the images.
    :param purpose: Purpose of the dataset ('train', 'test', 'validation'). You
    can also pass a list such as ['train', 'validation'] to get a combined dataset.
    """
    def __init__(self,
                 image_dir: str = IMG_DATA_PATH_FLOWER,
                 image_labels_file: str = LABELS_PATH_FLOWER,
                 set_id_file: str = SETID_PATH_FLOWER,
                 transform: Optional[transforms.Compose] = None,
                 purpose: str | list[str] = 'train') -> None:
        self.image_dir = image_dir
        self.transform = transform
        self.purpose = [purpose] if isinstance(purpose, str) else purpose
        if len(set(self.purpose)) < len(self.purpose):
            raise ValueError("Duplicate purposes found in the list. Please provide unique purposes.")
        self.labels = self._load_labels(image_labels_file)
        self.image_paths = self._load_image_paths()
        self.train_ids, self.val_ids, self.test_ids = self._load_set_ids(set_id_file)
        self.image_paths, self.labels = self._filter_by_purpose()

    def _load_labels(self, labels_file: str) -> list[int]:
        """
        Load image labels from the given .mat file.

        :param labels_file: Path to the .mat file with labels.
        :return: List of labels.
        """
        mat_data = scipy.io.loadmat(labels_file)
        return mat_data['labels'].squeeze().tolist()

    def _load_image_paths(self) -> list[str]:
        """
        Get sorted paths to all images in the directory.

        :return: List of sorted image file paths.
        """
        images = sorted(
            [f for f in os.listdir(self.image_dir) if f.endswith('.jpg')]
        )
        return [os.path.join(self.image_dir, img) for img in images]

    def _load_set_ids(self, set_id_file: str) -> tuple[list[int], list[int], list[int]]:
        """
        Load train, validation, and test IDs from the setid.mat file.

        :param set_id_file: Path to the .mat file with set IDs.
        :return: Tuple of train, validation, and test IDs.
        """
        mat_data = scipy.io.loadmat(set_id_file)
        train_ids = mat_data['tstid'].squeeze().tolist() # Swaps train and test, since test contains significantly more images
        val_ids = mat_data['valid'].squeeze().tolist()
        test_ids = mat_data['trnid'].squeeze().tolist()
        return train_ids, val_ids, test_ids

    def _filter_by_purpose(self) -> tuple[list[str], list[int]]:
        """
        Filter images and labels based on the dataset purpose.

        :return: Filtered image paths and labels.
        """
        chosen_ids = []
        for p in self.purpose:
            match p:
                case 'train':
                    chosen_ids += self.train_ids
                case 'validation':
                    chosen_ids += self.val_ids
                case 'test':
                    chosen_ids += self.test_ids
                case _:
                    raise ValueError(f"Unknown purpose: {p}. Must be 'train', 'validation', or 'test'.")

        chosen_ids = list(set(chosen_ids))

        filtered_paths = [self.image_paths[i - 1] for i in chosen_ids]
        filtered_labels = [self.labels[i - 1] for i in chosen_ids]
        return filtered_paths, filtered_labels

    def __len__(self) -> int:
        """
        Get the total number of images in the dataset.

        :return: Length of the dataset.
        """
        return len(self.image_paths)

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, int, str]:
        """
        Get an image and its corresponding label.

        :param idx: Index of the image.
        :return: Tuple of transformed image, label, and image path.
        """
        img_path = self.image_paths[idx]
        label = self.labels[idx] if self.labels else -1

        image = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)

        if self.transform:
            image = self.transform(image)

        return image, label, img_path

