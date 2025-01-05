from flask import Flask, render_template, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
    
    audio_file = request.files['audio']
    print(f"Received audio file: {audio_file.filename}")
    
    recognizer = sr.Recognizer()
    
    try:
        audio = sr.AudioFile(audio_file)
        with audio as source:
            audio_data = recognizer.record(source)
        
        text = recognizer.recognize_google(audio_data)
        return jsonify({'transcription': text})
    
    except Exception as e:
        print(f"Error during transcription: {str(e)}")
        return jsonify({'error': 'Transcription failed. Please try again.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
