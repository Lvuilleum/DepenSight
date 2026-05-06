import ast 
import pathlib

# This file is the crawler that looks through the project you want to analyze.
# We want to look in the directory of the file and look only at the dependence of the files. 

# find all the dependency in a .py file
def findDependence(fileName):
    with open(fileName, 'r') as f:
        sourceCode = f.read()

    imported_list = []
    tree = ast.parse(sourceCode)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_list.append(alias.name)
        if isinstance(node, ast.ImportFrom):
            if node.module:
                imported_list.append(node.module)
    return imported_list


# find all file in a directory
#return List[File]
def findFile(directoryName):
    return list(pathlib.Path(directoryName).rglob("*.py"))

