from PIL import Image
from rembg import remove


#here the jpeg doesn't support rgba so we need to convert it to rgb before saving it as jpeg

#then we take the output and save it as png which supports rgba

try:

   Input = Image.open("mustang.jpg")

   output = remove(Input)

   output.save("mustang_wbg1.png")
except OSError as e:
      
      print(f"An error occurred: {e}")