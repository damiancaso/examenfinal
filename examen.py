from flask import Flask
app=Flask(__name__)



@app.route('/')
def hello_geek():
	return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile</title>
</head>
<body>
    <h1>User Profile</h1>
    <div>
        <h2> Damian Caso </h2>
        <img src="https://i.pinimg.com/736x/fc/61/bb/fc61bb9edcd2fbd6867a885e62141a24.jpg" alt="User Photo">
		<h1>Desarrollo de sistemas de la información </h1>
        <p>Social Media:</p>
        <ul>
            {% for platform, link in user.social_media.items() %}
                <li>{{ platform }}: <a href="https://twitter.com/samuel">https://linkedin.com/in/samuel'</a></li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>'''

if __name__ == "__main__":
	app.run(debug=true)
