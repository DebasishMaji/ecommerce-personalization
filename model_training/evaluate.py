import xgboost as xgb
import matplotlib.pyplot as plt

# Load the model
model = xgb.Booster()
model.load_model("model_training/model.bin")

print("Model loaded. Insert evaluation code here to generate visualizations, e.g., loss curves or ROC curves.")
# Example placeholder: plot dummy loss curve
loss = [1.0, 0.8, 0.6, 0.5, 0.45]
plt.plot(loss)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss Curve")
plt.show()
