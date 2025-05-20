import json


class JsonCookieHandler:
    def __init__(self, file_path: str = "./cookies/cookies.json"):
        self.file_path = file_path

    def cookies_file_to_dict(self) -> dict[str, str] | None:
        result = {}
        try:
            with open(self.file_path, 'r') as file:
                file_content = file.read()

                # Parse the JSON data
                json_data: list = json.loads(file_content)

                for cookie in json_data:
                    result.update({cookie["name"]: cookie["value"]})

        except FileNotFoundError as error:
            print("File doesn't exist or file path invalid")

        except json.JSONDecodeError as error:
            print("file contains invalid JSON")

        if len(result) == 0:
            return None

        return result
