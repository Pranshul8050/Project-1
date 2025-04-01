AI Image Generator using Stable Diffusion
📌 Overview
This project is an AI-powered image generation system that uses a Stable Diffusion model to generate images based on user input. The user provides a text prompt, and the model generates a unique image accordingly.

⚡ Features
✅ Interactive text-based prompt input
✅ Uses Stable Diffusion v1.5 for high-quality image generation
✅ Supports CUDA acceleration (if available)
✅ Saves generated images automatically

🚀 Installation & Setup
1️⃣ Clone the Repository
sh
2️⃣ Install Dependencies
Ensure you have Python 3.8+ installed, then run
pip install torch torchvision torchaudio diffusers transformers accelerate scipy matplotlib
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
3️⃣ Run the Project
sh
python generate_image.py
Then enter a prompt, and the AI will generate an image! 🎨

🛠 Usage Example
Enter a description for the image you want to generate: A futuristic city with neon lights
✅ Image generated successfully! Saved as generated_image.png

📸 Sample Output
Input Prompt	Generated Image
"A cyberpunk city with flying cars"	
📌 Future Enhancements
🔹 Add GUI support for easier interaction
🔹 Implement multiple AI models for different styles
🔹 Optimize performance for faster generation
