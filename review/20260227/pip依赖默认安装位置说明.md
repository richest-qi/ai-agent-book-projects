# pip 依赖默认安装位置说明

当 Python 解释器安装在 `D:\python\python.exe` 时，在项目中执行 `pip install -r requirements.txt` 安装的依赖会安装到哪里？本文说明默认位置及验证方法。

---

## 目录

1. [默认安装位置](#1-默认安装位置)
2. [如何验证](#2-如何验证)

---

## 1. 默认安装位置

通过 `pip install -r requirements.txt` 安装的依赖会默认安装到**当前使用的 Python** 所对应的 `site-packages` 目录。

若你使用的是 `D:\python\python.exe`，则默认路径为：

```
D:\python\Lib\site-packages\
```

### 示例（部分包）

```
D:\python\Lib\site-packages\requests\
D:\python\Lib\site-packages\flask\
D:\python\Lib\site-packages\pandas\
...
```

---

## 2. 如何验证

### 方法一：使用 pip 查看

```bash
# 查看 pip 已安装的包及其位置
pip list -v

# 查看某个具体包的安装位置
pip show 包名
```

### 方法二：在 Python 中查看 site-packages

```bash
python -c "import site; print(site.getsitepackages())"
```

输出示例：

```
['D:\\python\\Lib\\site-packages', 'D:\\python\\Lib\\site-packages\\win32']
```

### 方法三：查看 pip 配置

```bash
pip config list
```

可查看与安装路径相关的配置（如存在自定义 `target` 等）。
