[![Website](https://img.shields.io/website-up-down-green-red/http/shields.io.svg?label=elky-essay)](https://elky84.github.io)
![Made with](https://img.shields.io/badge/made%20with-Python-brightgreen.svg)
![Made with](https://img.shields.io/badge/made%20with-Jupyter-blue.svg)

![GitHub forks](https://img.shields.io/github/forks/elky84/text-search.svg?style=social&label=Fork)
![GitHub stars](https://img.shields.io/github/stars/elky84/text-search.svg?style=social&label=Stars)
![GitHub watchers](https://img.shields.io/github/watchers/elky84/text-search.svg?style=social&label=Watch)
![GitHub followers](https://img.shields.io/github/followers/elky84.svg?style=social&label=Follow)

![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)
![GitHub repo size in bytes](https://img.shields.io/github/repo-size/elky84/text-search.svg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/elky84/text-search.svg)

# text-search

문자열 검색 예시 프로젝트입니다.

## usage

`.env` 또는 `.env.local` 파일에 

```properties
target_path=markdown
find_text=Hello
```

값을 변경하면 됨

target_path는 폴더임

## installation

### for mac

```bash
virtualenv venv

source venv/bin/activate

pip install -r requirements.txt
```

### for windows

```bash
virtualenv venv

.\venv\Scripts\activate.ps1

pip install -r requirements.txt

pin install pywin32
```

## Notebook

`/notebook` - Jupyter Notebook을 사용한 분석 코드들

다음과 같이 실행할 수 있습니다.

```python
jupyter notebook
```