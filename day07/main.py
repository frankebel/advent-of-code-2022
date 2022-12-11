# https://adventofcode.com/2022/day/7

class Directory:
    def __init__(self, name: str, children: dict = dict(), parent=None):
        self.name = name
        self.children = children
        self.parent: Directory = parent if parent else self

    def __repr__(self):
        return f"{self.name}"

    def add_child_dir(self, dir: str):
        child_dir = Directory(name=dir, children=dict(), parent=self)
        self.children[dir] = child_dir

    def add_child_file(self, file: str, size: int):
        child_file = File(name=file, parent=self, size=size)
        self.children[file] = child_file

    def size(self):
        size = 0
        for child in self.children.values():
            size += child.size() if type(child) == Directory else child.size
        return size

    def tree(self):
        res = [str(self)]
        for child in self.children.values():
            res.extend([child.tree()]) if type(child) == Directory \
                else res.extend([str(child)])
        return res


class File:
    def __init__(self, name: str, parent: Directory, size: int = 0):
        self.name = name
        self.parent = parent
        self.size = size

    def __repr__(self):
        return f"{self.name} {self.size}"


class FileSystem:
    def __init__(self, name: str):
        self.name = name
        self.root = Directory("/")
        self.working_dir = self.root

    def cd(self, dir: str):
        """Change directory."""
        match dir:
            case "/":
                self.working_dir = self.root
            case "..":
                self.working_dir = self.working_dir.parent
            case _:
                self.working_dir = self.working_dir.children[dir]


def part1(dir: Directory, threshold: int = 0):
    size = dir.size() if dir.size() <= threshold else 0
    for child in dir.children.values():
        if type(child) == Directory:
            size += part1(child, threshold)
    return size


def part2(dir: Directory, threshold=0):
    result = dir.size() if dir.size() >= threshold else float("inf")

    for child in dir.children.values():
        if type(child) == Directory:
            result = min(result, part2(child, threshold=threshold))
    return result


data = open("input.txt", "r").read().strip().split("\n")

fs = FileSystem(name="fs")
for line in data:
    match line.split():
        case ["$", "cd", dir]:
            fs.cd(dir)
        case ["$", "ls"]:
            pass
        case ["dir", dir]:
            fs.working_dir.add_child_dir(dir)
        case [size, file]:
            fs.working_dir.add_child_file(file, int(size))

# Part 1
threshold = 100_000
p1 = part1(fs.root, threshold)

# Part 2
total = 70_000_000
needed = 30_000_000
threshold = fs.root.size() + needed - total
p2 = part2(fs.root, threshold=threshold)

print(f"Solution Part 1: {p1}")
print(f"Solution Part 2: {p2}")
