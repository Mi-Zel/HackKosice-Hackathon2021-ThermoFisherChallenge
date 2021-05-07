# Hack Kosice Marathon: Your project name
## Team

*JustUs*

### Team members

- Mikuláš Zelenák, Spojená škola svätej Uršule
- Viera Michaela Blažíčková, Spojená škola svätého Františka z Assisi


## Description

*We tried to create programm that will analyze an image and fitt an ellipse aroud the ellipse shaped object in the image.*

## Protoype

*The program can't fitt ellipse yet. It calculates the cordinates where the ellipse lies. It times the whole proces and writes data to the "data.csv" file.*

## How to try

*Please copy the images (in .tiff format) to folder called "images" than open "fittingg.py" and run it. If you dont have all the required libraries instaled please do so before running the program otherwise it won't work.*

*To see the result data please open the "data.csv'.*

*You can also run the Jupiter notebook to see how are we workin on the tasks and you can try to display same things.*

## Challenges and accomplishments

*We learnt how to work with images, grafs, how to give image more contrast, what is convolution how does it work and how to use it. We practiced working with numpy and pandas libraries*

*We managed to optimize and speed up the programm by procesing only the new images. If you try to proces the same image (or image with same name) program will just skip it. This way you can just add images and run programm without worrting that it will process the same images again. Or when you have folder with images and you added newones you can just copy all images into "images" folder in our app and it will proces just the newones. This way you will save much time and work for procesor.*

*The programm processes one image at a time and dthis way it savas memory.*

## Next steps

*We need to implement ellipse fitting. We need to optimize the convolution and finding edges. We need to implement evaluation if there is is ellipse or not. We need to optimize it for harder recognizable images.*

## License

*This repository includes an [unlicense](http://unlicense.org/) statement though you may want [to choose a different license](https://choosealicense.com/).*
