from flask import Flask, jsonify, render_template, abort,request

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "Dế Mèn Phiêu Lưu Ký",
        "author": "Tô Hoài",
        "year": 1941,
        "category": "Văn học",
        "available": True
    },
    {
        "id": 2,
        "title": "Lập trình C",
        "author": "Nguyễn Văn A",
        "year": 2024,
        "category": "Lập trình",
        "available": True
    },
    {
        "id": 3,
        "title": "Cơ sở dữ liệu",
        "author": "Nguyễn Văn B",
        "year": 2023,
        "category": "Công nghệ",
        "available": False
    },
    {
        "id": 4,
        "title": "Python cơ bản",
        "author": "Nguyễn Văn C",
        "year": 2025,
        "category": "Lập trình",
        "available": True
    }
]

@app.route("/books")
def book_list():
    category = request.args.get("category")

    if category == "laptrinh":
        result = []

        for book in books:
            if book["category"] == "Lập trình":
                result.append(book)
    else:
        result = books

    return render_template("books.html", books=result)


@app.route("/books/<int:book_id>")
def book_detail(book_id):
    for book in books:
        if book["id"] == book_id:
            return render_template("detail.html", book=book)

    abort(404)


@app.route("/api/books")
def api_books():
    return jsonify(books)

@app.route("/api/books/<int:book_id>")
def api_book_detail(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book)

    return jsonify({
        "error": "Không có sách với ID = " + str(book_id)
    }), 404

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.route("/available")
def available_books():
    count = 0

    for book in books:
        if book["available"] == True:
            count = count + 1

    return "Có " + str(count) + " sách sẵn sàng cho mượn"

if __name__ == "__main__":
    app.run(debug=True)