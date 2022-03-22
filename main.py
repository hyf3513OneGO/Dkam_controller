# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

from util.camera_controller import capture_gray, capture_depth

def main():
    capture_gray('cap2')
    capture_depth('cap2')


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()


