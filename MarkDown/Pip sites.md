## 常见pip镜像源（国内源）
- 清华：https://pypi.tuna.tsinghua.edu.cn/simple
- 阿里云：http://mirrors.aliyun.com/pypi/simple/
- 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
- 华中理工大学：http://pypi.hustunique.com/
- 山东理工大学：http://pypi.sdutlinux.org/
- 豆瓣：http://pypi.douban.com/simple/
## Markdown 语法
### 基本语法
这些是 John Gruber 的原始设计文档中列出的元素。所有 Markdown 应用程序都支持这些元素。

- 元素	Markdown 语法
- 标题（Heading）	# H1 ## H2 ### H3
- 粗体（Bold）	**bold text**
- 斜体（Italic）	*italicized text*
- 引用块（Blockquote）	> blockquote
- 有序列表（Ordered List）	1. First item 2. Second item 3. Third item
- 无序列表（Unordered List）	- First item - Second item - Third item
- 代码（Code）	`code`
- 分隔线（Horizontal Rule）	---
- 链接（Link）	[title](https://www.example.com)
- 图片（Image）	![alt text](image.jpg)
### 扩展语法
这些元素通过添加额外的功能扩展了基本语法。但是，并非所有 Markdown 应用程序都支持这些元素。

- 元素 	Markdown 语法
- 表格（Table）	
| -   | Syntax    | Description |
| --- | --------- | ----------- |
| -   | Header    | Title       |
| -   | Paragraph | Text        |
- 代码块（Fenced Code Block）	```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}```
- 脚注（Footnote）	Here's a sentence with a footnote. [^1]
[^1]: This is the footnote.
- 标题编号（Heading ID）	### My Great Heading {#custom-id}
- 定义列表（Definition List）	term : definition
- 删除线（Strikethrough）	~~The world is flat.~~
- 任务列表（Task List）	- [x] Write the press release - [ ] Update the website - [ ] Contact the media

## 输入希腊字母
$\alpha$
## 插入数学结构符号
$\frac{abc}{def}$
$$\frac{abc}{def}$$
## 插入界定符
$$|$$
$$\|$$
$$
\left|\begin{matrix}
a&b&c\\
d&e&f\\
g&h&i
\end{matrix}\right|
$$
## 插入可变大小的符号
$$\sum\int\oint\iiint$$
## 插入函数名称
$$\tan(at-\pi)$$
## 插入二进制运算符和关系运输符
$$\times$$
$$\div$$
$$\cdot$$
## 插入箭头符号
$$\leftarrow$$
$$\Leftarrow$$
## 插入其他符号
$$\infty$$
$$\nabla$$
## 上下标
$$\sin^2(\theta)+\cos^2(\theta)=1$$
$$\sum_{n=1}^{\infty}k_n$$
$$\lim\limits_{x\to\infty}\exp(-x)=0$$
$$\int_a^bf(x)\,dx$$
## 矩阵
$$
\begin{bmatrix}
0&1&2\\
1&2&3\\
4&5&6\\
\end{bmatrix}
$$
$$
\begin{Bmatrix}
0&1&2\\
1&2&3\\
4&5&6\\
\end{Bmatrix}
$$
$$
\begin{vmatrix}
0&1&2\\
1&2&3\\
4&5&6\\
\end{vmatrix}
$$
$$
\begin{Vmatrix}
0&1&2\\
1&2&3\\
4&5&6\\
\end{Vmatrix}
$$
## 分段函数
$$
f(x)=\begin{cases}
2x,\,x>0\\
3x,\,x\le0\\
\end{cases}
$$
## 字体
$\mathbb{abcdefgABCDEFG}$
