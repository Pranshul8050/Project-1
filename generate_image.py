import torch
from diffusers import StableDiffusionPipeline

# Load the model
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe.to("cuda" if torch.cuda.is_available() else "cpu")



# Ask user for input
user_prompt = input("Enter a description for the image you want to generate: ")

# Generate an image
print("Generating image... Please wait.")
image = pipe(user_prompt, num_inference_steps=50, guidance_scale=7.5).images[0]

# Save the image
image.save("generated_image.png")

print("Image generated successfully!")
