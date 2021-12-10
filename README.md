Instructions
Here are the steps that you need to take, to be able to use the bot:
Go over to https://chromedriver.chromium.org/downloads, and install the chrome driver for you chrome version and put it in the same folder as the bot file is in.

![chromedriver](https://user-images.githubusercontent.com/95449479/145630836-57cd7117-db08-4619-8b56-485b49f49377.png)

To see your chrome version, go to chrome://version
It should say right at the top of the page

![chromedownloads](https://user-images.githubusercontent.com/95449479/145630869-5c055173-d161-4edd-865a-8adfc7f46097.png)

Then install Python, preferably the version 3.8.3 or older (https://www.python.org/downloads/)

Then open up the windows console (either by finding "command prompt" in the windows search or pressing Win + R and typing in cmd)

![cmd](https://user-images.githubusercontent.com/95449479/145630898-3087d4e6-1ee5-42e7-a3eb-f4554c952458.png)

And then separately enter the following commands (clicking Enter in between each one):
```
pip install selenium
pip install selenium-wire
pip install packaging
```
if pip install didn't work, then try to install all of the above modules like this:
```
py -m pip install selenium
```
(use it for all of the other modules above, by just swapping them in for "selenium")

If it still doesn't work, then you will have to reinstall pip using the following command:
```
python -m pip install --upgrade pip
```
and then running the first three commands that were stated above

If you are running the bot on a virtual machine, don't forget to install "visual studio 2015(or older)"
It can be found right here:
https://docs.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170

![redist](https://user-images.githubusercontent.com/95449479/145630945-606bf2fb-6cf9-44d0-a0a2-c4e7732e4942.png)

After you have set up everything stated above, go to the folder where the bot file is stored and right click on the file that you want to use. Click on "Edit with IDLE" to open the file of the bot.

![idle](https://user-images.githubusercontent.com/95449479/145630977-78567ff5-9c04-46bc-8d81-480fb285b307.png)

Then just click on "Run", and then "Run Module" (or just click F5 on your keyboard) and the bot will start working. It will automatically open up the farmersworld game website, and click the login buttons, and you will have 2 minutes to enter your account detail, and click the login button, after which the bot will start automatically endlessly working, as long as you have the needed items in your inventory (e.g. barley seeds, corn seeds, fishing rod, etc.)

![idlerun](https://user-images.githubusercontent.com/95449479/145631004-9d787943-2db1-4350-937f-044d90bc4110.png)

If you have any questions refer to support in the discord: https://discord.gg/EGUW8pn7aw
