
# Pawsey Upload Tool (APPN)

A simple tool to upload data to Pawsey (Acacia S3).

This tool:

*  Uploads files and folders
*  Automatically continues if interrupted
*  Lets you view your uploaded files
*  Handles all Pawsey technical settings internally

---

# Quick Start (3 Steps)

---

##  1. Install rclone and python

### Mac:

```bash
brew install rclone
```

To install Python:  https://pythontest.com/python/installing-python-3-14/


### Windows:

Download from: [https://rclone.org/downloads/](https://rclone.org/downloads/)

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