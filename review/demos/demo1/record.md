window cmd，安装方舟SDK
```
pip install 'volcengine-python-sdk[ark]'
```

```
[notice] A new release of pip is available: 25.2 -> 26.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip
ERROR: Invalid requirement: "'volcengine-python-sdk[ark]'": Expected package name at the start of dependency specifier 'volcengine-python-sdk[ark]'
```

这是一个命令行语法错误。错误提示说依赖项描述符的开头应该是包名，但这里却被引号包裹了。

**问题原因：**
在 Windows 的命令提示符（CMD）或 PowerShell 中，你使用了单引号 `' '` 来包裹包名。但在 Windows 环境下，命令行参数解析器不识别单引号作为有效的字符串分隔符（不像在 Linux 或 Mac 的终端里那样），它将单引号当成了包名的一部分，所以报错说包名无效。

**解决方法：**

有以下几种方式可以解决：

1.  **去掉引号（最简单）：**
    直接在包名上不要加任何引号。
    ```bash
    pip install volcengine-python-sdk[ark]
    ```

2.  **使用双引号（推荐，兼容性好）：**
    如果你习惯加引号，或者包名中有特殊字符，请使用双引号。
    ```bash
    pip install "volcengine-python-sdk[ark]"
    ```

**总结：**
直接在命令行中输入以下命令即可成功安装：
```bash
pip install "volcengine-python-sdk[ark]"
```

安装openai sdk
```
pip install openai
```