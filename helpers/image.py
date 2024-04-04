from PIL import Image
import requests
import numpy as np

def image_grid(imgs, rows, cols):
  assert len(imgs) == rows*cols

  w, h = imgs[0].size
  grid = Image.new('RGB', size=(cols*w, rows*h))
  grid_w, grid_h = grid.size

  for i, img in enumerate(imgs):
      grid.paste(img, box=(i%cols*w, i//cols*h))
  return grid

# def shrink_and_paste_on_blank(current_image, mask_width):
#   """
#   Decreases size of current_image by mask_width pixels from each side,
#   then adds a mask_width width transparent frame, 
#   so that the image the function returns is the same size as the input. 
#   :param current_image: input image to transform
#   :param mask_width: width in pixels to shrink from each side
#   """

#   height = current_image.height
#   width = current_image.width

#   #shrink down by mask_width
#   prev_image = current_image.resize((height-2*mask_width,width-2*mask_width))
#   prev_image = prev_image.convert("RGBA")
#   prev_image = np.array(prev_image)

#   #create blank non-transparent image
#   blank_image = np.array(current_image.convert("RGBA"))*0
#   blank_image[:,:,3] = 1

#   #paste shrinked onto blank
#   blank_image[mask_width:height-mask_width,mask_width:width-mask_width,:] = prev_image
#   prev_image = Image.fromarray(blank_image)

#   return prev_image

def shrink_and_paste_on_blank(current_image, mask_width):
    # Correcting the order of height and width for the resize operation
    width, height = current_image.size  # Use .size to get dimensions in (width, height) order

    # Shrink down by mask_width, ensuring dimensions are correctly ordered
    new_width, new_height = width - 2 * mask_width, height - 2 * mask_width
    prev_image = current_image.resize((new_width, new_height), Image.LANCZOS)
    prev_image = prev_image.convert("RGBA")
    prev_image_array = np.array(prev_image)

    # Create blank transparent image of the same size as the current_image
    blank_image = np.zeros((height, width, 4), dtype=np.uint8)

    # Calculate the correct position to paste the shrunken image
    top = mask_width
    left = mask_width
    bottom = height - mask_width
    right = width - mask_width

    # Paste shrunken image onto the blank image
    # Ensure the target slice dimensions match the prev_image_array dimensions
    blank_image[top:bottom, left:right, :] = prev_image_array

    # Convert back to PIL Image
    prev_image_pil = Image.fromarray(blank_image, 'RGBA')

    return prev_image_pil
  
def load_img(address, res=(512, 512)):
    if address.startswith('http://') or address.startswith('https://'):
        image = Image.open(requests.get(address, stream=True).raw)
    else:
        image = Image.open(address)
    image = image.convert('RGB')
    image = image.resize(res, resample=Image.LANCZOS)
    return image
