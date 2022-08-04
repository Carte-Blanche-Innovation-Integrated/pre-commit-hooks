import argparse
import logging

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='migration_dirs',action="store", nargs='*')
    args = parser.parse_args()
    checklist = []
    filenames = []
    print(args.migration_dirs )
    MIGRATION_DIR = filter(lambda dir: "migrations/" in dir, args.migration_dirs )
    for file in MIGRATION_DIR:
        arr = file.split("/")
        filenames.append(arr[-1])

    for filename in filenames:
        arr = filename.split("_")
        checklist.append(arr[0])
    print(filenames)

    if len(set(checklist)) == len(checklist):
        print(checklist)
        raise ValueError("Duplicates In Migrations .")
    else:
        print("failed due to migrations")
        raise ValueError("Duplicates In Migrations .")
    


if __name__ == "__main__":
    raise SystemExit(main())
