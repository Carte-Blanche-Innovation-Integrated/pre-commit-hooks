import argparse
import logging

logging.basicConfig(level=logging.DEBUG)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='migration_dirs',action="store", nargs='*')
    args = parser.parse_args()
    checklist = []
    filenames = []
    logging.debug(args.migration_dirs )
    MIGRATION_DIR = filter(lambda dir: "migrations/" in dir, args.migration_dirs )
    for file in MIGRATION_DIR:
        arr = file.split("/")
        filenames.append(arr[-1])

    for filename in filenames:
        arr = filename.split("_")
        checklist.append(arr[0])
    logging.debug(filenames)

    if len(set(checklist)) == len(checklist):
        logging.debug(checklist)
    else:
        logging.debug("failed due to migrations")
        raise ValueError("Duplicates In Migrations .")
    


if __name__ == "__main__":
    raise SystemExit(main())
