# PyCharm 中为 quickstart.py 创建独立 Debug 配置（方法一）

当右键 `quickstart.py` 只出现 `Debug 'pytest in quickstart.py'` 时，说明 IDE 当前按测试方式运行该文件。  
可通过手动创建 **Python 脚本运行配置** 来解决。

## 适用场景

- `quickstart.py` 脚本模式可运行；
- 右键菜单只有 pytest 调试选项；
- 需要用断点调试 `quickstart.py`，而不是 pytest。

## 操作步骤

1. 点击顶部运行配置下拉框，选择 `Edit Configurations...`。
2. 在弹窗左上角点击 `+`，选择 `Python`。
3. 按下列参数创建配置：
   - `Name`: `quickstart`
   - `Script path`: 选择 `week4/perception-tools/quickstart.py`
   - `Working directory`: `week4/perception-tools`
   - `Python interpreter`: 选择已安装 `requirements.txt` 依赖的解释器（建议项目虚拟环境）。
4. 点击 `Apply` / `OK` 保存。
5. 在顶部配置下拉框中选择 `quickstart`，点击 Debug 图标运行。

## 验证结果

- 顶部应显示 `quickstart` 配置（而非 pytest 配置）；
- 调试控制台不再出现 `Testing started` / `Empty suite`；
- 可正常命中 `quickstart.py` 断点并执行各测试步骤。

## 常见问题

- **仍出现 pytest 配置**：确认顶部选中的不是旧的 pytest 配置。
- **模块导入报错**：检查 `Python interpreter` 与你执行 `pip install -r requirements.txt` 的环境是否一致。
- **路径带空格**：尽量通过文件选择器设置 `Script path`，避免手输路径错误。

