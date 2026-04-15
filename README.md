
# Pawsey Upload Tool (APPN)

A simple tool to upload data to Pawsey (Acacia S3).

This tool:

*  Uploads files and folders
*  Lets you view your uploaded files
*  Handles all Pawsey technical settings internally

---

# Quick Start (3 Steps)

---

## 1. Install Python and rclone

You need two programs installed on your computer: **Python** and **rclone**. Follow the steps for your operating system below.

### Windows:

#### Install Python:

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click the big yellow **"Download Python"** button
3. Open the downloaded file to start the installer
4. **Important:** On the first screen, tick the checkbox that says **"Add python.exe to PATH"** (at the bottom of the window)
5. Click **"Install Now"**
6. Wait for it to finish, then click **"Close"**

To check it worked, open **Command Prompt** (search "cmd" in the Start menu) and type:

```
python --version
```

You should see something like `Python 3.x.x`. If you see an error, try again.

#### Install rclone:

1. Go to [https://rclone.org/downloads/](https://rclone.org/downloads/)
2. Under **Windows**, click **"Intel/AMD - 64 Bit"** to download the zip file
3. Open the downloaded zip file
4. Copy the **rclone.exe** file inside it to a folder you'll remember (e.g. `C:\rclone\`)
5. **Add rclone to your PATH** so you can use it from anywhere:
   - Search **"Environment Variables"** in the Start menu
   - Click **"Edit the system environment variables"**
   - Click the **"Environment Variables"** button
   - Under **"User variables"**, select **"Path"** and click **"Edit"**
   - Click **"New"** and type the folder where you put rclone (e.g. `C:\rclone`)
   - Click **"OK"** on all windows

To check it worked, open a **new** Command Prompt window and type:

```
rclone version
```

You should see version information. If you see an error, make sure you completed step 5 above and opened a **new** Command Prompt window.

### Mac:

#### Install Python:

Most Macs already have Python installed. To check, open **Terminal** (search "Terminal" in Spotlight, or find it in Applications > Utilities) and type:

```
python3 --version
```

If you see something like `Python 3.x.x`, you're good to go. If not:

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click the big yellow **"Download Python"** button
3. Open the downloaded file and follow the installer steps
4. When it finishes, close and reopen Terminal, then try `python3 --version` again

> **Note for Mac users:** Use `python3` instead of `python` in all commands below. For example: `python3 pawsey_uploader.py upload ...`

#### Install rclone:

If you have Homebrew installed (a common Mac tool), open Terminal and type:

```
brew install rclone
```

If you don't have Homebrew, you can install rclone directly:

1. Go to [https://rclone.org/downloads/](https://rclone.org/downloads/)
2. Under **macOS**, download the file for your Mac type:
   - **Apple Silicon (M1/M2/M3/M4)** — most Macs from 2021 onwards
   - **Intel/AMD** — older Macs (before 2021)
   - Not sure? Click the Apple menu () > **About This Mac** and check the **Chip** line
3. Open the downloaded zip file
4. Open Terminal and run these commands (copy and paste each line one at a time):
   ```
   cd ~/Downloads/rclone-*-osx-*
   sudo cp rclone /usr/local/bin/
   ```
5. It will ask for your Mac password — type it in (you won't see characters appear, that's normal) and press Enter

To check it worked, type:

```
rclone version
```

---

##  2. Configure your Pawsey access

Run:

```bash
rclone config
```

Follow prompts:

```
n) New remote
name: pawsey-user
type: s3
```

Enter:

```
endpoint: https://projects.pawsey.org.au
access_key_id: <your key>
secret_access_key: <your secret>
region: (leave blank)
```

You can find access_key_id and secret_access_key in Pawsey portal. Login -> Acacia -> Create New Key -> Copy Access ID and Secret Key
---

## 3. Upload data

```bash
python pawsey_uploader.py upload /path/to/data your-bucket-name
```

### Example:

```bash
python pawsey_uploader.py upload ./drone-data adelaideu-data
```

---

# Commands

---

##  Upload files or folders

```bash
python pawsey_uploader.py upload <local_path> <bucket>
```

 Uploads all files from your computer to Pawsey

---

##  View your uploaded files

```bash
python pawsey_uploader.py list <bucket>
```

### Example:

```bash
python pawsey_uploader.py list adelaideu-data
```

---

#  If your upload stops

Just run the same command again:

```bash
python pawsey_uploader.py upload /path/to/data your-bucket-name
```

The tool will:

* continue from where it stopped
* skip files already uploaded

---

# Check your upload

After uploading:

```bash
python pawsey_uploader.py list your-bucket-name
```

---

# Important Notes

---

## 🔴 Do NOT change rclone settings

The tool already applies required Pawsey settings automatically.

---

## 🔴 Keep your computer awake

For large uploads (e.g. drone data):

* prevent sleep mode
* keep internet stable

---

## 🔴 Use correct bucket name

You will be given a bucket like:

* `adelaideu-data`
* `uwa-data`
* `csu-data`

 You can only access your assigned bucket

---

# ❗ Troubleshooting

---

## ❌ “Access Denied”

* Check bucket name
* Ensure your access is set up
* Contact project team

---

## ❌ “rclone not found”

Install rclone:

```bash
brew install rclone
```

---

## ❌ Upload slow

* Check internet connection
* Try again

---

# Example Workflow

```bash
# Upload data
python pawsey_uploader.py upload ./data adelaideu-data

# If interrupted (later or next day)
python pawsey_uploader.py upload ./data adelaideu-data

# Check uploaded files
python pawsey_uploader.py list adelaideu-data
```

---

#  Security

* Do NOT share your access keys
* Each user can only access their own bucket

---