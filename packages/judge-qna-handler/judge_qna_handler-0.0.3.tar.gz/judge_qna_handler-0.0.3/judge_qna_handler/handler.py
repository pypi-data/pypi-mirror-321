from flask import Flask, request, jsonify

def get_rag_response_function(get_query_function):
    def endpoint_function():
        """
        Handles HTTP requests to the RAG endpoint and returns a response.

        Expects a JSON payload containing a 'question' field.
        Returns a dictionary with the 'answer' to the question.
        """
        # Retrieve JSON payload from the request
        data = request.get_json()

        # Extract the 'question' from the payload, defaulting to an empty string if not present
        question = data.get('question', "")

        # If no question is provided, return an error message
        if not question:
            return jsonify({"error": "No question provided."}), 400

        try:
            # Obtain the answer by calling get_query_function with the provided question
            answer = get_query_function(question)
        except Exception as e:
            print("Error: ", e)
            return jsonify({"error": "An error occurred"}), 500

        # Return the answer within a dictionary
        return jsonify({
            "answer": answer
        })
    
    return endpoint_function

def create_testing_rag_endpoint(app, get_query_response, route='/get_rag_response', methods=["POST"]):
    """
    Adds a new endpoint to the Flask app programmatically.

    Parameters:
    - app: Flask app object
    - get_query_response: The function to get the query response
    - route: The URL route (string)
    - methods: List of HTTP methods (default is ["POST"])
    """
    # Pass get_query_response to get_rag_response_function
    endpoint_function = get_rag_response_function(get_query_response)
    app.add_url_rule(route, view_func=endpoint_function, methods=methods)

# Example usage
# app = Flask(__name__)

def sample_get_query_response(question):
    # Simulate processing the question
    return f"Processed question: {question}"

# Create the endpoint dynamically
# create_testing_rag_endpoint(app, sample_get_query_response)

# if __name__ == '__main__':
#     app.run()
