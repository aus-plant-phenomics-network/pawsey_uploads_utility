import argparse
import subprocess
import sys
import os

RCLONE_REMOTE = "pawsey-user"
ACL_HEADER = "X-Amz-Acl:bucket-owner-full-control"


def run_command(cmd):
    try:
        print("\nRunning:", " ".join(cmd))
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("\n❌ Error: Command failed.")
        sys.exit(1)


def upload(source, bucket):
    if not os.path.exists(source):
        print("❌ Source path does not exist")
        sys.exit(1)

    cmd = [
        "rclone", "copy", source, f"{RCLONE_REMOTE}:{bucket}",
        "--header", ACL_HEADER,
        "--s3-no-check-bucket",
        "--progress",
        "--transfers", "8",
        "--checkers", "16",
        "--retries", "5",
        "--low-level-retries", "10"
    ]

    run_command(cmd)
    print("\n✅ Upload completed successfully!")


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