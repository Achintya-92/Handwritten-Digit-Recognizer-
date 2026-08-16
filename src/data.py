import tensorflow as tf


def load_mnist():
    (x_train, y_train), (x_test, y_test) = (
        tf.keras.datasets.mnist.load_data()
    )

    # Normalize: 0–255 → 0–1
    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0

    # Add channel dimension
    # (28, 28) → (28, 28, 1)
    x_train = x_train[..., None]
    x_test = x_test[..., None]

    return x_train, y_train, x_test, y_test