import tensorflow as tf
from tensorflow.keras import layers, models


def build_model():
    data_augmentation = tf.keras.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.RandomRotation(0.05)
    ])

    model = models.Sequential([
         # Data augmentation
        data_augmentation,

        layers.Conv2D(
            filters=32,
            kernel_size=(3, 3),
            activation="relu",
            input_shape=(28, 28, 1)
        ),

        layers.MaxPooling2D(pool_size=(2, 2)),

        layers.Conv2D(
            filters=64,
            kernel_size=(3,3),
            activation="relu"
        ),

        layers.Flatten(),

        layers.Dense(
            128,
            activation="relu"
        ),

        layers.Dense(
            10,
            activation="softmax"
        )
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model