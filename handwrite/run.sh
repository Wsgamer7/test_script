#!/bin/bash
rm output/*
echo "处理中..."
python3 simulator.py
convert $(ls -v output/*.jpg) output/output.pdf
echo "生成的文档在output文件夹\n准备了5个字体自己分别试一下\n纸张默认A4白纸 可以自己换\n 字的大小间距自己调代码\n"
rm output/*.jpg
