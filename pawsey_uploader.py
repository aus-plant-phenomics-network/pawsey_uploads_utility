import argparse
import subprocess
import sys
import os

RCLONE_REMOTE = "aaneja"

def run_command(cmd):
    try:
        print("\nRunning:", " ".join(cmd))
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("\n Error: Command failed.")
        sys.exit(1)


def upload(source, bucket):
    if not os.path.exists(source):
        print(" Source path does not exist")
        sys.exit(1)

    # If source is a folder, preserve the folder name in the destination
    dest = f"{RCLONE_REMOTE}:{bucket}"
    if os.path.isdir(source):
        folder_name = os.path.basename(os.path.normpath(source))
        dest = f"{RCLONE_REMOTE}:{bucket}/{folder_name}"

    cmd = [
        "rclone", "copy", source, dest,
        "--s3-no-check-bucket",
        "--s3-disable-checksum",
        "--s3-chunk-size", "64M",
        "--s3-upload-concurrency", "4",
        "--multi-thread-streams", "0",
        "--progress",
        "--stats", "10s",
        "--transfers", "1",
        "--checkers", "16",
        "--retries", "5",
        "--low-level-retries", "10",
        "-v"
    ]

    run_command(cmd)
    print("\n Upload completed successfully!")


def download(remote_path, dest, bucket):
    source = f"{RCLONE_REMOTE}:{bucket}/{remote_path}"
    cmd = [
        "rclone", "copy", source, dest,
        "--progress",
        "--transfers", "4",
        "--checkers", "16",
        "--retries", "5",
        "--low-level-retries", "10",
        "-v"
    ]
    run_command(cmd)
    print("\n Download completed successfully!")


def delete(remote_path, bucket):
    target = f"{RCLONE_REMOTE}:{bucket}/{remote_path}"
    print(f"\n⚠️  You are about to delete: {target}")
    confirm = input("Are you sure? (yes/no): ").strip().lower()
    if confirm != "yes":
        print(" Cancelled.")
        return
    cmd = [
        "rclone", "delete", target,
        "-v"
    ]
    run_command(cmd)
    print("\n Delete completed successfully!")


def list_bucket(bucket):
    cmd = [
        "rclone", "ls", f"{RCLONE_REMOTE}:{bucket}"
    ]
    run_command(cmd)


def main():
    parser = argparse.ArgumentParser(
        description="📦 Pawsey Upload Tool"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Upload command
    upload_parser = subparsers.add_parser("upload", help="Upload files/folders")
    upload_parser.add_argument("source", help="Local file or folder path")
    upload_parser.add_argument("bucket", help="Target bucket")

    # Download command
    download_parser = subparsers.add_parser("download", help="Download files/folders from bucket")
    download_parser.add_argument("remote_path", help="Remote path within the bucket (e.g. folder/subfolder/file.txt)")
    download_parser.add_argument("dest", help="Local destination folder")
    download_parser.add_argument("bucket", help="Bucket name")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete files/folders from bucket")
    delete_parser.add_argument("remote_path", help="Remote path to delete (e.g. folder/subfolder/file.txt)")
    delete_parser.add_argument("bucket", help="Bucket name")

    # List command
    list_parser = subparsers.add_parser("list", help="List bucket contents")
    list_parser.add_argument("bucket", help="Bucket name")

    args = parser.parse_args()

    if args.command == "upload":
        upload(args.source, args.bucket)
    elif args.command == "download":
        download(args.remote_path, args.dest, args.bucket)
    elif args.command == "delete":
        delete(args.remote_path, args.bucket)
    elif args.command == "list":
        list_bucket(args.bucket)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()