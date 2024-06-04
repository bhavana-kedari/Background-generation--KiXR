from gradio_client import Client, file

client = Client("briaai/BRIA-Background-Generation")
result = client.predict(
		input_image=file(r"C:\Users\91953\Downloads\kiran.jpg"),
		prompt="Create a beautiful beach wedding scene at sunset. The sky should be painted with vibrant hues of orange, pink, and purple, reflecting on the calm ocean. Set up a floral arch with white and pastel flowers on the sandy shore. Include white chairs arranged in rows, adorned with delicate ribbons. Ensure the shadows cast by the arch and chairs are long and soft, with the warm glow of the setting sun creating a romantic atmosphere",
		negative_prompt="Logo,Watermark,Text,Ugly,Morbid,Extra fingers,Poorly drawn hands,Mutation,Blurry,Extra limbs,Gross proportions,Missing arms,Mutated hands,Long neck,Duplicate,Mutilated,Mutilated hands,Poorly drawn face,Deformed,Bad anatomy,Cloned face,Malformed limbs,Missing legs,Too many fingers",
		num_steps=30,
		controlnet_conditioning_scale=1,
		seed=-1,
		api_name="/process"
)
print(result)