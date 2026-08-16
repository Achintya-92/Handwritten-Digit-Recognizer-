import numpy as np
import tensorflow as tf

from data import load_mnist


# Load test data
_, _, x_test, y_test = load_mnist()

# Load trained model
model = tf.keras.models.load_model(
    "mnist_cnn.keras"
)


# Predict all test images
predictions = model.predict(
    x_test,
    verbose=0
)

# Convert probabilities → predicted digit
predicted_digits = np.argmax(
    predictions,
    axis=1
)


# Find wrong predictions
wrong_indices = np.where(
     (y_test == 9) & (predicted_digits != 9)
)[0]

print("Actual 9 images:", np.sum(y_test == 9))
print("Wrongly predicted 9:", len(wrong_indices))

print("\nFirst 20 wrong predictions:")

for index in wrong_indices:
    print(
        f"Index: {index}, "
        f"Predicted: {predicted_digits[index]}, "
        f"Actual: {y_test[index]}"
    )

import matplotlib.pyplot as plt


# Show first 12 wrong predictions
plt.figure(figsize=(10, 8))

for i, index in enumerate(wrong_indices[:12]):

    plt.subplot(3, 4, i + 1)

    plt.imshow(
        x_test[index].squeeze(),
        cmap="gray"
    )

    plt.title(
        f"Pred: {predicted_digits[index]}\n"
        f"Actual: {y_test[index]}"
    )

    plt.axis("off")

plt.tight_layout()
plt.show()

# # Probability of predicted class
# confidences = np.max(predictions, axis=1)


# # Sort wrong predictions by confidence
# sorted_wrong = wrong_indices[
#     np.argsort(confidences[wrong_indices])[::-1]
# ]

# print("\nWrong 20 predictions with confidence:")

# for index in wrong_indices[:20]:
#     print(
#         f"Index: {index}, "
#         f"Predicted: {predicted_digits[index]}, "
#         f"Actual: {y_test[index]}, "
#         f"Confidence:{confidences[index]}"
#     )

# -------- Confusion Metrics--------------------------
# from sklearn.metrics import confusion_matrix
# import matplotlib.pyplot as plt

# cm = confusion_matrix(
#     y_test,
#     predicted_digits
# )

# print(cm)

# # ----- Checking reality model pred error vs actual img error
# import seaborn as sns 
# import matplotlib.pyplot as plt 

# plt.figure(figsize=(10,8))

# sns.heatmap(
#     cm,
#     annot=True,
#     fmt="d",
#     cmap="Blues"
# )

# plt.xlabel("Predicted")
# plt.ylabel("Actual")
# plt.title("Confusion Matrix")

# plt.show()

# /-----------------------
# pairs = [
#     (3, 5),
#     (4, 9),
#     (8, 9),
#     (2, 7)
# ]

# plt.figure(figsize=(10, 8))

# plot_index = 1

# for actual, predicted in pairs:

#     indices = np.where(
#         (y_test == actual) &
#         (predicted_digits == predicted)
#     )[0]

#     print(
#         f"Actual {actual} → Predicted {predicted}: "
#         f"{len(indices)} images"
#     )