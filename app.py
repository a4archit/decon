# dependencies
from flask import Flask, render_template, request, jsonify
from scripts import Encoder, Decoder




# creating instance of Flask class
app = Flask(__name__)






# creating objects of Encoder and Decoder
encoder = Encoder()
decoder = Decoder()






#               UTILITY FUNCTIONS   

def get_converted_text(text, operation_type):
    if operation_type == "encode":
        encoded_text = encoder.basic_encoding(text)
        updated_text = encoded_text

    elif operation_type == "decode":
        decoded_text = decoder.basic_decoding(text)
        updated_text = decoded_text

    return updated_text




# --------------- Home page ---------------- #
@app.route("/", methods=["GET"])
def home_page(): 
    return render_template('html_content.html')





# -------------------- API ------------------------- #
@app.route("/api/<string:operation_type>/<string:text>")
def api(text, operation_type) -> None :
    updated_text = get_converted_text(text, operation_type)
    api_data = {
        "original_text": text,
        "operation_type": operation_type,
        "converted_text": updated_text
    }
    return jsonify(api_data)



# --------------- Main page ----------------- #
@app.route("/tool", methods=["GET","POST"])
def main() -> None:
    if request.method == "GET":
        return render_template("html_content.html")
    else:
        try:
            encoded_text: str = None
            operation_type = request.form['enc_dec_radio']
            text = request.form['text_input']

            updated_text = get_converted_text(text, operation_type)
            

        except Exception as e: 
            print(e)

        return render_template("html_content.html", operation_type=operation_type, updated_text=updated_text)








if __name__ == "__main__":

    app.run(debug=True)





