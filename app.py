from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hardcoded database for the challenge
users_db = {
    "admin": "@#ert%^&iop"
}

flag = "STURSEC{SQL_1NJ3CT10N_WIN}"


def check_credentials(username, password):
    # Vulnerable SQL query
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print("Executed Query:", query)  # Log the query for testing
    if username in users_db and users_db[username] == password:
        return True
    return False


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if check_credentials(username, password):
            return f"Welcome, {username}! Here is your flag: {flag}"
        else:
            return "Invalid username or password!"

    return render_template_string("""
        <!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Portal</title>
    <style>
        /* Reset some default styles */
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #0073e6, #004d99);
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        /* Container styling */
        .login-container {
            background-color: #ffffff;
            color: #333333;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
            padding: 30px;
            max-width: 400px;
            width: 100%;
            text-align: center;
        }

        /* Heading styling */
        .login-container h1 {
            font-size: 2rem;
            margin-bottom: 20px;
            color: #004d99;
        }

        /* Form element styling */
        .login-container form {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .login-container label {
            font-size: 1rem;
            margin-bottom: 5px;
            text-align: left;
            width: 100%;
        }

        .login-container input[type="text"],
        .login-container input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #cccccc;
            border-radius: 5px;
            font-size: 1rem;
            box-sizing: border-box;
        }

        /* Button styling */
        .login-container input[type="submit"] {
            background-color: #004d99;
            color: #ffffff;
            font-size: 1rem;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .login-container input[type="submit"]:hover {
            background-color: #0073e6;
        }

        /* Responsive Design */
        @media (max-width: 480px) {
            .login-container {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Login Portal</h1>
        <form method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" placeholder="Enter your username" required>
            
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" placeholder="Enter your password" required>
            
            <input type="submit" value="Login">
        </form>
    </div>
</body>
</html>
    """)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

