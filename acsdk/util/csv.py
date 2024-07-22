import csv as csv

class CSV:
    @staticmethod
    def read(file_path):
        rows = []

        print("Reading " + file_path)

        with open(file_path) as file:
            reader = csv.DictReader(file)

            for row in reader:
                rows.append(row)

        return rows

    @staticmethod
    def write(file_path, fieldnames, data):
        rows = list(map(lambda item: dict(list(item.items())), data))

        with open(file_path, "w") as file:
            writer = csv.DictWriter(file, extrasaction="ignore", fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

            writer.writeheader()
            writer.writerows(rows)

        print("CSV written to " + file_path)
