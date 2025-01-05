let isRecording = false;

function startRecording() {
    const micButton = document.getElementById('mic-button');
    const transcriptionText = document.getElementById('transcription-text');
    const transcriptionContainer = document.getElementById('transcription-container');

    if (isRecording) {
        micButton.innerHTML = "🎙️"; // Reset to mic icon
        isRecording = false;
        return;
    }

    micButton.innerHTML = "🛑"; // Change to stop icon while recording
    isRecording = true;

    // Start recording audio
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            const mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();

            mediaRecorder.ondataavailable = async function(event) {
                const audioBlob = event.data;
                const formData = new FormData();
                formData.append('audio', audioBlob, 'audio.wav');

                // Send audio to backend for transcription
                try {
                    const response = await fetch('/transcribe', {
                        method: 'POST',
                        body: formData
                    });

                    const data = await response.json();

                    if (data.transcription) {
                        transcriptionText.textContent = "Transcription: " + data.transcription;
                    } else {
                        transcriptionText.textContent = "Error: Could not transcribe audio.";
                    }
                } catch (error) {
                    transcriptionText.textContent = "Error: Unable to connect to the server.";
                }

                transcriptionContainer.style.display = 'block'; // Show transcription container
                micButton.innerHTML = "🎙️"; // Reset the mic button
                isRecording = false;
            };

            // Stop recording when the user clicks the mic button again
            micButton.onclick = function() {
                mediaRecorder.stop();
            };
        })
        .catch(error => {
            console.error('Error accessing microphone:', error);
            transcriptionText.textContent = "Error accessing microphone.";
        });
}
