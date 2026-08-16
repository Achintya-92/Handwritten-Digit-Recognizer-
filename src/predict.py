import numpy as np 
import tensorflow as tf 
import matplotlib.pyplot as plt 
 
from data import load_mnist 
 
 
# Load test data 
_, _, x_test, y_test = load_mnist() 
 
# Load trained model 
model = tf.keras.models.load_model( 
    "mnist_cnn.keras" 
) 
 
# Select one image 
index = 0 
image = x_test[index] 
 
# Model expects a batch, so add batch dimension 
prediction = model.predict( 
    image[np.newaxis, ...], 
    verbose=0 
) 
 
# Get probabilities for all 10 digits 
probabilities = prediction[0] 
 
# Highest probability's index 
predicted_digit = np.argmax(probabilities) 
 
print("Predicted digit:", predicted_digit) 
print("Actual digit:", y_test[index]) 
 
print("\nProbabilities:") 
 
for digit, probability in enumerate(probabilities): 
    print(f"{digit}: {probability:.4f}") 
 
 
# Display image 
plt.imshow(image.squeeze(), cmap="gray") 
plt.title( 
    f"Predicted: {predicted_digit} | Actual: {y_test[index]}" 
) 
plt.axis("off") 
plt.show()