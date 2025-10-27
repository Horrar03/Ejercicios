"""
def remove_char(s):
    if len(s) == 2:
        return ''
    else:
        return s[1:-1]
        
        
print(remove_char("ABCDEFG"))
print(remove_char("AB"))
print(remove_char("XYZ"))   
print(remove_char(" HELLO"))   
print(remove_char("PYTHON"))
print(remove_char("ABCDEFGH"))
print(remove_char("1234567890"))

"""

"""
def ips(start, end):
    def ip_a_int(ip):
        parts = list(map(int, ip.split('.')))
        return(parts[0] << 24) + (parts[1] << 16) + (parts[2] <<  8) + parts[3]
    
    return ip_a_int(end) - ip_a_int(start)

print(ips("150.0.0.0", "150.0.0.1"))
print(ips("10.0.0.0", "10.0.0.50"))

"""

from collections import defaultdict, deque

def recover_secret(triplets):
    # Step 1: Build graph and in-degree map
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    all_chars = set()

    for triplet in triplets:
        a, b, c = triplet
        all_chars.update(triplet)
        if b not in graph[a]:
            graph[a].add(b)
            in_degree[b] += 1
        if c not in graph[b]:
            graph[b].add(c)
            in_degree[c] += 1
        # Ensure all characters are in in_degree
        for ch in triplet:
            in_degree.setdefault(ch, 0)

    # Step 2: Topological sort
    queue = deque([ch for ch in all_chars if in_degree[ch] == 0])
    result = []

    while queue:
        ch = queue.popleft()
        result.append(ch)
        for neighbor in graph[ch]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ''.join(result)


triplets = [
    ['t','u','p'],
    ['w','h','i'],
    ['t','s','u'],
    ['a','t','s'],
    ['h','a','p'],
    ['t','i','s']
]
print(recover_secret(triplets))  # Output: "whatisup"
