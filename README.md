# AutoClick
自用的Android模拟点击程序

## 切换输入法
因为ADB不能直接输入Unicode，所以重写了输入法，通过`broadcast`的方式将Unicode转化为Base64的字符串。如果想正常使用需安装[ADBKeyBoard](https://github.com/senzhk/ADBKeyBoard)，然后切换输入法。

```bash
# 切换为Adb的输入法
adb shell ime set com.android.adbkeyboard/.AdbIME
# 切换为自带输入法（我的情况）
adb shell ime set com.sec.android.inputmethod/.SamsungKeypad
# 查看所有输入法
adb shell ime list -a
```

## 运行程序
```bash
# mingyuan
python mingyuan.py
# yuandu
python yuandu.py
```
