import tensorflow as tf
import numpy as np

def start_model(model_path):
    model = tf.keras.models.load_model(model_path, compile=False)
    optimizer = tf.keras.optimizers.Adam()
    model.compile(
        optimizer=optimizer,
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    dummy_input = np.zeros((1, 150, 150, 3))
    _ = model.predict(dummy_input)
    return model
