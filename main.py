 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

dogs = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dogs')
def dogs():
    return render_template('dogs.html', dogs=dogs)

@app.route('/add_dog', methods=['GET', 'POST'])
def add_dog():
    if request.method == 'POST':
        dog = {
            'name': request.form['name'],
            'age': request.form['age'],
            'breed': request.form['breed'],
            'description': request.form['description']
        }
        dogs.append(dog)
        return redirect(url_for('dogs'))
    else:
        return render_template('add_dog.html')

@app.route('/edit_dog/<int:dog_id>', methods=['GET', 'POST'])
def edit_dog(dog_id):
    dog = dogs[dog_id]
    if request.method == 'POST':
        dog['name'] = request.form['name']
        dog['age'] = request.form['age']
        dog['breed'] = request.form['breed']
        dog['description'] = request.form['description']
        return redirect(url_for('dogs'))
    else:
        return render_template('edit_dog.html', dog=dog)

@app.route('/delete_dog/<int:dog_id>')
def delete_dog(dog_id):
    dogs.pop(dog_id)
    return redirect(url_for('dogs'))

if __name__ == '__main__':
    app.run(debug=True)


HTML code for index.html

html
<!DOCTYPE html>
<html>
<head>
  <title>Dog Lover Website</title>
</head>
<body>
  <h1>Welcome to the Dog Lover Website!</h1>
  <p>This website is a great resource for dog lovers. Here you can find information on different breeds of dogs, how to care for your dog, and where to find dog-friendly activities in your area.</p>
  <p><a href="/dogs">Click here</a> to see a list of all the dogs in our database.</p>
</body>
</html>


HTML code for dogs.html

html
<!DOCTYPE html>
<html>
<head>
  <title>Dog Lover Website</title>
</head>
<body>
  <h1>List of Dogs</h1>
  <ul>
    {% for dog in dogs %}
      <li>{{ dog.name }} ({{ dog.age }} years old, {{ dog.breed }})</li>
    {% endfor %}
  </ul>
  <p><a href="/add_dog">Click here</a> to add a new dog to the database.</p>
</body>
</html>


HTML code for add_dog.html

html
<!DOCTYPE html>
<html>
<head>
  <title>Dog Lover Website</title>
</head>
<body>
  <h1>Add a New Dog</h1>
  <form action="/add_dog" method="post">
    <label for="name">Name:</label><br>
    <input type="text" id="name" name="name"><br>
    <label for="age">Age:</label><br>
    <input type="number" id="age" name="age"><br>
    <label for="breed">Breed:</label><br>
    <input type="text" id="breed" name="breed"><br>
    <label for="description">Description:</label><br>
    <textarea id="description" name="description"></textarea><br><br>
    <input type="submit" value="Submit">
  </form>
</body>
</html>


HTML code for edit_dog.html

html
<!DOCTYPE html>
<html>
<head>
  <title>Dog Lover Website</title>
</head>
<body>
  <h1>Edit Dog</h1>
  <form action="/edit_dog/{{ dog.id }}" method="post">
    <label for="name">Name:</label><br>
    <input type="text" id="name" name="name" value="{{ dog.name }}"><br>
    <label for="age">Age:</label><br>
    <input type="number" id="age" name="age" value="{{ dog.age }}"><br>
    <label for="breed">Breed:</label><br>
    <input type="text" id="breed" name="breed" value="{{ dog.breed }}"><br>
    <label for="description">Description:</label><br>
    <textarea id="description" name="description">{{ dog.description }}</textarea><br><br>
    <input type="submit" value="Submit">
  </form>
</body>
</html>
