# tab2sql
将tab格式的表，转化为sql文件
## tab格式说明
tab文件是值以tab作为分隔符的utf8文本文件，并且可以用excel打开，在里面使用公式。  

## 生成sql说明
生成的SQL文件，包含`truncate`和`insert`语句。

## 使用说明
1. 对指定文件夹下的所有tab文件，进行转换。
2. 在`sqls`文件夹下生成对应的sql文件
3. 在`Convert.py`中可以配置`dirPath`需要转化的路径
4. 支持log级别输出

## 用法
```
python Convert.py
```

## 微信和公众号
![微信](./image/wechatQR.png)
![公众号](./image/cainiaopark.jpg)