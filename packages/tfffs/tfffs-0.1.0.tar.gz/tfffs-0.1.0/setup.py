from setuptools import setup, find_packages

setup(
    name="tfffs",                 # Tên thư viện
    version="0.1.0",                   # Phiên bản
    description="Feature selection based on top frequency",  # Mô tả
    author="Vu Kieu Anh",                # Tên tác giả
    author_email="vukieuanh.hnue@gmail.com",  # Email tác giả
    url="https://github.com/VuKieuAnh/TFFS",  # URL GitHub (nếu có)
    packages=find_packages(),          # Tự động tìm kiếm package
    classifiers=[                      # Phân loại thư viện
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',           # Phiên bản Python yêu cầu
)