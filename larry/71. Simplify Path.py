# 71. Simplify Path
# Medium


# Larry, https://www.youtube.com/watch?v=jCKaoPliMz0
class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = []
        
        for name in path.split("/"):
            if name == "." or name == "":
                continue
            elif name == "..":
                if len(dirs) > 0:
                    dirs.pop()
            else:
                dirs.append(name)
                
        return "/" + "/".join(dirs)
# 03/18/2022 15:50