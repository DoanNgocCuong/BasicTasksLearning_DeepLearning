document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('upload-form');
    const statusMessage = document.getElementById('status-message');
    const inputImage = document.getElementById('input-image');
    const outputImage = document.getElementById('output-image');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const fileInput = document.getElementById('file');
        const file = fileInput.files[0];
        
        if (!file) {
            statusMessage.textContent = 'Please select an image file.';
            return;
        }

        try {
            // Show loading message
            statusMessage.textContent = 'Processing image...';
            
            // Display input image
            const reader = new FileReader();
            reader.onload = (e) => {
                inputImage.src = e.target.result;
            };
            reader.readAsDataURL(file);

            // Prepare form data
            const formData = new FormData();
            formData.append('image', file);

            // Send request to backend
            const response = await fetch('http://localhost:3001/detect', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            
            // Display the processed image using base64 data
            outputImage.src = `data:image/jpeg;base64,${data.image}`;
            
            // Display detection result
            statusMessage.textContent = `Detection result: ${data.plate_text}`;

        } catch (error) {
            console.error('Error:', error);
            statusMessage.textContent = `Error: ${error.message}`;
        }
    });
});
