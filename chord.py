from pprint import pprint

def binarySearch(alist, item):
    """
    Tìm kiếm nhị phân trong danh sách alist để tìm item.
    Trả về True nếu tìm thấy phần tử, nếu không trả về điểm giữa cuối cùng trước khi tìm kiếm thất bại.
    Điểm giữa cuối cùng luôn là phần tử kế tiếp hoặc phần tử trước đó so với item (nếu không tìm thấy item).
    """
    first = 0
    last = len(alist)-1
    found = False
    
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    
    return found, midpoint

def successor(L, n):
    """
    Cho một danh sách đã được sắp xếp L và một số nguyên n, trả về phần tử nhỏ nhất trong L
    mà lớn hơn hoặc bằng n. Nếu không có, trả về None.
    """
    found, midpoint = binarySearch(L, n)
    if L[midpoint] >= n:
        return L[midpoint]
    if L[midpoint] < n:
        if midpoint == len(L)-1:
            return None
        return L[midpoint+1]


def get_fingers(nodes, m):
    """
    Xây dựng bảng ngón tay (finger table), cho một danh sách các node và giá trị m.
    """
    nodes_augment = nodes.copy()
    nodes_augment = sorted(nodes_augment)
    maxnum = pow(2, m)
    # Thêm phần tử đầu tiên vào cuối danh sách để chứa các node theo chiều kim đồng hồ của node đó
    nodes_augment.append(nodes_augment[0] + maxnum)
    
    finger_table = {}
    for node in nodes: 
        fingers = [None]*m
        for i in range(m):
            j = (node + pow(2, i)) % maxnum
            fingers[i] = successor(nodes_augment, j) % maxnum
        finger_table[node] = fingers.copy()
        
    return finger_table

def get_key_loc(nodes, k, m):
    """
    Cho một vị trí key k và vòng tròn có kích thước 2^m, cùng với danh sách các node,
    trả về vị trí của key trong DHT.
    """
    nodes_augment = nodes.copy()
    nodes_augment = sorted(nodes_augment)
    maxnum = pow(2, m)
    # Thêm phần tử đầu tiên vào cuối danh sách để chứa các node theo chiều kim đồng hồ của node đó
    nodes_augment.append(nodes_augment[0] + maxnum)
    return successor(nodes_augment, k) % maxnum


def get_query_path(nodes, k, n, m):
    """
    Tính toán đường đi truy vấn, cho một danh sách các node trong DHT, key k cần tìm, node xuất phát n và vòng tròn có kích thước 2^m.
    """
    nodes_copy = nodes.copy()
    nodes_copy = sorted(nodes_copy)
    
    k_loc = get_key_loc(nodes_copy, k, m) # Vị trí của key k
    fingers = get_fingers(nodes_copy, m) # Bảng ngón tay
    query_path = [n] # Bắt đầu đường đi với node xuất phát
    
    while(True): # Tiếp tục cho đến khi tìm được vị trí của key đúng
        if k_loc == n: # Trả về đường đi nếu đã tìm được vị trí đúng
            return query_path

        f = fingers[n]
        
        i = 0
        x = f[i]
        
        if k_loc > n: 
            # Nếu đường đi theo chiều kim đồng hồ giữa node xuất phát (n) và vị trí key (k_loc) KHÔNG bao gồm 0,
            # tất cả các node nằm trong đường đi này (x) phải thỏa mãn k_loc > x > n
            while (x < k_loc) and (x > n):
                i += 1
                if i == len(f):
                    break
                x = f[i]
                
        if k_loc < n: 
            # Nếu đường đi theo chiều kim đồng hồ giữa node xuất phát và vị trí key bao gồm 0,
            # tất cả các node nằm trong đường đi này (x) phải thỏa mãn (k_loc < x) && (n < x) hoặc (k_loc > x) && (n > x)
            while ( ((x > k_loc) and (x > n)) or ((x < k_loc) and (x < n)) ):
                i += 1
                if i == len(f):
                    break
                x = f[i]
        
        # Cập nhật node tiếp theo để truy vấn và thêm vào đường đi
        if i == 0:
            n = f[0]
        else:
            n = f[i-1]
            
        query_path.append(n)
    
if __name__ == "__main__":
    
    # DHT Chord như đã mô tả trong bài giảng 5 của tuần 3 trong khóa học Coursera Cloud Computing Concepts Part 1
    
    nodes = [112, 96, 80, 16, 32, 45] # Các node trong hệ thống P2P
    m = 7 # Vòng tròn có kích thước 2^m
    print('DHT Chord với các peer {nodes}, và m = {m} \n'.format(nodes=nodes, m=7))
    
    print('Bảng finger table: ')
    pprint(get_fingers(nodes, m))
    print()
    
    file_key = 42
    print('Vị trí file với khóa {file_key} nằm tại node {file_key_location} \n'.format(
        file_key=file_key, file_key_location=get_key_loc(nodes, file_key, m)
    ))
    
    query_node = 80
    print('Đường đi truy vấn cho file {file_key} với node xuất phát {query_node} : {query_path}'.format(
        file_key=file_key, query_node=query_node, query_path=get_query_path(nodes, file_key, query_node, m)
    ))
    
    query_node = 96
    print('Đường đi truy vấn cho file {file_key} với node xuất phát {query_node} : {query_path}'.format(
        file_key=file_key, query_node=query_node, query_path=get_query_path(nodes, file_key, query_node, m)
    ))
    
    query_node = 45
    print('Đường đi truy vấn cho file {file_key} với node xuất phát {query_node} : {query_path}'.format(
        file_key=file_key, query_node=query_node, query_path=get_query_path(nodes, file_key, query_node, m)
    ))
