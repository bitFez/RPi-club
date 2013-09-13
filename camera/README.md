# Web Cameras

Connecting cameras is easy, but only some cameras work. 

If the camera is a webcam, we can use a program called fswebcam to take an image.

Look here to see which cameras work on the Raspberry pi. Most of my testing has been done on the Playstation 3 eye camera.

* DSLR camera

We need to camera to either support PTP (usually mid priced amateur cameras and above), or be a standard USB webcam. 

If the camera supports PTP then we can use gphoto2 to take the image. If the camera supports it, gphoto2 can adjust settings like exposure or aperture settings


# Connections

* plug the camera into the Pi's USB socket
