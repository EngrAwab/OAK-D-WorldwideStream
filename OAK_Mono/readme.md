# OAK-D-WorldwideStream

This file is compatible with all the OAK depth cameras including `OAK-D, OAK-D Lite` etc., because all of the OAK depth cameras have the mono camera. Please note that it is not compatible with those OAK cameras which don't have `mono cameras`.


To use this code, you need to clone this repository:

```bash
git clone https://github.com/EngrAwab/OAK-D-WorldwideStream.git
```
Or download this repository. After downloading the repository, please navigate to the oak_rgb folder. Make sure that you have included your authentication code in ngrok. If not, please read the [instruction first](https://github.com/EngrAwab/OAK-D-WorldwideStream/tree/main). Then open `two PowerShell` windows and execute the following commands:
```bash 
pip install -r requirements.txt
ngrok http http://localhost:8080
```
Then, in Terminal 2, run this:
```bash
streamlit run OAK_RGB.py --server.port 8080
```
`8080` is the port; if you want to change your port, you need to change the port on both commands, and they must be the same.
## Caution
Please note that your internet connection should be stable and have good uploading speed.

