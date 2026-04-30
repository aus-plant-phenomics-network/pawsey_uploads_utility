import argparse
import subprocess
import sys
import os

RCLONE_REMOTE = "pawsey-user"

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
        "--s3-acl", "bucket-owner-full-control",
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

    # List command
    list_parser = subparsers.add_parser("list", help="List bucket contents")
    list_parser.add_argument("bucket", help="Bucket name")

    args = parser.parse_args()

    if args.command == "upload":
        upload(args.source, args.bucket)
    elif args.command == "list":
        list_bucket(args.bucket)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()