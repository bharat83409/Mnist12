from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import io
import mysql.connector

app = Flask(__name__)

# MySQL configurations
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'gani',
    'use_pure': True,
}

# Create MySQL connection
try:
    mydb = mysql.connector.connect(**db_config)
except mysql.connector.Error as err:
    print(f"Error during MySQL connection: {err}")
    mydb = None

# Load the trained model
loaded_model = load_model("mnist_classifier_model.h5")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the image file from the POST request
        image_file = request.files['image']
        img_bytes = image_file.read()
        img_stream = io.BytesIO(img_bytes)

        # Load and preprocess the image
        img = image.load_img(img_stream, color_mode="grayscale", target_size=(28, 28))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Make a prediction using the loaded model
        prediction = loaded_model.predict(img_array)
        predicted_label = np.argmax(prediction)

        # Log the prediction in the MySQL database
        log_prediction(image_file.filename, int(predicted_label))

        return render_template('index.html', predicted_label=int(predicted_label))

    except Exception as e:
        return render_template('index.html', error=str(e))

def log_prediction(image_filename, predicted_label):
    try:
        # Check if the connection is established
        if mydb is not None:
            # Create a cursor and execute the SQL query
            cursor = mydb.cursor()
            query = "INSERT INTO predictions (image_filename, predicted_label) VALUES (%s, %s)"
            values = (image_filename, predicted_label)
            cursor.execute(query, values)

            # Commit the transaction and close the cursor
            mydb.commit()
            cursor.close()
        else:
            print("MySQL connection is not established.")

    except Exception as e:
        # Handle the exception (e.g., print it for debugging)
        print(f"Error in log_prediction: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
