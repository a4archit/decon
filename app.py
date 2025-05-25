# dependencies
from flask import Flask, render_template, request
from scripts import Encoder, Decoder


# creating instance of Flask class
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home_page():
    return render_template('html_content.html')





@app.route("/tool", methods=["GET","POST"])
def tool_operations() -> None:
    if request.method == "GET":
        return render_template("html_content.html")
    else:
        try:
            encoded_text: str = None
            operation_type = request.form['enc_dec_radio']
            text = request.form['text_input']

            if operation_type == "encode":
                encoder = Encoder()
                encoder.update_text(text)
                encoded_text = encoder.basic_encoding()
                updated_text = encoded_text

            elif operation_type == "decode":
                decoder = Decoder()
                decoder.update_text(text)
                decoded_text = decoder.basic_decoding()
                updated_text = decoded_text

        except Exception as e:
            print(e)

        return render_template("html_content.html", operation_type=operation_type, updated_text=updated_text)



# @app.route("/encoder", methods=["GET","POST"])
# def encoder_page():
#     if request.method == "GET":
#         return render_template('encoder_page.html')
#     else:
#         simple_text = request.form['taking_simple_text']
#         encoder = Encoder(simple_text)
#         encoded_text = encoder.basic_encoding(simple_text)

#         return render_template('encoder_page.html', encoded_text=encoded_text)

         


# @app.route("/decoder", methods=["GET","POST"])
# def decoder_page():
#     if request.method == "GET":
#         return render_template('decoder_page.html')
#     else:
#         encoded_text = request.form['taking_encoded_text']
#         decoder = Decoder(encoded_text)
#         decoded_text = decoder.basic_decoding()

#         return render_template('decoder_page.html', decoded_text=decoded_text)






if __name__ == "__main__":
    app.run(debug=True)





