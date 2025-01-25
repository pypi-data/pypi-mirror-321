from setuptools import setup, find_packages

setup(
    name="pyPanDEG",  # 패키지 이름
    version="0.0.1",  # 초기 버전
    author="Kyutark",
    author_email="kyutkim01@korea.ac.kr",
    description="DEG Analysis Using Pan-transcriptome Data Construction",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Kyutark/pyPanDEG",  # GitHub 링크
    project_urls={
        "Documentation": "https://github.com/Kyutark/pyPanDEG",
        "Source": "https://github.com/Kyutark/SpaceBio",
    },
    packages=find_packages(where="."),  # 현재 디렉토리 기준으로 패키지 탐색
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "biopython>=1.79",
        "pandas>=1.3.0",
        "numpy>=1.21.0",
    ],
    entry_points={
        "console_scripts": [
            "run_pipeline=pyPanDEG.main_pipeline:main",  # CLI 명령어 등록
        ],
    },
    include_package_data=True,  # 추가 데이터를 포함
    keywords=["bioinformatics", "transcriptome", "DEG"],  # 키워드
)
