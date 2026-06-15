
# Pawsey Upload Tool (APPN)

A simple tool to upload, download, and manage data on Pawsey (Acacia S3).

This tool:

*  Uploads files and folders
*  Downloads files and folders from a bucket
*  Deletes files and folders from a bucket
*  Lets you view your uploaded files
*  Handles all Pawsey technical settings internally

---

# Quick Start (4 Steps)

---

## 1. Download this tool

You need to download this tool to your computer first.

### Option A: Download as a zip file (easiest)

1. Go to [https://github.com/aus-plant-phenomics-network/pawsey_uploads_utility](https://github.com/aus-plant-phenomics-network/pawsey_uploads_utility)
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. Open the downloaded zip file and extract (unzip) it to a folder you'll remember, for example:
   - **Windows:** `C:\Users\YourName\Desktop\pawsey_uploads_utility`
   - **Mac:** `/Users/YourName/Desktop/pawsey_uploads_utility`

### Option B: Using git (if you have git installed)

Open **Command Prompt** (Windows) or **Terminal** (Mac) and type:

```
git clone https://github.com/aus-plant-phenomics-network/pawsey_uploads_utility.git
```

This creates a folder called `pawsey_uploads_utility` in your current location.

---

## 2. Install Python and rclone

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

## 3. Configure your Pawsey access

Open **Command Prompt** (Windows) or **Terminal** (Mac) and type:

```
rclone config
```

It will ask you a series of questions. Follow along below — type the answer shown after each prompt and press **Enter**:

| It asks | You type |
|---------|----------|
| `e/n/d/r/c/s/q>` | `n` (for new remote) |
| `name>` | `pawsey-user` |
| `Storage>` | `s3` |
| `provider>` | `Ceph` |
| `env_auth>` | `false` |
| `access_key_id>` | Your access key (see below where to find it) |
| `secret_access_key>` | Your secret key (see below where to find it) |
| `region>` | Just press **Enter** (leave blank) |
| `endpoint>` | `https://projects.pawsey.org.au` |
| `location_constraint>` | Just press **Enter** (leave blank) |
| `acl>` | Just press **Enter** (leave blank) |

For any other questions it asks, just press **Enter** to accept the default until you see:

```
y) Yes this is OK
```

Type `y` and press **Enter**. Then type `q` to quit the config.

### Where to find your access key and secret key:

1. Go to the **Pawsey portal** and log in
2. Navigate to **Acacia**
3. Click **"Create New Key"**
4. Copy the **Access ID** — this is your `access_key_id`
5. Copy the **Secret Key** — this is your `secret_access_key`

> **Important:** Save these keys somewhere safe. The secret key is only shown once!
---

## 4. Upload data

First, you need to **navigate to the tool's folder** in your Command Prompt or Terminal. This is the folder you downloaded in Step 1.

**Windows** — open **Command Prompt** and type:

```
cd C:\Users\YourName\Desktop\pawsey_uploads_utility
```

**Mac** — open **Terminal** and type:

```
cd /Users/YourName/Desktop/pawsey_uploads_utility
```

> Replace the path above with wherever you saved the folder in Step 1.

Now run the upload command:

```
python pawsey_uploader.py upload /path/to/data your-bucket-name
```

> **Mac users:** use `python3` instead of `python`

### Example:

```
python pawsey_uploader.py upload ./drone-data adelaideu-data
```

> **Tip:** You need to be inside the `pawsey_uploads_utility` folder every time you run a command. If you close and reopen Command Prompt / Terminal, you'll need to `cd` into the folder again.

---

# Commands

---

##  Upload files or folders

```bash
python pawsey_uploader.py upload <local_path> <bucket>
```

 Uploads all files from your computer to Pawsey

---

##  Download files or folders

```bash
python pawsey_uploader.py download <remote_path> <local_destination> <bucket>
```

Downloads files from your bucket to your computer.

### Examples:

```bash
# Download a folder
python pawsey_uploader.py download "APEx_day_1/20260415/run_00/T1_proc/products" ./products/ usyd-data

# Download a single file
python pawsey_uploader.py download "APEx_day_1/somefile.txt" ./local-dest/ usyd-data
```

---

##  Delete files or folders

```bash
python pawsey_uploader.py delete <remote_path> <bucket>
```

Deletes files from your bucket. You will be asked to confirm before anything is deleted.

### Examples:

```bash
# Delete a specific file
python pawsey_uploader.py delete "APEx_day_1/somefile.txt" usyd-data

# Delete an entire folder
python pawsey_uploader.py delete "APEx_day_1/20260415/run_00" usyd-data
```

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

# Download a folder from the bucket
python pawsey_uploader.py download "drone-data/flight_01" ./local-folder/ adelaideu-data

# Delete a file from the bucket
python pawsey_uploader.py delete "drone-data/old-file.txt" adelaideu-data
```

---

#  Security

* Do NOT share your access keys
* Each user can only access their own bucket

---