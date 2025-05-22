# dependencies
from flask import Flask, render_template, request
from scripts import Encoder, Decoder


# creating instance of Flask class
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home_page():
    return '<h1><center>Decon</center></h1> <a href="http://127.0.0.1:5000/encoder">Encoder</a> <a href="http://127.0.0.1:5000/decoder">Decoder</a>'



@app.route("/encoder", methods=["GET","POST"])
def encoder_page():
    if request.method == "GET":
        return render_template('encoder_page.html')
    else:
        simple_text = request.form['taking_simple_text']
        encoder = Encoder(simple_text)
        encoded_text = encoder.basic_encoding(simple_text)

        return render_template('encoder_page.html', encoded_text=encoded_text)

         


@app.route("/decoder", methods=["GET","POST"])
def decoder_page():
    if request.method == "GET":
        return render_template('decoder_page.html')
    else:
        encoded_text = request.form['taking_encoded_text']
        decoder = Decoder(encoded_text)
        decoded_text = decoder.basic_decoding()

        return render_template('decoder_page.html', decoded_text=decoded_text)






if __name__ == "__main__":
    app.run(debug=True)





