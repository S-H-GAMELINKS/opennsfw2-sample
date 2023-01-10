import opennsfw2 as n2

image_path = "./safe.jpg"

nsfw_probability = n2.predict_image(image_path)

print("######################################")
print(nsfw_probability)
print("######################################")

image_path = "./nsfw.jpg"

nsfw_probability = n2.predict_image(image_path)

print("######################################")
print(nsfw_probability)
print("######################################")
