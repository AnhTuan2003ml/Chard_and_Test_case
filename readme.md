# Chord

## Chức năng chính của Chord

Chord là một giao thức phân tán cho phép quản lý và truy xuất dữ liệu trong mạng P2P (peer-to-peer). Chức năng chính của Chord bao gồm:

1. **Quản lý nút**: Chord cho phép thêm, xóa và quản lý các nút trong mạng một cách hiệu quả, đảm bảo rằng mạng có thể mở rộng mà không làm giảm hiệu suất.

2. **Tìm kiếm nhanh chóng**: Cung cấp khả năng tìm kiếm nhanh chóng cho các khóa trong mạng, giúp người dùng dễ dàng truy cập dữ liệu.

3. **Phân phối dữ liệu đồng đều**: Dữ liệu được phân phối đồng đều giữa các nút, tối ưu hóa việc lưu trữ và truy cập.

4. **Khả năng phục hồi**: Chord có khả năng phục hồi tốt khi một hoặc nhiều nút bị lỗi, đảm bảo tính khả dụng của dữ liệu.

5. **Khả năng mở rộng**: Hệ thống có thể mở rộng dễ dàng khi thêm nhiều nút mới mà không làm giảm hiệu suất.

## Chức năng các hàm

Dưới đây là mô tả chức năng của các hàm chính trong Chord:

1. **`binarySearch(alist, item)`**: 
   - Thực hiện tìm kiếm nhị phân trong danh sách `alist` để tìm `item`. Trả về `True` nếu tìm thấy phần tử, nếu không trả về chỉ số của phần tử gần nhất.

2. **`successor(L, n)`**: 
   - Tìm phần tử nhỏ nhất trong danh sách `L` mà lớn hơn hoặc bằng `n`. Nếu không có, trả về `None`.

3. **`get_fingers(nodes, m)`**: 
   - Xây dựng bảng ngón tay (finger table) cho một danh sách các nút và giá trị `m`. Bảng ngón tay giúp tối ưu hóa việc tìm kiếm trong mạng.

4. **`get_key_loc(nodes, k, m)`**: 
   - Tìm vị trí của khóa `k` trong mạng DHT (Distributed Hash Table) dựa trên danh sách các nút và kích thước vòng tròn `2^m`.

5. **`get_query_path(nodes, k, n, m)`**: 
   - Tính toán đường đi truy vấn cho một danh sách các nút trong DHT, khóa `k` cần tìm, nút xuất phát `n` và kích thước vòng tròn `2^m`.

## Test Cases

Các test case dưới đây được sử dụng để kiểm tra tính chính xác và hiệu suất của các hàm trong Chord.

### 1. Test Case cho `get_fingers(nodes, m)`

- **Mục đích**: Kiểm tra xem bảng ngón tay được xây dựng chính xác cho một danh sách các nút và giá trị `m`.
- **Đầu vào**:
  - `nodes`: `[112, 96, 80, 16, 32, 45]`
  - `m`: `7`
- **Kết quả mong đợi**: Bảng ngón tay chính xác cho từng nút trong danh sách.

### 2. Test Case cho `get_key_loc(nodes, k, m)`

- **Mục đích**: Kiểm tra xem vị trí của khóa `k` được xác định chính xác trong DHT.
- **Đầu vào**:
  - `nodes`: `[112, 96, 80, 16, 32, 45]`
  - `k`: `42`
  - `m`: `7`
- **Kết quả mong đợi**: Vị trí của khóa `42` trong mạng, phải là `45`.

### 3. Test Case cho `get_query_path(nodes, k, n, m)`

- **Mục đích**: Kiểm tra xem đường đi truy vấn được tính toán chính xác từ nút xuất phát `n` đến vị trí của khóa `k`.
- **Đầu vào**:
  - `nodes`: `[112, 96, 80, 16, 32, 45]`
  - `k`: `42`
  - `n`: `80` (nút xuất phát)
  - `m`: `7`
- **Kết quả mong đợi**: Đường đi truy vấn từ nút `80` đến vị trí của khóa `42` phải là `[80, 16, 32, 45]`.

### 4. Test Case cho `get_query_path` với các nút xuất phát khác nhau

- **Mục đích**: Kiểm tra tính chính xác của đường đi truy vấn từ các nút xuất phát khác nhau.
- **Đầu vào**:
  - `nodes`: `[112, 96, 80, 16, 32, 45]`
  - `k`: `42`
  - `n`: `96` (nút xuất phát)
  - `m`: `7`
- **Kết quả mong đợi**: Đường đi truy vấn từ nút `96` đến v�� trí của khóa `42` phải là `[96, 32, 45]`.

- **Đầu vào**:
  - `n`: `45` (nút xuất phát)
- **Kết quả mong đợi**: Đường đi truy vấn từ nút `45` đến vị trí của khóa `42` phải là `[45]`.

## Thực thi test case

Để chạy các test case cho Chord, bạn có thể sử dụng lệnh sau trong terminal:

```bash
python -m unittest .\test_chord.py
```

Lệnh này sẽ thực thi tất cả các test case được định nghĩa trong file `test_chord.py` và hiển thị kết quả trên màn hình.

