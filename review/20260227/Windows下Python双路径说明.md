# Windows 下 Python 双路径说明

本文说明在 Windows 命令行执行 `where python` 时为何会看到两个 Python 路径，以及如何区分与验证实际使用的解释器。

---

## 目录

1. [现象说明](#1-现象说明)
2. [两个路径分别是什么](#2-两个路径分别是什么)
3. [WindowsApps 中的 Python 详解](#3-windowsapps-中的-python-详解)
4. [如何确认正在使用的是哪个](#4-如何确认正在使用的是哪个)
5. [如何区分真实 Python 与存根](#5-如何区分真实-python-与存根)
6. [WindowsApps 中其他常见重定向器](#6-windowsapps-中其他常见重定向器)

---

## 1. 现象说明

在命令行执行：

```text
C:\Users\admin>python --version
Python 3.11.4

C:\Users\admin>where python
D:\python\python.exe
C:\Users\admin\AppData\Local\Microsoft\WindowsApps\python.exe
```

系统会列出两个 Python 路径。原因是：一个是你**手动安装的完整 Python**，另一个是 **Windows 自带的存根/重定向器**，并非完整功能的 Python。

---

## 2. 两个路径分别是什么

### D:\python\python.exe

- 用户**手动安装**的 Python
- 位于 D 盘 `python` 目录
- 具备完整功能的 Python 解释器

### C:\Users\admin\AppData\Local\Microsoft\WindowsApps\python.exe

- **不是用户安装的**，而是 **Windows 系统预装**的组件
- 属于 **App Installer（应用安装程序）** 的一部分
- 本质是 **Python 存根/重定向器（Stub/Redirector）**，不是完整 Python
- 文件体积很小（通常几百 KB），而完整 Python 安装为几十 MB

---

## 3. WindowsApps 中的 Python 详解

### 它是什么

- **Python 存根/重定向器**
- Windows 10/11 自带的 App Installer 功能之一
- 路径中一定包含 `WindowsApps`

### 主要功能

当在命令行输入 `python` 时：

- **未安装 Python** → 提示从 Microsoft Store 安装
- **已安装 Python** → 将命令转发给系统中真实的 Python（如 `D:\python\python.exe`）

### 微软这样做的原因

- 方便用户在命令行直接触发 Python 安装
- 提供类似 Linux 包管理器的体验
- 减少出现「python 不是内部或外部命令」的情况

---

## 4. 如何确认正在使用的是哪个

在命令行执行：

```bash
python -c "import sys; print(sys.executable)"
```

若已正确使用手动安装的 Python，输出应为：`D:\python\python.exe`。

---

## 5. 如何区分真实 Python 与存根

| 特征       | 真实 Python（如 D:\python\python.exe） | WindowsApps 存根                          |
|------------|----------------------------------------|-------------------------------------------|
| 文件大小   | 几十 MB 量级                           | 通常仅几百 KB                             |
| 路径       | 用户安装目录                           | 路径中包含 `WindowsApps`                  |
| 发布者     | Python Software Foundation 等        | 右键属性中多为 Microsoft Corporation     |

也可直接对比两个文件大小：

```bash
dir D:\python\python.exe
dir C:\Users\admin\AppData\Local\Microsoft\WindowsApps\python.exe
```

---

## 6. WindowsApps 中其他常见重定向器

`WindowsApps` 目录下还有多种类似的重定向器，例如：

- `python.exe` — Python 存根
- `python3.exe` — Python 3 存根
- `pip.exe` — pip 存根
- 其他开发工具的重定向器

它们都不是完整安装，仅负责检测并转发到真实程序或引导到商店安装。
