# username_generator.py
from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

# Music-themed words for username generation
music_adjectives = ["melodic", "rhythmic", "harmonic", "acoustic", "electric", 
                   "jazzy", "funky", "classical", "rock", "pop", "indie"]
music_nouns = ["guitarist", "drummer", "pianist", "vocalist", "composer", 
               "maestro", "soloist", "bassist", "producer", "dj", "musician"]

@app.route('/generate', methods=['POST'])
def generate_username():
    data = request.get_json()
    
    # Extract data or use defaults
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')
    favorite_genre = data.get('favorite_genre', '')
    
    # Generate username options
    usernames = []
    
    # Option 1: first initial + last name + random number
    if first_name and last_name:
        username1 = first_name[0].lower() + last_name.lower() + str(random.randint(1, 999))
        usernames.append(username1)
    
    # Option 2: music adjective + first name + random digit
    if first_name:
        adj = random.choice(music_adjectives)
        username2 = adj + first_name.lower() + str(random.randint(0, 9))
        usernames.append(username2)
    
    # Option 3: genre + music noun + random characters
    if favorite_genre:
        noun = random.choice(music_nouns)
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
        username3 = favorite_genre.lower() + noun + random_suffix
        usernames.append(username3)
    
    # Default option if no input provided
    if not usernames:
        adj = random.choice(music_adjectives)
        noun = random.choice(music_nouns)
        username_default = adj + noun + str(random.randint(100, 999))
        usernames.append(username_default)
    
    return jsonify({
        'success': True,
        'usernames': usernames
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'service': 'username-generator'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)