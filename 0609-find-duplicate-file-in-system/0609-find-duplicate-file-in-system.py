
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = {}

        for path in paths:
            parts = path.split()
            directory = parts[0]

            for file_info in parts[1:]:
                name, content = file_info.split("(", 1)
                content = content[:-1]

                full_path = directory + "/" + name

                if content not in content_map:
                    content_map[content] = []

                content_map[content].append(full_path)

        return [
            files
            for files in content_map.values()
            if len(files) > 1
        ]
