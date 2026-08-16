from data import load_mnist
from model import build_model


# Load data
x_train, y_train, x_test, y_test = load_mnist()


# Build model
model = build_model()


# Train
history = model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=32,
    validation_split=0.1
)


# Save trained model
model.save("mnist_cnn.keras")