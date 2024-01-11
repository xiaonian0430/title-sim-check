# 文章标题相似丢检测模型

## 服务器环境要求：

**最低配置：**
- 2G内存 
- 40G磁盘
- 2v CPU



**软件：**
```
python3.8.10

pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ 
```
 
参考网站：

https://blog.csdn.net/qq_43692950/article/details/132645864

https://blog.51cto.com/elasticsearch/5768473

测试数据
https://github.com/Toyhom/Chinese-medical-dialogue-data



## 正式环境部署
 
**接口服务**
```
 ## 命令行运行
 python3 run.py
 
 ## 守护进程运行
 nohup python3 run.py >/dev/null 2>/dev/null &
 
 或者直接运行shell脚本
```
 
 访问地址示例：http://127.0.0.1:5000/text/sim?text_one=测试&text_two=测试2
 

**反向代理服务**
 
```
 # 进入nginx /usr/local/nginx/conf 配置文件目录下
 cd /usr/local/nginx/conf
 
 # 修改 nginx.conf
 vi nginx.conf
 
 # 修改内容如下
 upstream text_sim_api{
     server 127.0.0.1:5000 weight=1;
     server 127.0.0.1:5000 weight=1;
     server 127.0.0.1:5000 weight=1;
 }
 server {
     listen 80;
     server_name  localhost;
     index  index.html index.htm index.php;
  
     ## send request back to apache ##
     location / {
         #需要转发请求的服务器  负载均衡也是如此配置
         proxy_pass  http://text_sim_api;
 
         #Proxy Settings
         proxy_redirect     off; #是否跳转
         proxy_set_header   Host             $host; #请求要转发的host
         proxy_set_header   X-Real-IP        $remote_addr;#请求的远程地址    这些在浏览器的header都可看，不一一解释
         proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
         proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
         proxy_max_temp_file_size 0;
         proxy_connect_timeout      300;  #连接前面的服务器超时时间
         proxy_send_timeout         300;  #请求转发数据报文的超时时间
         proxy_read_timeout         300;  #读取超时时间
         proxy_buffer_size          64k;  #缓冲区的大小
         proxy_buffers              4 32k;
         proxy_busy_buffers_size    64k; #proxy_buffers缓冲区，网页平均在32k以下的
         proxy_temp_file_write_size 64k; #高负荷下缓冲大小（proxy_buffers*2）
    }
 }
```


