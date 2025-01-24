# 汉字拼音查询包 (Hanzi-Pinyin)

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?style=flat-square&logo=github)](https://github.com/neooier/hanzi-pinyin-py.git)
[![License](https://img.shields.io/github/license/neooier/hanzi-pinyin-py.svg?style=flat-square)](https://github.com/neooier/hanzi-pinyin-py/blob/main/LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/hanzi_pinyin.svg?style=flat-square)](https://pypi.org/project/hanzi_pinyin/)

<!-- [English](README_en.md) -->

## 描述
`hanzi_pinyin` 是一个用于查询汉字拼音（罗马化）的包。它提供了获取简体和详细拼音表示的工具。

## 安装
你可以使用 pip 来安装这个包：

```bash
pip install hanzi_pinyin
```

## 使用方法

### 导入包
你可以按以下方式从包中导入函数：

```python
from hanzi_pinyin import pinyin, detailed_pinyin, alls
```

### 函数

#### `pinyin(char: str) -> List[str] | None`
返回给定汉字的拼音表示列表，不带声调。

**示例:**
```python
result = pinyin('汉')  # ['han']
print(result)
```

#### `detailed_pinyin(char: str) -> List[str] | None`
返回给定汉字的详细拼音表示列表，包括声调。

**示例:**
```python
result = detailed_pinyin('汉')  # ['hàn']
print(result)
```

#### `alls() -> Dict[str, List[str]]`
返回整个汉字到含声调拼音映射的字典。

**示例:**
```python
dict_ = alls()
print(dict_['汉'])  # ['hàn']
```

## 数据来源

本包中的数据来源为：[汉语国学](https://www.hanyuguoxue.com/zidian/)

爬取脚本可见 [fetcher.ts](https://github.com/neooier/hanzi-pinyin/blob/main/cmd/fetcher.ts)

## 许可证
本包采用 MIT 许可证。

## 贡献
欢迎贡献！请提交问题或拉取请求。

## 作者
- Neooier
