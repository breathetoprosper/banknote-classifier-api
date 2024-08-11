from flask import Flask, jsonify, request, redirect
import pandas as pd
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# Load your CSV file into a Pandas DataFrame
csv_file_path = r'path_here_to_file\name_of_the_file.csv'
df = pd.read_csv(csv_file_path)
headers = ['variance', 'skewness', 'kurtosis', 'entropy', 'class']
df.columns = headers

# Redirect the root URL to /api/data
@app.route('/')
def index():
    return redirect('/api/data')

# Define a route to serve the entire dataset
@app.route('/api/data', methods=['GET'])
def get_data():
    """
    Get the entire dataset in JSON format.
    This dataset contains information about the banknote authentication dataset.
    It contains 4 features and 1 class target.
    //X-Features
    - Variance: description of variance
    - Skewness: description of skewness
    - Kurtosis: description of kurtosis
    - Entropy: description of entropy
    //Y-Target
    - Class: classification label (0 or 1)
    ---
    responses:
      200:
        description: A list of records from the dataset
        schema:
          type: array
          items:
            type: object
            properties:
              variance:
                type: number
              skewness:
                type: number
              kurtosis:
                type: number
              entropy:
                type: number
              class:
                type: number
    """
    data = df.to_dict(orient='records')
    return jsonify(data)

# Define a route to query specific data
@app.route('/api/data/query', methods=['GET'])
def query_data():
    """
    Query the dataset based on a column and value.
    ---
    parameters:
      - name: column
        in: query
        type: string
        required: true
        description: The column to filter by
      - name: value
        in: query
        type: string
        required: true
        description: The value to filter by
    responses:
      200:
        description: Filtered data
        schema:
          type: array
          items:
            type: object
            properties:
              variance:
                type: number
              skewness:
                type: number
              kurtosis:
                type: number
              entropy:
                type: number
              class:
                type: number
      400:
        description: Invalid input
        schema:
          type: object
          properties:
            error:
              type: string
    """
    column = request.args.get('column')
    value = request.args.get('value')

    if column and value:
        filtered_data = df[df[column] == value].to_dict(orient='records')
        return jsonify(filtered_data)
    else:
        return jsonify({"error": "Please provide column and value query parameters"}), 400

if __name__ == '__main__':
    app.run(debug=True)
