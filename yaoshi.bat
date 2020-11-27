@echo ON
echo **********************************************
echo.
echo                 职业药师
echo.
echo **********************************************
TIMEOUT /T 1 
rem 注释：(^)号这里是换行符，与后面的"&"前后要保持前后有空格
cmd /k "^
cd /d D:\Python_projects\trade_projects\virtualenv\Scripts\^
 & activate^
 & cd /d D:\Python_projects\trade_projects\opencv_projects\yaoshi^
 & python main.py runserver" 

pause
echo 启动完毕，准备退出。。。  