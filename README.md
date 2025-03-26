File needs some dependencies.
--------------------------------------------------------------------------------------------------------------------------------------------------
1. Install Visual Studio 2022 - Community edition (free) "In the setup phase, you'll only need the Desktop Development with C++ Package"
2. It will probably ask you to restart your computer.
3. Open your IDE of choice and install the dependencies: -cmake -dlib -face_recognition -numpy -opencvpython (pip install "dependencies listed")
4. You can use the "images" folder to upload new faces so the program recognizes the ones you want. Right now, it only recognizes the ones inside of the folder.
5. The program uses your camera to recognize faces, and updates a firebase database with attendance, date, total_atendance.
6. Make sure the faces match their bd ID.