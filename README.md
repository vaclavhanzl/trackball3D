# trackball3D
Read billiard ball rotations in any 3D axis and control pymol camera accordingly.

<img src="doc/images/trackball3D.jpg" width="500">

Obviously, you also need to make the device :) Buy two mice and one billiard ball, 3D-print a piece of
plastic to keep it together and here you go!

If one day the model is ready, I will put it to [my Printables page](https://www.printables.com/@vaclavh_797838/models).

In the meantime, I think some pymol related tricks I used are worth publishing by themselves.

## Installation

You need to get priviledges to be able to mess with mouse inputs:
```
sudo gpasswd -a YOUR-OWN-USERNAME input
```
Get the source code, create virtual environment for it, install evdev and run the code:
```
git clone https://github.com/vaclavhanzl/trackball3D.git
cd trackball3D
python3 -m venv env
env/bin/pip3 install evdev
env/bin/python3 trackball
```

(See my [hacktrack](https://github.com/vaclavhanzl/hacktrack) project for details of what is needed.
You can leave out xdo, trackball3D does not use it).
