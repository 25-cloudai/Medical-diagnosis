from tensorflow.keras.models import load_model

model = load_model("models/pneumonia_model.keras")

print("Model:", model.name)
print("Type:", type(model))

model.summary()

print("\nLayers:")
for i, layer in enumerate(model.layers):
    print(i, layer.name, layer.__class__.__name__)