# Flask

## TODO

1時間ごとのデータをアーカイブ。
ホスティングでバックエンドをスケジュールできるところがあるかどうか。
Node.jsでもいいのか。
みんなの外為のデータだと４時間足がない。
それをPandasでリサンプルしていた。
同じことをNode.jsでやるのは面倒そう。

## setup

```
% pip3 install --user Flask
Collecting Flask
  Downloading https://files.pythonhosted.org/packages/9b/93/628509b8d5dc749656a9641f4caf13540e2cdec85276964ff8f43bbb1d3b/Flask-1.1.1-py2.py3-none-any.whl (94kB)
     |████████████████████████████████| 102kB 561kB/s 
Collecting itsdangerous>=0.24 (from Flask)
  Downloading https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
Collecting Werkzeug>=0.15 (from Flask)
  Downloading https://files.pythonhosted.org/packages/ce/42/3aeda98f96e85fd26180534d36570e4d18108d62ae36f87694b476b83d6f/Werkzeug-0.16.0-py2.py3-none-any.whl (327kB)
     |████████████████████████████████| 327kB 1.1MB/s 
Requirement already satisfied: Jinja2>=2.10.1 in /Users/user/Library/Python/3.7/lib/python/site-packages (from Flask) (2.10.1)
Collecting click>=5.1 (from Flask)
  Downloading https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl (81kB)
     |████████████████████████████████| 81kB 1.1MB/s 
Requirement already satisfied: MarkupSafe>=0.23 in /Users/user/Library/Python/3.7/lib/python/site-packages (from Jinja2>=2.10.1->Flask) (1.1.1)
Installing collected packages: itsdangerous, Werkzeug, click, Flask
  WARNING: The script flask is installed in '/Users/user/Library/Python/3.7/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed Flask-1.1.1 Werkzeug-0.16.0 click-7.0 itsdangerous-1.1.0
```

## run

~/Library/Python/3.7/bin/flask

```
 % echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin:/Library/Apple/bin
% export PATH=$PATH:~/Library/Python/3.7/bin
% echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin:/Library/Apple/bin:/Users/user/Library/Python/3.7/bin
```

```
% env FLASK_APP=hello.py flask run
 * Serving Flask app "hello.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not import "hello".
```

```
export FLASK_ENV=development
```

実行までのまとめ。

```
export PATH=$PATH:~/Library/Python/3.7/bin
export FLASK_ENV=development
env FLASK_APP=mtf.py flask run
```

http://127.0.0.1:5000/static/fullscreen.html
