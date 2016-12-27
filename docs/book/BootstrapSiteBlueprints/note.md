Bootstrap实战
===============

[美] David Cochran, lan Whitley 著 李松峰 译

第1章 初识Bootstrap
-------------------

**步骤1：**下载Bootstrap源代码：https://codeload.github.com/twbs/bootstrap/zip/v3.3.7

- less文件夹：包含重要的LESS文件
- js文件夹：包含Bootstrap插件
- dist文件夹：包含预编译的css或javascript文件
- docs\examples文件夹：包含示例文件

**步骤2：**下载`HTML5 Boilerplate（H5BP）`源码，访问[h5bp.com]( http://h5bp.com )

- .htaccess文件：主要作用是保证站点性能最优。（ https://httpd.apache.org/docs/current/howto/htaccess.html ）

以下3个文件仅提供了项目的标准信息：

- humans.txt文件：这个文件记载贡献者，H5BP、Bootstrap的，还有其他贡献者。
- LICENSE.txt文件：加上用到的各种库的许可信息。
- README.md文件：增加自己项目的说明。

更新站点桌面和触摸设备的图标：

- apple-touch-icon.png：原文中记录是144px，而`v5.3.0`版本是180px。
- favicon.ico：32px见方的图标文件。

**步骤3：**将bootstrap下的fonts文件夹复制到html5-boilerplate_v5文件夹中。

增加.htaccess文件，以提高跨域友好性。代码如下：

```
<FilesMatch "\.(ttf|otf|eot|woff)$">
    <IfModule mod_headers.c>
        Header set Access-Control-Allow-Origin "*"
    </IfModule>
</FilesMatch>
```

**步骤4：**新建`html5-boilerplate_v5\js\bootstrap`文件夹，将`bootstrap\js`下的js都复制过来。

在`html5-boilerplate_v5\js\vendor`目录下包含两个文件：

- jquery-1.12.0.min.js：Bootstrap的插件都基于jQuery。
- modernizr-2.8.3.min.js：包含HTML5“垫片”（shiv）脚本，可以让IE8支持HTML5的分区（section）元素。还可以让我们更方便地检测特定浏览器的能力。

**步骤5：**打开`bootstrap-3.3.7\dist\js\bootstrap.min.js`复制内容到`html5-boilerplate_v5\js\plugins.js`文件的最后。

H5BP采用的方法是把所有插件代码都复制到一个plugins.js模版文件中，以加快站点加载速度。

**步骤6：**复制`bootstrap-3.3.7\less`文件夹到`html5-boilerplate_v5`中。

第2章 作者展示站点
-------------------

第3章 WordPress主题
-------------------

第4章 企业网站
-------------------

第5章 电子商务网站
-------------------

第6章 单页营销网站
-------------------

附录A 优化站点资源
-------------------

附录B 实现响应式图片
-------------------

附录C 让传送带支持手势
-------------------