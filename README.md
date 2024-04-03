# OAK-D-WorldwideStream
Get OAK-D video feed access from anywhere in the world. There are some other approaches as well like using the [robothub](https://www.luxonis.com/robothub) but the issues is that it requires linux. Moreover it is bit complex in terms of customization. 
This approach is valid on Windows and it must be valid on the linux as well but I haven't tested yet. 


## Step 1: Create ngrok Account
1. Create an account on [ngrok](https://dashboard.ngrok.com/login).
2. Once logged in, visit your [Dashboard](https://dashboard.ngrok.com/).
3. In the left-hand menu, navigate to **Your Authtoken** and copy the authentication code.

## Step 2: Install and Connect pyngrok

Install the `pyngrok` library using the following command:
```bash
pip install pyngrok
```
After installing you need to connect your account. So open the powershell and use the following command by replacing authentication code
```bash
ngrok config add-authtoken <TOKEN>
```
After running the above command Sucessfully run this command 
```bash
ngrok http http://localhost:8080
```
You wil get this output after running the command 
```bash
ngrok                                                                   (Ctrl+C to quit)

Session Status                online
Account                       Your_name (Plan: Free)
Version                       3.0.0
Region                        United States (us)
Latency                       78ms
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://84c5df474.ngrok-free.dev -> http://localhost:8080

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```
Please Note the forwarding URL because your site will be live on this adress.In this case the link is _https://84c5df474.ngrok-free.dev_
## Step 3: Hosting your Python Code 

Streamlit is a powerful tool for creating web pages with just a few clicks. Clone this repository and navigate to your desired webpage directory. Launch PowerShell by pressing **Shift+Right Click** in the directory, then run the following command:

```bash
streamlit run app.py --server.port 8080
```
Replace app.py with the name of the Python script you downloaded from this repository.Now Open the link that 
