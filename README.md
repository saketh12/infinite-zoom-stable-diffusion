# Smooth Infinite Zoom  

### A user friendly colab notebook to generate infinite loop videos in minutes (works on free colab plan)
  
<a target="_blank" href="https://colab.research.google.com/github/BalintKomjati/smooth-infinite-zoom/blob/main/smooth_infinite_zoom.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>



### Examples:

Dream of a distant galaxy:

https://user-images.githubusercontent.com/47415815/220372351-76a8b510-a42c-4025-99d3-9b6976cf10c4.mp4
  
Downtown alley:

https://user-images.githubusercontent.com/47415815/220378972-d8612868-22bc-4c41-8fa8-92c97caa7df1.mp4
  
Colorful fractals:

https://user-images.githubusercontent.com/47415815/220379181-bf5c6624-1680-4480-ab27-ad4439edb1a2.mp4
  
Creepy tunnel:

https://user-images.githubusercontent.com/47415815/220379251-22b405f5-7b7c-4f2a-b4dd-c5df413afbee.mp4
  
Cave of skulls:

https://user-images.githubusercontent.com/47415815/220379362-4ef3d810-9b4c-4376-8200-29eba8ef16c3.mp4

### Credits

 - Original idea and 1st version of the notebook was created by @hardmaru
 - Thereafter @BalintKomjati made the following improvements:
    - Adopted to run on Google Colab
    - Introduced "interpolation" between outpainted images so output is smoother. This also allows to use larger outpainting steps, which enables larger coherent structures to appear more easily on the video, without unpleasant jumps between to frames.
    - Put the whole product into a intuitive, user friendly notebook (at least that was the intention :) )


### Backlog of potential improvements (contributions are welcome):

 - Add the possibility for the output to "drift" between prompts (now uses the same prompt for all images with different seed)
 - Fix the issue that any resolution higer than 512 will drastically decrease the network's imagination resulting the generated video rather boring. (e.g. upscale after each inpainting step?)
 - Make movement in the video more realistic without "fisheye" distorsions
 - Possibility to change movement of the camera during video (e.g. turns in any direction)
 - Generate video in non-cubic resolution (now only cubic is possible)
