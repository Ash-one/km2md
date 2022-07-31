import json

class Node:
    def __init__(self,data,children:list):
        self.data = data
        self.text = ' '+data['text']
        self.children = []
        for child in self.getchildren(children):
            node = Node(child['data'],child['children'])
            self.children.append(node)
        
    def getchildren(self,children:list):
        realchildren = []
        for child in children:
            if child != None:
                realchildren.append(child)
        return realchildren

def node2md(md,node:Node,layer:int):
    if node.children is None:
        return md
    else:
        for child in node.children:
            md += '#'*layer+ child.text + '\n' + node2md('',child,layer+1)
        layer += 1
        return md

if __name__ == '__main__':
    path = './语音合成.km'
    md_path = './语音合成.md'
    
    with open(path, 'r') as f:
        content = json.load(f)
    
    root = Node(content['root']['data'],content['root']['children'])
    md = '#' + root.text + '\n'
    layer = 2

    md = node2md(md,root,layer)

    with open(md_path,'w') as f2:
        f2.write(md)
    print(md)
    print('ok,please check your md file')