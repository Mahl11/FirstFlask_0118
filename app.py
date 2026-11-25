from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    nama = ""
    hasil = None
    error = None

    if request.method == "POST":
        # Ambil data dari input yang name="nama"
        nama = request.form.get("nama", "").strip()

        if not nama:
            error = "Nama tidak boleh kosong."
        else:
            hasil = f"Halo, {nama}! Data kamu berhasil diterima lewat method POST."

    return render_template("index.html", nama=nama, hasil=hasil, error=error)


if __name__ == "__main__":
    app.run(debug=True)