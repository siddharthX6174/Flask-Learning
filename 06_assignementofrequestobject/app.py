from flask import Flask, request, render_template

app = Flask("__main__")

@app.route("/")
def take_form():
    return render_template("takeName.html")

@app.route("/checkPalindrome", methods=["POST"])
def check_palindrome():
    name = request.form["name"]
    is_palindrome = name == name[::-1]
    if is_palindrome:
        result = f"{name} is a palindrome."
    else:
        result = f"{name} is not a palindrome."
    return result

if __name__ == "__main__":
    app.run(debug=True)