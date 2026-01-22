import tensorflow_datasets as tfds
import cv2
import os

dataset, info = tfds.load(
    "plant_village",
    split="train",
    as_supervised=True,
    with_info=True
)

class_names = info.features["label"].names

BASE_DIR = "dataset/images/train"
os.makedirs(BASE_DIR, exist_ok=True)

count = 0

for image, label in dataset.take(2000):
    class_name = class_names[label.numpy()]
    class_dir = os.path.join(BASE_DIR, class_name)
    os.makedirs(class_dir, exist_ok=True)

    img = image.numpy()
    img_path = os.path.join(class_dir, f"{count}.jpg")
    cv2.imwrite(img_path, img)
    count += 1

print("✅ Classification dataset prepared correctly")
