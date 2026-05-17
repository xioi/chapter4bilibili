# chapter4bilibili
将（主要是fcpx导出的）内含章节标记的视频文件中的章节信息提取出来，并转换成哔哩哔哩可用的文本格式
## 示范：
```bash
$ ./chapter2bilibili.py 周年祭.mov
00:00 开幕式
01:38 《贱侠》
05:07 《咒术回战第三季OP》
07:44 《奶油苏打和冕型灯》
12:06 《百战成诗》
21:39 《Yes！BanG-Dream》
27:44 观众互动
52:44 《everything is everything》
57:00 《寻味于心》
61:31 《夏洛特特烦恼》
78:07 《Sugar Hate》
82:23 舞蹈串烧
86:20 综漫走秀
99:07 《six feet under》
103:43 《未名之剧》
```
## 使用方法
```bash
$ ./chapter2bilibili.py <视频文件路径>
```
## 需求
安装`ffprobe`（`ffmpeg`自带解析工具）和`python3`
